class Converter:
    """Class for handling the conversion of text to morse code"""

    __reference = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": "/",
    }

    def convert_text(self, word: str) -> str:
        """
        Converts the given word into morse code
        {params} text: the word in English, this function expects only one word to be passed
        in instead of an entire line.
        {returns} The morse code version of the inputted word
        """
        morse_code = [self.__reference[char.upper()] for char in word if char.isalnum()]
        return "   ".join(morse_code)
