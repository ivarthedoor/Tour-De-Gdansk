"""
🔵 (Niebieski krąg) – \U0001F535
🔴 (Czerwony krąg) – \U0001F534
🟢 (Zielony krąg) – \U0001F7E2
🟡 (Żółty krąg) – \U0001F7E1
"""
#
import random
import questions
def throw_the_dice():
    throw = random.randint(1, 1)
    return throw

board_range = range(1, 30)
position_A = 0
position_B = 1
position_C = 1
position_D = 1
equal_position = 0
player_A_points = 0


def positioning_A():
    global position_A
    position_A += throw_the_dice()

def positioning_B():
    global position_B
    position_B += throw_the_dice()

def positioning_C():
    global position_C
    position_C += throw_the_dice()



def generate_board():
    global position_A
    global position_B
    global position_C
    global equal_position
    
    board_list = ["____" for _ in board_range]
    if  position_A != position_B and position_A != position_C and position_B != position_C:
        board_list[position_A - 1] = "_\U0001F535__"
        board_list[position_B - 1] = "_\U0001F534__"
        board_list[position_C - 1] = "_\U0001F7E2__"
    elif position_A == position_B and position_A == position_C and position_B == position_C:
        equal_position = position_A
        board_list[equal_position - 1] = "_\U0001F535\U0001F534\U0001F7E2"        
    elif position_A == position_B:
        equal_position = position_A  
        board_list[equal_position - 1] = "_\U0001F535\U0001F534_"
        board_list[position_C - 1] = "_\U0001F7E2__"
    elif position_A == position_C:
        equal_position = position_A
        board_list[position_B - 1] = "_\U0001F534__"
        board_list[equal_position - 1] = "_\U0001F535\U0001F7E2_"
    elif position_B == position_C:
        equal_position = position_B
        board_list[position_A - 1] = "_\U0001F535__"
        board_list[equal_position - 1] = "_\U0001F534\U0001F7E2_"
    board_joined = ".".join(board_list)
    return board_joined


def game():
    while True:
        play = input("press a to move A, b to move B, or q to quit: ")
        if play == "a":
            positioning_A()
            if position_A == 3:
                questions.abcd_questions()
                if questions.abcd_questions() == True:
                    player_A_points + 10
                    position_A + 1
                    print(player_A_points)

                else:
                    player_A_points - 10
                    position_A - 1
                    print(player_A_points)

        elif play == "b":
            positioning_B()
        elif play == "c":
            positioning_C()
        elif play == "q":
            break
        print(generate_board())
 
game()
# questions.abcd_question1()