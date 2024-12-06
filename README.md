## DE-CRYPT 4.7

DE-CRYPT 4.7 converts text to MIDI notes and back using customizable cypher mappings. It offers encryption, decryption, randomized MIDI generation, and dynamic configuration.

## FEATURES

Customizable Cypher Maps

    Map characters to MIDI notes using pre-defined mappings or generate them from MIDI files.
    Save and load cypher maps for reuse and consistency.

Vigenère Cypher Integration

    Add an extra layer of encryption with Vigenère cypher.
    Manage and update keywords dynamically via a keyword.txt file.

Text Encryption and Decryption

    Encrypt text into MIDI files or decrypt MIDI files back into text.
    Ensures sequential file naming to prevent overwrites.

Advanced MIDI Functionality

    Random MIDI Generation:
        Create random text strings or embed custom messages with adjustable padding.
        Export as MIDI files.
    Keyword MIDI File Generation:
        Generate MIDI files based on the current Vigenère cypher keyword for easy reference.

Settings and Configuration

    Dynamic Root Note Selection:
        Choose any MIDI note (0-127) as the root note (e.g., C4, A#3).
    Adjustable MIDI Timings:
        Customize "note-on" and "note-off" durations for tailored playback.
    Unified Alphabet Management:
        Set and reset the alphabet dynamically to support additional characters and custom needs.

## MENU OPTIONS

    Generate Randomized MIDI File
        Create a random text string or embed a message.
        Convert the result to MIDI using the active cypher map.
        Save the output and display the plaintext and MIDI notes.

    Encrypt Text to MIDI
        Encrypt input text (via direct input or file) into a MIDI file.
        Optionally apply the Vigenère cypher for enhanced security.
        View plaintext, cyphertext, and MIDI note mappings.

    Decrypt MIDI to Text
        Decrypt MIDI files into plaintext (direct input or file).
        Apply reverse Vigenère cypher if a keyword is set.
        Save decrypted text to a file.

    Settings
        Access configuration options for cypher files, keywords, MIDI timings, and more.

    Exit
        Quit the program.

## SETTINGS OPTIONS

    Change Library
        View the current library and optionally update it with a custom set of characters.

    Change Root Note
        Select a new root note using any MIDI note (0-127).

    Change Cypher File
        Load a new cypher file to update character-to-MIDI mappings.

    Set Vigenère Cypher Keyword
        Define or update the keyword for Vigenère cypher encryption.
        Automatically syncs with the keyword.txt file.

    Create Cypher from MIDI
        Generate a cypher map by mapping unique MIDI notes from a file to the character list.
        Save the generated map for reuse.

    Generate Keyword MIDI File
        Create a MIDI file representing the Vigenère cypher keyword.

    Change Note-On Time
        Adjust the "note-on" duration for MIDI playback.

    Change Note-Off Time
        Adjust the "note-off" duration for MIDI playback.

    View Current Cypher Map
        Display the current cypher map, root note, and character-to-MIDI mappings.

## Installation

    Prerequisites:
        Python 3.8 or higher is required.

    Install Dependencies:
        Run: pip install mido