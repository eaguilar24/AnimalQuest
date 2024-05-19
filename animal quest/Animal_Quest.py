import random

# Function to read riddles from a text file, creating empty list, loops and splits lines into sections, adds sections as tuple to list
def load_riddles(file_name):
    riddles = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            section = line.strip().split('-')
            riddle = section[0]
            answer = section[1]
            food_choices = section[2:]
            riddles.append((riddle, answer, food_choices))
    return riddles

# Function to display game introduction and instructions
def display_intro():
    print("Welcome to the Animal Quest Game!\n"
          "You will encounter various animals that will give you riddles to solve.\n"
          "If you guess the animal correctly, you must then offer it the correct food to \n"
          "to join you. If you guess the animal incorrectly, you will lose a point.\n"
          "You start with 2 points per level, and the game ends if you reach 0 points.\n"
          "You have a maximum of 2 guesses for both the riddle and the food.\n"
          "Good luck!\n")

# Function to display level introduction
def display_level_intro(level):
    print(f"Level {level} - Happy collecting!\n")
    print("Solve the riddles and offer the correct food to the animals.\n")

# Function to play games levels, empty list for animals, tracks points and guesses, displays random riddle
def play_level(level, riddles):
    points = 2
    animals = []

    display_level_intro(level)

    while points > 0 and riddles:
        riddle, answer, food_choices = random.choice(riddles)
        print(f"Riddle: {riddle}")
        riddle_guesses = 0

        while riddle_guesses < 2:
            user_answer = input("Your guess: ").strip().lower()
            if user_answer == answer.lower():
                print("Correct! Now offer the correct food to persuade the animal.")
                food_guesses = 0

                while food_guesses < 2:
                    user_food = input("Offer food: ").strip().lower()
                    if user_food in [food.lower() for food in food_choices]:
                        print(f"The {answer} is pleased and joins you on your journey.\n")
                        animals.append(answer)
                        riddles.remove((riddle, answer, food_choices))
                        break
                    else:
                        food_guesses += 1
                        if food_guesses < 2:
                            print("Incorrect food! Try again.")
                        else:
                            print(f"Incorrect food! The {answer} refuses to join you.\n")
                break
            else:
                riddle_guesses += 1
                if riddle_guesses < 2:
                    print("Incorrect! Try again.")
                else:
                    print(f"Incorrect! You lose a point. Points remaining: {points - 1}\n")
                    points -= 1
                    break
        if riddle_guesses == 2 or food_guesses == 2:
            riddles.remove((riddle, answer, food_choices))  # Remove the animal if player has guessed incorrectly twice
       
        if not riddles:
            print(f"Congratulations! You have completed Level {level}.\n")
    
    return points, animals

# Function for gameplay mechanics, levels, intro, animal list, level loops, game endings
def main():
    display_intro()

    levels = 3
    all_animals = []

    for level in range(1, levels + 1):
        riddles = load_riddles(f'level_{level}.txt')
        points, animals = play_level(level, riddles)
        all_animals.extend(animals)

        if points == 0:
            print("Game over! You have run out of points.\n")
            break

    print(f"Your journey has ended. Animals you met: {', '.join(all_animals)}")

if __name__ == "__main__":
    main()