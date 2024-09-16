"""EX02 - Chardle - A cute step toward Wordle."""
	 
__author__ = "730763375"


def input_word() -> str:
    """Using a word as the input"""
    # I spent time trying to figure out how to let the function recognize the input must be exactly 5 characters
    # I know I had to use len function to set the length of the word from input and set equal to 5, otherwise it will print error
    five_character_word: str = input("Enter a 5-character word: ")
    if len(five_character_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return five_character_word


def input_letter() -> str:
    """Using a letter for the output"""
    single_character: str = input("Enter a single character: ")
    if len(single_character) != 1:
        print("Error: Character must be a single character.")
        exit()
    return single_character



def contains_char(word:str, letter:str) -> None:
    """Checking if the indices of the word str matches with the character str"""
    # Figuring out how to make the outputs appear exactly as the one in the assginment was challenging
    # First, I used if then and else statments, and indexed each letter of the word so see if they match the letter given
    # Also printed out where letter was indexed
    # However, when I tried to count the instances in which the letter was found in the word, it only produced 1 instance at max if there was 1 or more matches
    # I knew this is because of the if then and else statements, so it took me some time to figure out that using only the if then statements would suffice
    # I then used not equal statements to produce "No instances of a letter is found in word" when count = 0
    # These codes finally produced the outputs for the program of the chardle game
    print("Searching for " + letter + " in " + word )
    count: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    if count ==1:
        print(str(count) + " instance of " + letter + " found in " + word)
    if count != 0 and count !=1:
        print(str(count) + " instances of " + letter + " found in " + word)
    



def main() -> None:
    """Handles all function calls"""
    print(contains_char(word=input_word(), letter=input_letter()))


if __name__ == "__main__":
    main()
