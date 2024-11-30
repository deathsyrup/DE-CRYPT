import os
import random
from mido import Message, MidiFile, MidiTrack

class CypherHandler:
    def __init__(self, filename="default_cypher.txt", base_root_note=60):
        self.filename = filename
        self.base_root_note = base_root_note
        self.scale = self.load_scale_from_file()

    def load_scale_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                scale = {
                    char.strip(): int(value.strip())
                    for line in file if ':' in line
                    for char, value in [line.split(':', 1)]
                }
                print(f"Cypher loaded successfully from '{self.filename}'.")
                return scale
        except FileNotFoundError:
            print(f"Error: Cypher file '{self.filename}' not found.")
            return {}
        except ValueError as e:
            print(f"Error in cypher file format: {e}")
            return {}

    def reverse_scale(self):
        return {v: k for k, v in self.scale.items()}


class MIDIHandler:
    def __init__(self, base_root_note=60, note_on_time=0, note_off_time=480):
        self.base_root_note = base_root_note
        self.note_on_time = note_on_time
        self.note_off_time = note_off_time

    def text_to_midi_notes(self, text, scale):
        return [self.base_root_note + scale[char.upper()] for char in text if char.upper() in scale]

    def midi_to_text(self, filename, scale):
        reverse_scale = {v: k for k, v in scale.items()}
        try:
            mid = MidiFile(filename)
            decrypted_text = []
            midi_notes = []
            for track in mid.tracks:
                for msg in track:
                    if msg.type == 'note_on' and msg.velocity > 0:
                        note = msg.note - self.base_root_note
                        midi_notes.append(msg.note)
                        if note in reverse_scale:
                            decrypted_text.append(reverse_scale[note])
            return ''.join(decrypted_text), midi_notes
        except FileNotFoundError:
            print(f"Error: MIDI file '{filename}' not found.")
            return "", []

    def create_midi_file(self, notes, filename):
        try:
            mid = MidiFile()
            track = MidiTrack()
            mid.tracks.append(track)
            for note in notes:
                track.append(Message('note_on', note=note, velocity=32, time=self.note_on_time))
                track.append(Message('note_off', note=note, velocity=32, time=self.note_off_time))
            mid.save(filename)
        except Exception as e:
            print(f"Error creating MIDI file '{filename}': {e}")

    def create_cypher_from_midi(self, midi_file, output_cypher_file):
        try:
            mid = MidiFile(midi_file)
            midi_notes = {msg.note for track in mid.tracks for msg in track if msg.type == 'note_on' and msg.velocity > 0}
            midi_notes = sorted(midi_notes)

            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            cypher_map = {alphabet[i]: note for i, note in enumerate(midi_notes) if i < len(alphabet)}

            with open(output_cypher_file, 'w') as file:
                for char, note in cypher_map.items():
                    file.write(f"{char}: {note}\n")

            print(f"Cypher created and saved to '{output_cypher_file}'.")
        except FileNotFoundError:
            print(f"Error: MIDI file '{midi_file}' not found.")
        except Exception as e:
            print(f"Error creating cypher: {e}")


class Utils:
    MAX_FILENAME_LENGTH = 32

    @staticmethod
    def truncate_filename(filename, extension):
        base_length = Utils.MAX_FILENAME_LENGTH - len(extension)
        return (filename[:base_length] if len(filename) > base_length else filename) + extension

    @staticmethod
    def generate_random_string(length, valid_chars):
        return ''.join(random.choice(valid_chars) for _ in range(length))

    @staticmethod
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


def generate_root_notes():
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    root_notes = {}
    for midi_note in range(128):
        octave = midi_note // 12 - 1
        note_name = note_names[midi_note % 12]
        root_notes[f"{note_name}{octave}"] = midi_note
    return root_notes


def settings_menu(cypher_handler, midi_handler, root_notes):
    while True:
        print("\nSettings:")
        print("1. View Current Cypher Map")
        print("2. Create Cypher from MIDI")
        print(f"3. Change Cypher File (Current: {cypher_handler.filename})")
        print(f"4. Change Root Note (Current: {cypher_handler.base_root_note})")
        print(f"5. Change Note-On Time (Current: {midi_handler.note_on_time})")
        print(f"6. Change Note-Off Time (Current: {midi_handler.note_off_time})")
        print("7. Return")
        setting_choice = input("Enter your choice: ").strip()

        if setting_choice == "1":
            print("\nCurrent Cypher Map:")
            for char, interval in cypher_handler.scale.items():
                midi_note = cypher_handler.base_root_note + interval
                print(f"{char}: {interval} -> {midi_note}")
        elif setting_choice == "2":
            midi_file = input("Enter the MIDI file path: ").strip()
            output_file = input("Enter output cypher file path: ").strip()
            midi_handler.create_cypher_from_midi(midi_file, output_file)
        elif setting_choice == "3":
            filename = input("Enter new cypher file path: ").strip()
            cypher_handler.filename = filename
            cypher_handler.scale = cypher_handler.load_scale_from_file()
        elif setting_choice == "4":
            print("\nAvailable Root Notes:")
            for name, note in root_notes.items():
                print(f"{name} (MIDI: {note})")
            user_input = input("Enter a root note name (e.g., C4) or MIDI number (0-127): ").strip()
            if user_input.isdigit():
                midi_number = int(user_input)
                if 0 <= midi_number < 128:
                    cypher_handler.base_root_note = midi_number
                    print(f"Root note set to MIDI {midi_number}.")
                else:
                    print("Invalid MIDI number. Must be between 0 and 127.")
            elif user_input.upper() in root_notes:
                cypher_handler.base_root_note = root_notes[user_input.upper()]
                print(f"Root note set to {user_input.upper()}.")
            else:
                print("Invalid root note.")
        elif setting_choice == "5":
            midi_handler.note_on_time = int(input("Enter new Note-On time: ").strip())
        elif setting_choice == "6":
            midi_handler.note_off_time = int(input("Enter new Note-Off time: ").strip())
        elif setting_choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    root_notes = generate_root_notes()
    cypher_handler = CypherHandler()
    midi_handler = MIDIHandler()

    while True:
        print("\nDE-CRYPT IV:")
        print("1. Generate Randomized MIDI File")
        print("2. Encrypt Text to MIDI")
        print("3. Decrypt MIDI to Text")
        print("4. Settings")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            if not cypher_handler.scale:
                print("No cypher loaded. Please load a cypher first.")
                continue

            print("\n1. Generate a completely random string")
            print("2. Input a custom message to embed")
            sub_choice = input("Enter your choice (1 or 2): ").strip()

            if sub_choice == "1":
                length = int(input("Enter the length of the random string: "))
                valid_chars = list(cypher_handler.scale.keys())
                random_string = Utils.generate_random_string(length, valid_chars)
            elif sub_choice == "2":
                length = int(input("Enter the total length of the string: "))
                message = input("Enter the message to embed: ").strip()
                if len(message) > length:
                    print("Error: The message is longer than the total string length.")
                    continue

                padding_length = length - len(message)
                left_padding = random.randint(0, padding_length)
                right_padding = padding_length - left_padding

                valid_chars = list(cypher_handler.scale.keys())
                left_padding_str = Utils.generate_random_string(left_padding, valid_chars)
                right_padding_str = Utils.generate_random_string(right_padding, valid_chars)

                random_string = f"{left_padding_str}{message}{right_padding_str}"
            else:
                print("Invalid choice.")
                continue

            midi_notes = midi_handler.text_to_midi_notes(random_string, cypher_handler.scale)
            filename = Utils.truncate_filename("generated", ".mid")
            midi_handler.create_midi_file(midi_notes, filename)
            print(f"MIDI file '{filename}' created.")
            print(f"Generated String: {random_string}")
            print(f"Corresponding MIDI Notes: {midi_notes}")

        elif choice == "2":
            if not cypher_handler.scale:
                print("No cypher loaded. Please load a cypher first.")
                continue
            print("\n1. Encrypt from a Text File")
            print("2. Encrypt from Direct Input")
            method = input("Enter 1 or 2: ").strip()
            if method == "1":
                filepath = input("Enter the path to the text file: ").strip()
                text = Utils.read_text_from_file(filepath)
            elif method == "2":
                text = input("Enter the text to encrypt: ").strip()
            else:
                print("Invalid choice.")
                continue
            midi_notes = midi_handler.text_to_midi_notes(text, cypher_handler.scale)
            filename = Utils.truncate_filename("output", ".mid")
            midi_handler.create_midi_file(midi_notes, filename)
            print(f"MIDI file '{filename}' created.")
            print(f"Input Text: {text}")
            print(f"Corresponding MIDI Notes: {midi_notes}")

        elif choice == "3":
            file = input("Enter the MIDI file path: ").strip()
            decrypted_text, midi_notes = midi_handler.midi_to_text(file, cypher_handler.scale)
            if decrypted_text:
                truncated_text = decrypted_text[:Utils.MAX_FILENAME_LENGTH]
                output_filename = Utils.truncate_filename(truncated_text, ".txt")
                with open(output_filename, 'w') as file:
                    file.write(decrypted_text)
                print(f"Decrypted Text: {decrypted_text}")
                print(f"Corresponding MIDI Notes: {midi_notes}")
                print(f"Decrypted text saved to file: {output_filename}")
            else:
                print("Decrypted text is empty or invalid.")

        elif choice == "4":
            settings_menu(cypher_handler, midi_handler, root_notes)

        elif choice == "5":
            print("Exiting.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
