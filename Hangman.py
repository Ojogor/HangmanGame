import random
import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.hideturtle()
t.backward(150)
t.penup()
t.forward(150)
t.left(90)
t.pendown()
t.forward(200)
t.penup()
t.right(90)
t.right(90)
t.forward(200)
t.left(90)
t.pendown()
t.forward(200)
t.backward(200)
t.left(90)
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.penup()
t.right(90)
#t.forward()
t.pendown()
def draw_hangman(num_wrong):
    if num_wrong == 0:
    #head intilizie
        t.circle(15)
        t.left(90)
        t.penup()
        t.forward(31)
        t.pendown()
    if num_wrong == 1:
    #neck
        t.forward(10)
    #left arm
    if num_wrong == 2:
        t.right(65)
        t.forward(30)
        t.penup()
        t.backward(30)
        t.pendown()
    #right arm
    if num_wrong==3:
        t.right(235)
        t.forward(30)
        t.penup()
        t.backward(30)
        t.pendown()
        t.left(235+65)
    #body
    if num_wrong==4:
        t.forward(45)
    #left leg
    if num_wrong==5:
        t.right(65)
        t.forward(15)
        t.penup()
        t.backward(15)
        t.pendown()
    #right leg
    if num_wrong==6:
        t.right(235)
        t.forward(15)
        t.penup()
        t.backward(15)
        t.pendown()
        t.left(235+65)

def choose_word():
    easy_words = ['cat', 'dog', 'bird', 'book', 'cup', 'milk', 'fish', 'cake', 'home', 'tree', 'sun', 'moon', 'car', 'bus', 'baby', 'door', 'hat', 'love', 'pen', 'duck']
    hard_words = ['xylophone', 'jazz', 'cryptocurrency', 'jigsaw', 'rhythm', 'yacht', 'jukebox', 'zigzag', 'voodoo', 'jockey', 'pneumonia', 'syzygy', 'mnemonic', 'zephyr', 'gazebo', 'haphazard', 'juxtaposition', 'kilobyte', 'quicksilver', 'whiskey']
    words = easy_words + hard_words
    return random.choice(words)
def init_board(word):
    board = "#" * len(word)
    return list(board)

# Define a function to display the game board
def display_board(board):
    print("".join(board))
def play_hangman():
    word = choose_word()
    board = init_board(word)
    display_board(board)
    guessed_letters = []
    num_wrong = -1
    while num_wrong < 6:
        player_letter_guess = input("Guess a letter: ").lower()
        if player_letter_guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        if player_letter_guess in word:
            print("Correct guess!")
            for i in range(len(word)):
                if word[i] == player_letter_guess:
                    board[i] = player_letter_guess
            display_board(board)
            if "#" not in board:
                print("Congratulations, you guessed the word!")
                break
        else:
            print("Incorrect guess!")
            num_wrong += 1 
            draw_hangman(num_wrong)
        guessed_letters.append(player_letter_guess)
        print("Guessed letters:", "".join(guessed_letters))
    if num_wrong == 6:
        print("Game over! You are hanged. The word was", word)
    turtle.Screen().exitonclick()
play_hangman()