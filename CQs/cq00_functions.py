"""My first challenge question in COMP110!"""

__author__ = "730763375"

def mimic(message: str) -> str:
    """To repeat the same phrase"""
    return message


def main() -> None:
    """Starting point of a program"""
    print(mimic(message=input("What is your message?")))

if __name__ == "__main__":
	  main()