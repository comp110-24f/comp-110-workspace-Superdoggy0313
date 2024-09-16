"""Planning out amount of items and cost for a giant, cozy party"""

__author__ : str = "730763375"


def main_planner(guests:int) -> None:
    """Bringing all the functions together"""
    print("A " + "Cozy " + "Tea " + "Party " +  "for " + str(guests) + " People!")
    print("Tea " + "Bags: " + str(tea_bags(people = guests)))
    print("Treats: " + str(treats(people = guests)))
    print("Cost: " +  "$" +str(cost(tea_count = tea_bags(people=guests), treat_count= treats(people=guests))))
# It was challenging for me with the main_planner function as it took me a while to format the string literals to get to the desired outputs 
# I first tried to concatenate every word and add them up, but there was no space inbetween the words and the guests won't return an int
# I then removed the quotation marks from guests, but a str and an int cannot be added together
# So I decided to leave space between the quotation marks and turn the value of guests into str using the str() and got the desired results
# I did the same for the rest, leaving some space inbetween quotation marks, calling the defined functions, and adding them as str

def tea_bags(people:int) -> int:
    """Number of tea bags per guest"""
    return people * 2


def treats(people:int) -> int:
    """Number of treats per tea bag"""
    return(int((tea_bags(people = people)) * 1.5))


def cost(tea_count:int, treat_count:int) -> float:
    """Total cost of tea bags and treats"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
        main_planner(guests=int(input("How many guests are attending your tea party? ")))
        