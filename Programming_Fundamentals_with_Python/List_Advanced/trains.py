"""
train_length = int(input())  # Input train length
train = [0] * train_length   # Initialize train with zeros

command = input()  # Read the first command

while command != "End":
    tokens = command.split(" ")
    key_word = tokens[0]

    if key_word == "add":
        # Add people to the last wagon
        people = int(tokens[1])
        train[-1] += people
    elif key_word == "insert":
        # Insert people at a specific index
        index = int(tokens[1])
        people = int(tokens[2])
        if 0 <= index < train_length:
            train[index] += people
    elif key_word == "leave":
        # Remove people from a specific index
        index = int(tokens[1])
        people = int(tokens[2])
        if 0 <= index < train_length:
            train[index] = max(0, train[index] - people)  # Prevent negative number of people

    command = input()  # Read the next command

# Output the final state of the train
print(train)
"""

# second solution
wagons = [0] * int(input())

while True:
    command = input().split()
    current_command = command[0]

    if current_command == "End":
        print(wagons)
        break

    elif current_command == "add":
        number_of_people = int(command[1])
        wagons[-1] += number_of_people

    elif current_command == "insert":
        index = int(command[1])
        number_of_people = int(command[2])
        wagons[index] += number_of_people

    elif current_command == "leave":
        index = int(command[1])
        number_of_people = int(command[2])
        wagons[index] -= number_of_people
