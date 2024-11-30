# DE-CRYPT_IV

DE-CRYPT IV    

    -DE-CRYPT IV converts text to MIDI notes and back using customizable cypher mappings, 
     allowing encryption, decryption, random MIDI generation, and dynamic settings adjustment.-

## Features

- **Generate Randomized MIDI Files**:
    - Creates a MIDI file based on a random string generated using the loaded cypher map.
- **Encrypt Text to MIDI**:
    - Converts input text into MIDI notes using the cypher map and saves them as a MIDI file.
- **Decrypt MIDI to Text**:
    - Converts a MIDI file back into text using the reverse of the loaded cypher map.
- **View Current Cypher Map**:
    - Displays the active cypher file, root note, and the character-to-MIDI mappings.
- **Create Cypher from MIDI**:
    - Generates a new cypher mapping from a MIDI file by sequentially assigning MIDI notes to the alphabet (A-Z) and saves it as a new cypher text file.
- **Dynamic Root Note Selection**:
    - Choose any MIDI note (0-127) as the root note, with full naming support for octaves (e.g., `C4`, `A#3`).
- **Adjust Settings**:
    - Change the cypher file, root note (frequency), or MIDI note timing.

## Menu Options

- **Generate Randomized MIDI File**:
    - Prompts for the length of the random string.
    - Generates a string using characters from the loaded cypher file.
    - Converts the string into MIDI notes based on the root note and cypher intervals.
    - Saves the output as a `.mid` file.

- **Encrypt Text to MIDI**:
    - Prompts for text input (directly or from a text file).
    - Converts the text into MIDI notes based on the cypher map and root note.
    - Saves the output as `output.mid`.

- **Decrypt MIDI to Text**:
    - Prompts for the path to a MIDI file.
    - Converts MIDI notes into text using the reverse cypher map.
    - Displays the text and saves it as a `.txt` file with a truncated name based on the decrypted content.

- **View Current Cypher Map**:
    - Displays the loaded cypher file name.
    - Shows the active root note.
    - Lists the character-to-interval and MIDI note mappings.

- **Create Cypher from MIDI**:
    - Prompts for the path to a MIDI file and an output file name.
    - Extracts unique MIDI notes and maps them sequentially to the alphabet (A-Z).
    - Saves the resulting cypher as a `.txt` file.

- **Settings**:
    - Change the cypher file (`.txt` format required).
    - Update the root note (full MIDI range 0-127, e.g., `C4`, `A#3`).
    - Adjust MIDI note-on and note-off timings (in ticks).

- **Exit**:
    - Exits the program.
		
## Credits

    Written by deathsyrup
        https://1deathsyrup.bandcamp.com/
        https://www.twitch.tv/1deathsyrup/
