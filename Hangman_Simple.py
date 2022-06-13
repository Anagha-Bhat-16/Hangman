import random  # import random module for usage

score = 0  # Maintain Win Scores
score_loss = 0  # Maintain Loss Scores
wordlist = ["python", "java", "swift", "javascript"]  # create list of possible words

print("H A N G M A N")  # HANGMAN
while True:
    command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')  # Menu
    if command == 'play':
        attempts = 8  # counter to track attempts
        attempt_list = []  # to track the guesses
        answer = random.choice(wordlist)  # set answer to random choice from list of possible words
        masked_answer = len(answer) * "-"  # create a masked answer with hyphens
        dummy = answer  # to count the occurrences of letter and update the masked answer
        print()
        print(masked_answer)
        while attempts > 0:  # enter loop if attempts are still left
            letter = input("Input a letter: ")  # accept input
            if len(letter) != 1:  # check for erroneous input
                print("Please, input a single letter.")
                print()
                print(masked_answer)
            elif letter.isalpha() and letter.islower():  # if correct input proceed
                attempts -= 1
                if letter not in attempt_list:  # new guess
                    attempt_list.append(letter)
                    if letter in answer:  # new guess - correct
                        c = answer.count(letter)
                        temp = list(masked_answer)
                        for j in range(c):  # loop to create new mask
                            pos = dummy.find(letter)
                            temp[pos] = letter
                            dummy = dummy[:pos] + " " + dummy[pos + 1:]
                        masked_answer = "".join(temp)
                        print()
                        print(masked_answer)
                        attempts += 1
                        if masked_answer == answer:  # check win/lose status
                            print("You guessed the word {}!".format(masked_answer))
                            print("You survived!")
                            score += 1  # update win score
                            break
                    else:  # new guess - incorrect
                        print("That letter doesn't appear in the word.")
                        print()
                        print(masked_answer)
                else:  # old guess
                    print("You've already guessed this letter.")
                    print()
                    print(masked_answer)
                    attempts += 1
            else:  # erroneous input
                print("Please, enter a lowercase letter from the English alphabet.")
                print()
                print(masked_answer)
        if masked_answer != answer:  # check win/lose status
            print()
            print("You lost!")
            score_loss += 1  # update loss score
    elif command == 'results':  # If player selects 'results' option
        print('You won: {} times'.format(score))
        print('You lost: {} times'.format(score_loss))
    elif command == 'exit':  # If player selects 'exit' option
        quit()
    else:
        continue
