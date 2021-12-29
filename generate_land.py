import random
from noise import pnoise2
from termcolor import colored


def generate_land(cols=10, rows=20, noise_level=10):
    seed = random.randint(0, 100)
    data = [
        "🏔",
        "🌲",
        "🌲",
        "🏡",
        "🌲",
        "🌾",
        "🌴",
        "🌴",
        "🌴",
        "🏖",
        "🌊",
        "🌊",
        "🌊",
        "🌊",
        "🏖",
        "🌴",
        "🌴",
        "🌴",
        "🏢",
        "🌲",
        "🌲",
        "🌲",
    ]
    land = ""

    print(f"Generate a landscape which is {cols} by {rows}")

    for row in range(rows):
        for col in range(cols):
            n = pnoise2(row / rows, col / cols, base=seed, octaves=5)
            n *= noise_level
            n = round(n)
            n = n % len(data)
            land += data[n]
        land += "\n"

    print("Finished generating a landscape")
    return land


def ask_for_number(question):
    tries = 0

    while tries < 3:
        answer = input(question)
        if answer.isnumeric():
            return int(answer)
        else:
            print(colored("Invalid answer", "red"))
            tries += 1
    quit()


if __name__ == "__main__":
    cols = ask_for_number(colored("Enter number of cols: ", "green"))
    rows = ask_for_number(colored("Enter number of rows: ", "green"))

    output = generate_land(cols, rows)
    print(output)
