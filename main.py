from time import sleep

from converter import Converter

def typing_print(text: str) -> None:
    """Prints the text to console with a typing effect."""
    for char in text:
        print(char, end="", flush=True)
        sleep(0.1)
    print("\n")

if __name__ == "__main__":
    converter = Converter()
    user_input = ""
    while len(user_input) < 1:
        user_input = input("Please provide the text you would like to convert: ")

    words = user_input.split(" ")
    print("Converted text is displayed below!")
    print(
        "(Letters in the same word is seperated by 3 spaces and words are seperated by new line)"
    )
    for word in words:
        converted_word = converter.convert_text(word)
        typing_print(converted_word)
