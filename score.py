import random


def main():
    score = get_score()
    result = determine_result(score)
    print(f"Score: {score}, Result: {result}")

    random_score = random.randint(0, 100)
    result = determine_result(random_score)
    print(f"Random Score: {random_score}, Result: {result}")


def get_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
