import random
import os
from mido import Message, MidiFile, MidiTrack

# Root note mapping (C3 = 48 to C4 = 60 as references)
root_notes = {
    'C': 60, 'C#': 61, 'D': 62, 'D#': 63, 'E': 64,
    'F': 65, 'F#': 66, 'G': 67, 'G#': 68, 'A': 69, 'A#': 70, 'B': 71,
    'C-': 48, 'C#-': 49, 'D-': 50, 'D#-': 51, 'E-': 52,
    'F-': 53, 'F#-': 54, 'G-': 55, 'G#-': 56, 'A-': 57, 'A#-': 58, 'B-': 59
}

# Settings
selected_scale_file = "default_cypher.txt"
selected_root_note = 60
note_on_time = 0
note_off_time = 480
MAX_FILENAME_LENGTH = 32

def truncate_filename(filename, extension):
    """
    Truncate filenames to ensure they do not exceed MAX_FILENAME_LENGTH.
    """
    base_length = MAX_FILENAME_LENGTH - len(extension)
    if len(filename) > base_length:
        return filename[:base_length] + "" + extension
    return filename + extension

def load_scale_from_file(filename):
    scale = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                if ':' in line:
                    char, value = line.strip().split(':')
                    scale[char.strip()] = int(value.strip())
        return scale
    except FileNotFoundError:
        print(f"Error: Cypher '{filename}' not found.")
        return {}

def reverse_scale(scale):
    return {v: k for k, v in scale.items()}

def text_to_midi_notes(text, scale, base_root_note=60):
    return [base_root_note + scale[char.upper()] for char in text if char.upper() in scale]

def create_midi_file(notes, filename):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    for note in notes:
        track.append(Message('note_on', note=note, velocity=32, time=note_on_time))
        track.append(Message('note_off', note=note, velocity=32, time=note_off_time))
    mid.save(filename)

def midi_to_text(filename, scale, base_root_note=60):
    reverse_scale_select = reverse_scale(scale)
    try:
        mid = MidiFile(filename)
        decrypted_text = []
        midi_notes = []
        for track in mid.tracks:
            for msg in track:
                if msg.type == 'note_on' and msg.velocity > 0:
                    note = msg.note - base_root_note
                    midi_notes.append(msg.note)
                    if note in reverse_scale_select:
                        decrypted_text.append(reverse_scale_select[note])
        return ''.join(decrypted_text), midi_notes
    except FileNotFoundError:
        print("Error: MIDI file not found.")
        return "", []

def read_text_from_file(filepath):
    """
    Read and return the content of a text file.
    """
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return ""
    except Exception as e:
        print(f"Error reading file '{filepath}': {e}")
        return ""

def generate_random_string(length, scale):
    valid_chars = list(scale.keys())
    return ''.join(random.choice(valid_chars) for _ in range(length))

def update_settings():
    global selected_scale_file, selected_root_note, note_on_time, note_off_time
    while True:
        print("\nSettings:")
        print(f"1. Change Cypher (Current: {selected_scale_file})")
        print(f"2. Change Frequency (Current: {get_root_note_name(selected_root_note)})")
        print(f"3. Change Note-On Time (Current: {note_on_time})")
        print(f"4. Change Note-Off Time (Current: {note_off_time})")
        print("5. Return")
        choice = input("Enter 1, 2, 3, 4, or 5: ").strip()
        if choice == "1":
            file = input("Enter the path to the new cypher: ").strip()
            if load_scale_from_file(file):
                selected_scale_file = file
                print(f"Cypher updated to '{selected_scale_file}'.")
            else:
                print("Invalid Cypher.")
        elif choice == "2":
            print("\nAvailable:")
            print("C, C#, D, D#, E, F, F#, G, G#, A, A#, B (C4)")
            print("C-, C#-, D-, D#-, E-, F-, F#-, G-, G#-, A-, A#-, B- (C3)")
            note = input("Choose a new frequency: ").strip().upper()
            if note in root_notes:
                selected_root_note = root_notes[note]
                print(f"Frequency updated to {note}.")
            else:
                print("Invalid Frequency.")
        elif choice == "3":
            try:
                note_on_time = int(input("Enter the new Note-On time (ticks): ").strip())
                print(f"Note-On time updated to {note_on_time}.")
            except ValueError:
                print("Invalid input.")
        elif choice == "4":
            try:
                note_off_time = int(input("Enter the new Note-Off time (ticks): ").strip())
                print(f"Note-Off time updated to {note_off_time}.")
            except ValueError:
                print("Invalid input.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def get_root_note_name(midi_note):
    for name, note in root_notes.items():
        if note == midi_note:
            return name
    return "Unknown"

def display_current_cypher_and_midi(scale, root_note):
    """
    Display the current cypher map and associated MIDI bindings.
    """
    print("\nCurrent Cypher Map and MIDI Bindings:")
    print(f"Loaded Cypher File: {selected_scale_file}")
    print(f"Frequency: {get_root_note_name(root_note)} ({root_note})")
    print("\nCharacter -> Interval -> MIDI Note")
    for char, interval in scale.items():
        midi_note = root_note + interval
        print(f"{char}: {interval} -> {midi_note}")
    print("-" * 40)

if __name__ == "__main__":
    while True:
        scale = load_scale_from_file(selected_scale_file)

        print("\nDE-CRYPT v3.3:")
        print("1. Generate Randomized MIDI File")
        print("2. Encrypt Text to MIDI")
        print("3. Decrypt MIDI to Text")
        print("4. View Current Cypher Map")
        print("5. Settings")
        print("6. Exit")
        choice = input("Enter 1, 2, 3, 4, 5, or 6: ").strip()

        if choice == "1":
            if not scale:
                continue
            try:
                length = int(input("Enter the length of the random string: ").strip())
                if length <= 0:
                    print("Length must be a positive number.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            random_string = generate_random_string(length, scale)
            print(f"Generated Random String: {random_string}")
            midi_notes = text_to_midi_notes(random_string, scale, selected_root_note)
            print(f"MIDI Notes: {midi_notes}")
            filename = truncate_filename(random_string, ".mid")
            create_midi_file(midi_notes, filename)
            print(f"Randomized MIDI file '{filename}' has been created.")

        elif choice == "2":
            if not scale:
                continue
            print("\n1. Encrypt from a Text File")
            print("2. Encrypt from Direct Input")
            method = input("Enter 1 or 2: ").strip()
            if method == "1":
                file = input("Enter the path to the text file: ").strip()
                text = read_text_from_file(file)
            elif method == "2":
                text = input("Enter the text to encrypt: ").strip()
            else:
                print("Invalid choice. Returning to menu.")
                continue
            midi_notes = text_to_midi_notes(text, scale, selected_root_note)
            print(f"MIDI Notes: {midi_notes}")
            create_midi_file(midi_notes, "output.mid")
            print("Encrypted MIDI file 'output.mid' has been created.")

        elif choice == "3":
            if not scale:
                continue
            file = input("Enter the path to the MIDI file: ").strip()
            if os.path.exists(file):
                decrypted_text, midi_notes = midi_to_text(file, scale, selected_root_note)
                print(f"\nDecrypted Text: {decrypted_text}")
                print(f"MIDI Notes: {midi_notes}")
                if decrypted_text:
                    filename = truncate_filename(decrypted_text[:MAX_FILENAME_LENGTH], ".txt")
                else:
                    filename = "output.txt"
                with open(filename, 'w') as f:
                    f.write(decrypted_text)
                print(f"Decrypted text file '{filename}' has been created.")
            else:
                print(f"Error: MIDI file '{file}' not found.")

        elif choice == "4":
            if scale:
                display_current_cypher_and_midi(scale, selected_root_note)
            else:
                print("No valid cypher loaded.")

        elif choice == "5":
            update_settings()

        elif choice == "6":
            print("Exiting.")
            break

        else:
            print("Invalid choice.")

