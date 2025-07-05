# PersonalGreeting.py

def personal_greeting():
    name = input("What is your name? ")
    age = input("How old are you? ")
    color = input("What is your favorite color? ")

    message = (
        f"Hello, {name}! You are {age} years old and your favorite color is {color}. "
        "That's awesome! Have a fantastic day!"
    )

    print(message)

if __name__ == "__main__":
    personal_greeting()
