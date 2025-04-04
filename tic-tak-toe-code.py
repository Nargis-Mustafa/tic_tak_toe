# step to do
# (1) board (2) Display board (3) Enter the input by the user

# Some details about the game before starting.
print("Welcome to the Tic-Tac-Toe Game\n")
print("Rules of the game\n")
print("Player 1 = X")
print("Player 2 = 0\n")

chance=input("Enter the chance X or O to initiate the game: ")

# Variable to store the board

board=["1","2","3",
       "4","5","6",
       "7","8","9"]

check_board=["1","2","3","4","5","6","7","8","9"]

# Display the board
def print_board():
    print("\n")
    print(f" {board[0]}|{board[1]}|{board[2]}")
    print("-------")
    print(f" {board[3]}|{board[4]}|{board[5]}")
    print("-------")
    print(f" {board[6]}|{board[7]}|{board[8]}")

# Check the input is valid or not
def input_check(number):
    if number not in range(1,10):
        print("Invalid Number")
        take_input()

condition=True
# Take the input from the user
def take_input():
    while (condition):
        global chance
        if (chance=="x"):
            intake = int(input("\n X please enter the number from 1-9: "))
            input_check(intake)
            if (board[(intake-1)]=="x"or board[(intake-1)]=="0"):
                print("override is not allowed")
            else:
                board[(intake-1)]="x"
                check_board[(intake-1)]=False
                print_board()
                x_chack_win()
                chance="0"
        else:
            intake = int(input("\n0 please  enter the number from 1-9: "))
            input_check(intake)
            if (board[(intake-1)]=="x"or board[(intake-1)]=="0"):
                print("override is not allowed")
            else:
                board[(intake-1)]="0"
                check_board[(intake-1)]=False
                print_board()
                y_chack_win()
                chance="x"

# Check the wining condition for the X team
def x_chack_win():
    if (board[0]=="x" and board[1]=="x" and board[2]=="x") or (board[3]=="x" and board[4]=="x" and board[5]=="x") or (board[6]=="x" and board[7]=="x" and board[8]=="x") or (board[0]=="x" and board[4]=="x" and board[8]=="x") or (board[2]=="x" and board[4]=="x" and board[6]=="x") or (board[0]=="x" and board[3]=="x" and board[6]=="x") or(board[1]=="x" and board[4]=="x" and board[7]=="x") or (board[2]=="x" and board[5]=="x" and board[8]=="x"):
        print("\nWaaaoooo X team Win")
        global condition
        condition=False
        return condition
    else:
        res=any(i for i in check_board)
        if res==False:
            print("\nMatch Draw")
            #global condition
            condition =False
            return condition
            
# Check the wining condition for the 0 team   
def y_chack_win():
    if (board[0]=="0" and board[1]=="0" and board[2]=="0") or (board[3]=="0" and board[4]=="0" and board[5]=="0") or (board[6]=="0" and board[7]=="0" and board[8]=="0") or (board[0]=="0" and board[4]=="0" and board[8]=="0") or (board[2]=="0" and board[4]=="0" and board[6]=="0") or (board[0]=="0" and board[3]=="0" and board[6]=="0")or (board[1]=="0" and board[4]=="0" and board[7]=="0") or (board[2]=="0" and board[5]=="0" and board[8]=="0") :
        print("\nWaaaoooo 0 team Win")
        global condition
        condition=False
        return condition
    else:
        res=any(i for i in check_board)
        if res==False:
            print("\nMatch Draw")
            #global condition
            condition=False
            return condition
        
print_board()
take_input()


