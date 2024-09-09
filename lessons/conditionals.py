"""Practicing my conditionals."""


def less_than_10(num: int) -> None:
    """Tell us if num < 10."""
    if num < 10: # check if this is true
        print("Small number!")  #Then Block
    else:
        print("Big number!")
    print("This is the end of the function!")

def wake_up(alarm:bool) -> bool:
    """Return a message based on if alarm is going off. """
    if alarm is True:
        return "Wake up! Go to Comp 110!"
    else:
        return "Keep sleeping. You deserve it. :"
    

def check_first_letter(word: str, letter: str) -> str:
        """Checking if the first character of a word is a letter"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match"

