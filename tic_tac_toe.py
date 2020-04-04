#Pruben
#03/24/220
#Trying to do tic-tac-toe or something
import os

board = []

x_win = False
o_win = False

for i in range (0, 3):
    board.append([])
for row in range (0, 3):
    for col in range(0, 3):
        board[row].append([' '])
        
for i in range (0, 3):
    print(board[i])

def win_con():
    if x_win == True:
        print("X Wins!")
        os._exit()
    elif o_win == True:
        print("O Wins!")
        os._exit()
    elif x_win != True and o_win != True:
        sep_boy = 0
        for row in range(0, 3):
            for col in range(0, 3):
                sep_boy += board[row].count([' '])
                
        if sep_boy == 0:
            print("Cat's Game!")
            os._exit()
            
        
            
while True:
    
    while True:
        print("X's Turn!")
        print()
        print("\t   1\t   2\t   3")
        print("\nA\t" , board[0][0] , "\t" , board[0][1] , "\t" , board[0][2])
        print("\nB\t", board[1][0], "\t", board[1][1], "\t", board[1][2])
        print("\nC\t", board[2][0], "\t", board[2][1], "\t", board[2][2])
        print()
        while True:
            x_move = input("Please pick your move! (Example A1): ")
            sep = list(x_move)
            if x_move == '':
                print("Invalid input! Please try again.")
                print()
                continue
            if len(sep) != 2:
                print("Invalid input! Please try again.")
                print()
                continue
            
            cap_check = sep[0].upper()
            
            if cap_check == "A":
                if sep[1] == '1':
                    if board[0][0] == [' ']:
                        board[0][0] = ['X']
                        if board[0][1] == ['X'] and board[0][2] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[1][0] == ['X'] and board[2][0] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[1][1] == ['X'] and board[2][2] == ['X']:
                            print("X Winds!")
                            print()
                            x_win = True
                            
                    
                        break
                    else:
                        print("That space is already taken!")
                        print("Try again!")
                        print("1")
                elif sep[1] == '2':
                    if board[0][1] == [' ']:
                        board[0][1] = ['X']
                        if board[0][0] == ['X'] and board[0][2] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[1][1] == ['X'] and board[2][1] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        break
                    else:
                        print("That space is already taken.")
                        print("Try again!")
                        print()
                elif sep[1] == '3':
                    if board[0][2] == [' ']:
                        board[0][2] = ['X']
                        if board[0][0] == ['X'] and board[0][1] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[1][1] == ['X'] and board[2][0] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[1][2] == ['X'] and board[2][2] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True                           
                        
                        break
                    else:
                        print("That space is already taken.")
                        print("Please try again!")
                        print()
                
                else:
                    print("Invalid input! Please try again.")
                    print()
            
                    
            elif cap_check == "B":
                if sep[1] == '1':
                    if board[1][0] == [' ']:
                        board[1][0] = ['X']
                        if board[0][0] == ['X'] and board[2][0] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[1][1] == ['X'] and board[1][2] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                            
                        break
                    else:
                        print("That space is already taken!")
                        print("Please try again!")
                        print()
                elif sep[1] == '2':
                    if board[1][1] == [' ']:
                        board[1][1] = ['X']
                        if board[1][0] == ['X'] and board[1][2] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[0][0] == ['X'] and board[2][2] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[0][1] == ['X'] and board[2][1] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[0][2] == ['X'] and board[2][0] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        
                        break
                    else:
                        print("That space is already taken")
                        print("Please try again!")
                        print()
                
                elif sep[1] == '3':
                    if board[1][2] == [' ']:
                        board[1][2] = ['X']
                        if board[1][1] == ['X'] and board[1][0] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[0][2] == ['X'] and board[2][2] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
    
                        break
                    else:
                        print("That space is already taken.")
                        print("Try again!")
                        print()
            
                else:
                    print("Invalid input! Please try again.")
                    print()
        
            elif cap_check == "C":
                if sep[1] == '1':
                    if board[2][0] == [' ']:
                        board[2][0] = ['X']
                        if board[0][0] == ['X'] and board[1][0] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[2][1] == ['X'] and board[2][2] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[1][1] == ['X'] and board[0][2] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        break
                    else:
                        print("That space is already taken.")
                        print("Try again!")
                        print()
                elif sep[1] == '2':
                    if board[2][1] == [' ']:
                        board[2][1] = ['X']
                        if board[2][0] == ['X'] and board[2][2] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[1][1] == ['X'] and board[0][1] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        
                        break
                    else:
                        print("That space is already taken.")
                        print("Please try agin!")
                        print()
                elif sep[1] == '3':
                    if board[2][2] == [' ']:
                        board[2][2] = ['X']
                        if board[2][0] == ['X'] and board[2][1] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        elif board[1][1] == ['X'] and board[0][0] == ['X']:
                            print("X Wins!")
                            print()
                            x_win = True
                        break
                    else:
                        print("That space is already taken.")
                        print("Try again!")
                        print()
                else:
                    print("Invalid input! Please try again.")
                    print()
        win_con()
        break            
        
    while True:
        print("O's Turn!")
        print()
        print("\t   1\t   2\t   3")
        print("\nA\t" , board[0][0] , "\t" , board[0][1] , "\t" , board[0][2])
        print("\nB\t", board[1][0], "\t", board[1][1], "\t", board[1][2])
        print("\nC\t", board[2][0], "\t", board[2][1], "\t", board[2][2])
        print()
        while True:
            x_move = input("Please pick your move! (Example A1): ")
            sep = list(x_move)
            
            if x_move == '':
                print("Invalid input! Please try again.")
                print()
                continue
            if len(sep) != 2:
                print("Invalid input! Please try again.")
                print()
                continue
            
            cap_check = sep[0].upper()
            
            if cap_check == "A":
                if sep[1] == '1':
                    if board[0][0] == [' ']:
                        board[0][0] = ['O']
                        if board[0][1] == ['O'] and board[0][2] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        elif board[1][0] == ['O'] and board[2][0] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        elif board[1][1] == ['O'] and board[2][2] == ['O']:
                            print("O Winds!")
                            print()
                            o_win = True
                            
                    
                        break
                    else:
                        print("That space is already taken!")
                        print("Try again!")
                        print("1")
                elif sep[1] == '2':
                    if board[0][1] == [' ']:
                        board[0][1] = ['O']
                        if board[0][0] == ['O'] and board[0][2] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        elif board[1][1] == ['O'] and board[2][1] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        break
                    else:
                        print("That space is already taken.")
                        print("Try again!")
                        print()
                elif sep[1] == '3':
                    if board[0][2] == [' ']:
                        board[0][2] = ['O']
                        if board[0][0] == ['O'] and board[0][1] == ['O']:
                            print("O Wins!")
                            print()
                            x_win = True
                        elif board[1][1] == ['O'] and board[2][0] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        elif board[1][2] == ['O'] and board[2][2] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True                           
                        
                        break
                    else:
                        print("That space is already taken.")
                        print("Please try again!")
                        print()
                
                else:
                    print("Invalid input! Please try again.")
                    print()
            
                    
            elif cap_check == "B":
                if sep[1] == '1':
                    if board[1][0] == [' ']:
                        board[1][0] = ['O']
                        if board[0][0] == ['O'] and board[2][0] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        elif board[1][1] == ['O'] and board[1][2] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                            
                        break
                    else:
                        print("That space is already taken!")
                        print("Please try again!")
                        print()
                elif sep[1] == '2':
                    if board[1][1] == [' ']:
                        board[1][1] = ['O']
                        if board[1][0] == ['O'] and board[1][2] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        elif board[0][0] == ['O'] and board[2][2] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        elif board[0][1] == ['O'] and board[2][1] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        elif board[0][2] == ['O'] and board[2][0] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        
                        break
                    else:
                        print("That space is already taken")
                        print("Please try again!")
                        print()
                
                elif sep[1] == '3':
                    if board[1][2] == [' ']:
                        board[1][2] = ['O']
                        if board[1][1] == ['O'] and board[1][0] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        elif board[0][2] == ['O'] and board[2][2] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        
                        break
                    else:
                        print("That space is already taken.")
                        print("Try again!")
                        print()
            
                else:
                    print("Invalid input! Please try again.")
                    print()
        
            elif cap_check == "C":
                if sep[1] == '1':
                    if board[2][0] == [' ']:
                        board[2][0] = ['O']
                        if board[0][0] == ['O'] and board[1][0] == ['O']:
                            print("O Wins!")
                            print()
                            x_win = True
                        elif board[2][1] == ['O'] and board[2][2] == ['O']:
                            print("O Wins!")
                            print()
                            x_win = True
                        elif board[1][1] == ['O'] and board[0][2] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        break
                    else:
                        print("That space is already taken.")
                        print("Try again!")
                        print()
                elif sep[1] == '2':
                    if board[2][1] == [' ']:
                        board[2][1] = ['O']
                        if board[2][0] == ['O'] and board[2][2] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        elif board[1][1] == ['O'] and board[0][1] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        
                        break
                    else:
                        print("That space is already taken.")
                        print("Please try agin!")
                        print()
                elif sep[1] == '3':
                    if board[2][2] == [' ']:
                        board[2][2] = ['O']
                        if board[2][0] == ['O'] and board[2][1] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        elif board[1][1] == ['O'] and board[0][0] == ['O']:
                            print("O Wins!")
                            print()
                            o_win = True
                        break
                    else:
                        print("That space is already taken.")
                        print("Try again!")
                        print()
                else:
                    print("Invalid input! Please try again.")
                    print()
        win_con()
        break
            
            
    
        
        
    