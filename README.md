# DE-CRYPT_4.4.4

DE-CRYPT 4.4.4

    - DE-CRYPT 4.4.4 converts text to MIDI notes and back using customizable cypher mappings, 
      allowing encryption, decryption, random MIDI generation, and dynamic settings adjustment. -

## Features

    Customizable Cypher Maps:
        Map alphabetic characters to MIDI notes using existing MIDI files or pre-defined mappings.
        Save and load cypher files for reuse.

    Vigenère Cypher Integration:
        Enhance security with optional Vigenère cypher encryption.
        Manage keywords via a keyword.txt file, with automatic updates.

    Text Encryption and Decryption:
        Encrypt text into MIDI files or decrypt MIDI files back into text.
        Sequential naming ensures no files are accidentally overwritten.

Advanced MIDI Functionality:

    Generate Randomized MIDI Files:
        Create random text strings or embed custom messages with adjustable padding.
        Save the result as a MIDI file.

    Keyword MIDI File:
        Generate a MIDI file based on the current Vigenère cypher keyword for reference.

Settings and Configuration:

    Dynamic Root Note Selection:
        Choose any MIDI note (0-127) as the root note (e.g., C4, A#3).

    Adjustable MIDI Timings:
        Customize MIDI note-on and note-off durations.

## Menu Options

    Generate Randomized MIDI File:
        Create a random text string or embed a message with padding.
        Encrypt the result to MIDI using the cypher map and save it.
        Displays the plaintext and corresponding MIDI notes.

    Encrypt Text to MIDI:
        Encrypt input text (via file or direct input) into MIDI file.
        Optionally apply the Vigenère cypher for added security.
        Displays the plaintext, cyphertext, and corresponding MIDI notes.

    Decrypt Text:
        Decrypt input text (via file or direct input) into a .txt file.
        Apply reverse Vigenère cypher if a keyword is set.
        Save the decrypted plaintext to a sequential .txt file.

    Settings:
        Configure cypher files, keywords, MIDI timings, and more.

    Exit:
        Quit the program.

## Settings

    View Current Cypher Map:
        Display the current cypher file, root note, and character-to-MIDI mappings.

    Change Root Note:
        Update the root note using any MIDI note (0-127).

    Change Cypher File:
        Load a new cypher file to update the character-to-MIDI mapping.

    Set Vigenère Cypher Keyword:
        Update the keyword for Vigenère cypher encryption.
        Automatically updates the keyword.txt file.

    Create Cypher from MIDI:
        Generate a cypher mapping from a MIDI file.
        Map unique MIDI notes to the alphabet (A-Z) and save the result.

    Generate Keyword MIDI File:
        Create a MIDI file based on the Vigenère cypher keyword.

    Change Note-On Time:
        Adjust the duration of MIDI "note-on" events.

    Change Note-Off Time:
        Adjust the duration of MIDI "note-off" events.

    Return to Main Menu:
        Exit the settings menu and return to the main program.

## Installation
	
	Prerequisites:
		Install Python 3.8 or higher.
		Install required dependencies:
			pip install mido

## Credits

Written by deathsyrup  
https://1deathsyrup.bandcamp.com/  
https://www.twitch.tv/1deathsyrup/
