# text-to-morse
A simple command line tool to convert text to morse code

## Installation

1. Clone the repo:
    ```bash
    git clone https://github.com/Ashish-Krishna-K/text-to-morse.git
    cd text-to-morse
    ```
1. Run the script:
    ```bash
    python main.py
    ```

## Usage

1. Run the script by executing 'main.py'.
1. Enter the text you want to convert when prompted.
1. The converted text will be displayed with a typing effect.

## Features

- Converts text to Morse code with a typing effect for user interaction.
- Supports letters, numbers, and spaces.

## Structure
- **main.py**: Contains the main script for user interaction.
- **converter.py**: Defines the Converter class for handling the conversion of text to Morse code.
- **test_converter.py**: Includes unit tests for the Converter class.

## Example

```bash
Please provide the text you would like to convert: Hello World

Converted text is displayed below!
(Each letter is separated by 3 spaces and words are separated by a new line)
....   .   .-..   .-..   ---     .--   ---   .-.   .-..   -..
```

## Running Tests
Run the unit tests using:
```bash
python test_converter.py
```

## Dependencies
The script uses only standard Python libraries.


