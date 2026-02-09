name = input("Enter your name: ")
goal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
    file.write(f"{name} - Daily Goal: {goal}\n")

print("Saved successfully!")

with open("journal.txt", "r") as file:
    content = file.read()

print(content)
