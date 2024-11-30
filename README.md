# DE-CRYPT_IV

DE-CRYPT IV

    - DE-CRYPT IV converts text to MIDI notes and back using customizable cypher mappings, 
      allowing encryption, decryption, random MIDI generation, and dynamic settings adjustment. -

## Features

- **Generate Randomized MIDI Files**:
  - Create a MIDI file based on a random string generated using the loaded cypher map.
  - Optionally embed a custom message within the random string.
  - Displays the generated string and its corresponding MIDI notes.

- **Encrypt Text to MIDI**:
  - Converts input text into MIDI notes using the cypher map and saves them as a MIDI file.
  - Displays the text and the corresponding MIDI notes.

- **Decrypt MIDI to Text**:
  - Converts a MIDI file back into text using the reverse of the loaded cypher map.
  - Displays the decrypted text and corresponding MIDI notes.
  - Saves the decrypted text as a `.txt` file named after the text content.

- **View Current Cypher Map**:
  - Displays the active cypher file, root note, and the character-to-MIDI mappings.

- **Create Cypher from MIDI**:
  - Generates a new cypher mapping from a MIDI file by sequentially assigning MIDI notes to the alphabet (A-Z).
  - Saves the new cypher as a `.txt` file.

- **Dynamic Root Note Selection**:
  - Choose any MIDI note (0-127) as the root note, with full naming support for octaves (e.g., `C4`, `A#3`).

- **Adjust Settings**:
  - Change the cypher file, root note (frequency), or MIDI note timing.

## Menu Options

1. **Generate Randomized MIDI File**:
    - Prompts for the length of the string.
    - Offers the option to:
      - Generate a fully random string.
      - Embed a custom message within the random string.
    - Converts the string into MIDI notes based on the root note and cypher intervals.
    - Saves the result as a `.mid` file.
    - Displays the generated string and corresponding MIDI notes.

2. **Encrypt Text to MIDI**:
    - Prompts for text input (directly or from a text file).
    - Converts the text into MIDI notes using the cypher map and root note.
    - Saves the result as `output.mid`.
    - Displays the input text and the corresponding MIDI notes.

3. **Decrypt MIDI to Text**:
    - Prompts for the path to a MIDI file.
    - Converts MIDI notes into text using the reverse cypher map.
    - Displays the decrypted text and corresponding MIDI notes.
    - Saves the decrypted text as a `.txt` file with a filename derived from the decrypted content.

4. **Settings**:
    - Allows dynamic adjustment of key settings:
      - **View Current Cypher Map**:
        - Displays the loaded cypher file name, active root note, and character-to-MIDI mappings.
      - **Create Cypher from MIDI**:
        - Prompts for a MIDI file and output filename.
        - Extracts unique MIDI notes and maps them to the alphabet (A-Z).
        - Saves the resulting cypher as a `.txt` file.
      - **Change Cypher File**:
        - Loads a new cypher file (`.txt` format required).
      - **Change Root Note**:
        - Update the root note using any MIDI note (0-127, e.g., `C4`, `A#3`).
      - **Adjust MIDI Timings**:
        - Modify MIDI note-on and note-off timings (in ticks).
      - **Return to Main Menu**:
        - Exit the settings menu and return to the main program.

5. **Exit**:
    - Exits the program.

## Updates and Enhancements

- **Embed Custom Messages**:
  - Generate a randomized string and embed a readable message within it.

- **Unified Outputs**:
  - Displays generated strings, decrypted text, and their corresponding MIDI notes.

- **Decrypted Text Saved**:
  - Automatically saves the decrypted text to a `.txt` file with a filename derived from the text.

- **Improved Random String Handling**:
  - Fixed issues with subscripting keys for random string generation.

## Credits

Written by deathsyrup  
https://1deathsyrup.bandcamp.com/  
https://www.twitch.tv/1deathsyrup/
