"""Planning out amount of items and cost for a giant, cozy party"""

__author__ : str = "730763375"


def main_planner(guests:int) -> None:
    """Bringing all the functions together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(guests*2))
    print("Treats: " + str(int((tea_bags(guests))*1.5)))
    print("Cost: $" + str(0.5 * (guests*2)+ 0.75 *(tea_bags(guests))*1.5))
# It was challenging for me with the main_planner function as it took me a while to format the string literals to get to the desired outputs 
# I first tried to concatenate every word and add them up, but there was no space and the guests won't return an int
# I then combined the words into a str and add it to the guests function, but you cannot add a str and an int
# So I decided to leave space between the quotation marks and turn the value of guests into str using the str() and got the desired results
# I did the same for the rest, leaving some space inbetween quotation marks, calling the defined functions, and adding them as str

def tea_bags(people:int) -> int:
    """Number of tea bags per guest"""
    return people * 2


def treats(people:int) -> int:
    """Number of treats per tea bag"""
    return(int((tea_bags(people)) * 1.5))


def cost(tea_count:int, treat_count:int) -> float:
    """Total cost of tea bags and treats"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
        main_planner(guests=int(input("How many guests are attending your tea party? ")))
        