"""Creating a tea party organizer using subprograms, functions, and main functions. """

__author__: str = "730809199"


def main_planner(guests: int) -> None:
    """Determine tea bag and treat amounts and overall costs from guest number."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: "
        + "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


# Here I went through a few issues, initially it was that I didn't convert the data types to str.
# Next I had the issue where when I added a function into the string, I didn't add parameters of people-guests
# I then had an issue with the cost line, but by adding a call to the tea_bags and treats function I was able to fix it
# Lastly I had a small, simple fix issue of spacing with my dollar sign. By fixing spacing within the string concatenation I fixed the issue.


def tea_bags(people: int) -> int:
    """Find number of people attending party and get amount of tea bags needed."""
    return people * 2


def treats(people: int) -> int:
    """Utilize number of tea bags to find number of treats"""
    return int(1.5 * tea_bags(people=people))


# The switch to int is something I didn't recognize as first since 1.5 is a float
# Calling tea bags helps in case tea bag amount changes, we only have to change one line of code
# calling people=people was a challenge I encountered so I looked back in our class notes.


def cost(tea_count: int, treat_count: int) -> float:
    """Caclulate cost of$0.50 tea bags and $0.75 treats."""
    return (0.50 * tea_count) + (0.75 * treat_count)


# I think i struggled a lot with this function because I assumed we had to call the last functions into it, not realizing it was a seperate input.
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
