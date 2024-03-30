import random
# Get Guess
def get_guess():
    return list(input("What is your guess??"))
# Generate Computer Code 123
def generate_code():
    digits = [str(num) for num in range(10)]
    #Shuffle the digits
    random.shuffle(digits)
    #then grab the first three
    return digits[:3]
# Generate the Clues
def generate_clues(code,user_guess):

    if user_guess == code:
        return "Congratulations Code Cracked!!"
    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    
    if clues == []:
        return ["Nope"]
    else:
        return clues



# Run game logic
    
print("Welcome to the Code Breaker!!")

secret_code = generate_code()

clue_report = []

while clue_report != "Congratulations Code Cracked!!":
    guess = get_guess()
    clue_report = generate_clues(guess,secret_code)
    print("The result of your guess is: ")
    for clue in clue_report:
        print (clue)