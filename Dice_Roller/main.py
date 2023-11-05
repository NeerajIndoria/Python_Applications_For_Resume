import random

print("Welcome to Neeraj Indoria/'s Application")
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


def generate_dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])

    dice_faces_row = []
    for row_index in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_index])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_row.append(row_string)

    width = len(dice_faces_row[0])
    diagram_header = "RESULTS".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_row)
    return dice_faces_diagram


def parse_input(input_user):
    if input_user in {"1", "2", "3", "4", "5", "6"}:
        return int(input_user)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)


def roll_dice(num_dic):
    roll_result = []
    for _ in range(num_dic):
        roll = random.randint(1, 6)
        roll_result.append(roll)
    return roll_result


# main code block
# Get and Validate user input

user_input = input("Enter Number of Dice/'s you want to roll?? [1-6] : ")
num_dice = parse_input(user_input)

# roll the dice
roll_results = roll_dice(num_dice)
print(roll_results)

# Generate the ASCII diagram of dice faces
dice_face_diagram = generate_dice_faces(roll_results)

# Display the diagram
# print(f"\n{dice_face_diagram}")
