import random

def get_int(prompt, default):
    s = input(f"{prompt} [{default}]: ").strip()
    if not s:
        return default
    try:
        v = int(s)
        if v < 1:
            raise ValueError
        return v
    except ValueError:
        print("Invalid input, using default.")
        return default

def roll_dice(num_dice, sides):
    return [random.randint(1, sides) for _ in range(num_dice)]

def main():
    print("Dice Roller Simulator")
    while True:
        num_dice = get_int("How many dice to roll?", 1)
        sides = get_int("How many sides per die?", 6)

        rolls = roll_dice(num_dice, sides)
        total = sum(rolls)
        print(f"\nYou rolled: {' '.join(str(r) for r in rolls)}  (Sum = {total})")

        again = input("Roll again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
