#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# get names
names = []
with open("./Input/Names/invited_names.txt") as name_file:
    for line in name_file.readlines():
        names.append(line.strip())

letter_template = ""
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_template = letter_file.read()

for name in names:
    with open(f"./Output/ReadyToSend/letter_to_{name}", mode="w") as letter:
        letter.write(letter_template.replace("[name]", name))

# open letter
# take template
# save letter