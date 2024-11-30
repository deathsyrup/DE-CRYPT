import random
import os
from mido import Message, MidiFile, MidiTrack

def generate_root_notes():
    """
    Generate a dictionary of MIDI note numbers (0-127) mapped to note names with octave suffixes.
    """
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    root_notes = {}
    for midi_note in range(128):
        octave = midi_note // 12 - 1  # MIDI note 0 is C-1
        note_name = note_names[midi_note % 12]
        root_notes[f"{note_name}{octave}"] = midi_note
    return root_notes

# Generate root notes dynamically
root_notes = generate_root_notes()

# Settings
selected_scale_file = "default_cypher.txt"
selected_root_note = 60
note_on_time = 0
note_off_time = 480
MAX_FILENAME_LENGTH = 32

def truncate_filename(filename, extension):
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

def create_cypher_from_midi(midi_file, output_cypher_file):
    try:
        mid = MidiFile(midi_file)
        midi_notes = set()
        for track in mid.tracks:
            for msg in track:
                if msg.type == 'note_on' and msg.velocity > 0:
                    midi_notes.add(msg.note)
        
        midi_notes = sorted(midi_notes)
        
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        cypher_map = {}
        for i, note in enumerate(midi_notes):
            if i < len(alphabet):  
                cypher_map[alphabet[i]] = note
            else:
                break

        with open(output_cypher_file, 'w') as file:
            for char, note in cypher_map.items():
                file.write(f"{char}: {note}\n")

        print(f"Cypher created successfully and saved to '{output_cypher_file}'.")
    except FileNotFoundError:
        print(f"Error: MIDI file '{midi_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

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
        print(f"2. Change Root Note (Current: {get_root_note_name(selected_root_note)})")
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
            print("\nAvailable Notes (0-127):")
            print(", ".join(root_notes.keys()))
            note = input("Choose a new root note (e.g., C4): ").strip().upper()
            if note in root_notes:
                selected_root_note = root_notes[note]
                print(f"Root note updated to {note} ({selected_root_note}).")
            else:
                print("Invalid root note. Please select from the available options.")
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

if __name__ == "__main__":
    while True:
        scale = load_scale_from_file(selected_scale_file)

        print("\nDE-CRYPT IV:")
        print("1. Generate Randomized MIDI File")
        print("2. Encrypt Text to MIDI")
        print("3. Decrypt MIDI to Text")
        print("4. View Current Cypher Map")
        print("5. Create Cypher from MIDI")
        print("6. Settings")
        print("7. Exit")
        choice = input("Enter 1, 2, 3, 4, 5, 6, or 7: ").strip()

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
            print(f"MIDI file '{filename}' has been created.")

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
                print("Invalid choice.")
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
                print("\nCurrent Cypher Map and MIDI Bindings:")
                print(f"Loaded Cypher File: {selected_scale_file}")
                print(f"Frequency: {get_root_note_name(selected_root_note)} ({selected_root_note})")
                print("\nCharacter -> Interval -> MIDI Note")
                for char, interval in scale.items():
                    midi_note = selected_root_note + interval
                    print(f"{char}: {interval} -> {midi_note}")
                print("-" * 40)
            else:
                print("No valid cypher loaded.")

        elif choice == "5":
            midi_file = input("Enter the path to the MIDI file: ").strip()
            output_file = input("Enter the path for the new cypher text file: ").strip()
            create_cypher_from_midi(midi_file, output_file)

        elif choice == "6":
            update_settings()

        elif choice == "7":
            print("Exiting.")
            break

        else:
            print("Invalid choice.")
