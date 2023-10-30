import random

with open("five_digit_word.txt", "r") as file:
    word_list = [word.strip() for word in file]

print("Let's start the Wordle!")
random.seed(42)
while True:
    random_word = random.choice(word_list)
    attempts = 0
    
    user_input = " "
    feedback = " "

    while True: 
        user_input = input("Type in 5 digit word! Press @ if you want to end")
        attempts += 1

        if len(user_input) != 5:
            print("Wrong input. Please type in 5 digit word.")
        
        if user_input == '@' :
            print("Game Ended.")
            break

        if user_input == random_word : 
            print("You're Right!")
            print("Right answer in", attempts, "times")
            break
        
        else : 
            feedback = " "
        for i in range(5):
            if user_input[i] == random_word[i] :
                feedback += [i]
            elif user_input[i] in random_word :
                feedback += '#'
            else: 
                feedback += '_'
        
        if attempts > 1:
            print(feedback)