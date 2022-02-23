invites = []

with open("input/names/invited_names.txt") as file:
    invites = file.read().splitlines()

for invite in invites:
    with open("input/letters/starting_letter.txt") as file:
        content = file.read()
    content = content.replace("[name]", invite)
    letter = f"output/ready-to-send/{invite} invite.txt"
    with open(letter, "w") as new_file:
        new_file.write(content)

