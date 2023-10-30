import random

def init_game():
    pass

def load_words(txt_path: str):
    """
    Load the words from given txt_path

    Args:
        - txt_path: path of the text file to read.

    Returns:
        - word_list: the list of word .
    """
    with open(txt_path, "r") as file:
        word_list = [word.strip() for word in file]

    return word_list

if __name__ == '__main__':
    random.seed(42)

    print("Let's start the Wordle!")

    word_list = load_words()

    random_word = random.choice(word_list)

    while True:
            
        attempts = 0

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
                print(feedback)`