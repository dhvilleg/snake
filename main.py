import concurrent
import time

import keyboard
import readchar
import os
import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def drawMap():
    WIDTH = 25
    HEIGHT = 15
    direction = ""
    my_pos_in_list = [12, 7]
    my_eat_in_list = []
    if my_eat_in_list not in my_pos_in_list:
        my_eat_in_list = [random.randint(0, 24), random.randint(0, 14)]
    my_snake_tail = []
    tail_length = 0

    eval_direction = "d"

    while eval_direction != "z":
        clearConsole()

        print("+" + "-" * (WIDTH * 3) + "" + "+")

        for my_position_y in range(HEIGHT):
            print("|", end="")

            for my_position_x in range(WIDTH):

                char_to_draw = " "
                my_eat_in_cell = None
                flag = True

                if my_eat_in_list[0] == my_position_x and my_eat_in_list[1] == my_position_y:
                        char_to_draw = "*"
                        my_eat_in_cell = my_eat_in_list

                if tail_length > 0:
                    for draw_tail in my_snake_tail[-tail_length:]:
                        if draw_tail[0] == my_position_x and draw_tail[1] == my_position_y:
                            char_to_draw = "@"

                if my_position_x == my_pos_in_list[0] and my_position_y == my_pos_in_list[1]:
                    char_to_draw = "@"

                    if my_eat_in_cell:
                        tail_length += 1
                        while flag:
                            position_aux = [random.randint(0, 24), random.randint(0, 14)]
                            if position_aux not in my_pos_in_list and position_aux not in my_snake_tail[-tail_length:]:
                                my_eat_in_list = [random.randint(0, 24), random.randint(0, 14)]
                                flag = False


                print(" {} ".format(char_to_draw), end="")
            print("|")

        print("+" + "-" * (WIDTH * 3) + "" + "+")

        if eval_direction == "w":
            my_snake_tail.append(my_pos_in_list.copy())
            my_pos_in_list[1] = my_pos_in_list[1] - 1
            my_pos_in_list[1] %= HEIGHT
        elif eval_direction == "s":
            my_snake_tail.append(my_pos_in_list.copy())
            my_pos_in_list[1] = my_pos_in_list[1] + 1
            my_pos_in_list[1] %= HEIGHT
        elif eval_direction == "d":
            my_snake_tail.append(my_pos_in_list.copy())
            my_pos_in_list[0] = my_pos_in_list[0] + 1
            my_pos_in_list[0] %= WIDTH
        elif eval_direction == "a":
            my_snake_tail.append(my_pos_in_list.copy())
            my_pos_in_list[0] = my_pos_in_list[0] - 1
            my_pos_in_list[0] %= WIDTH

        if keyboard.is_pressed('w'):

            eval_direction = "w"
        elif keyboard.is_pressed('s'):

            eval_direction = "s"
        elif keyboard.is_pressed('d'):

            eval_direction = "d"
        elif keyboard.is_pressed('a'):

            eval_direction = "a"
        elif keyboard.is_pressed('z'):

            eval_direction = "z"

        if my_pos_in_list in my_snake_tail[-tail_length:] and tail_length != 0:
            print("Juego Terminado, has recogido {} comiditas ".format(tail_length))
            eval_direction = "z"

        time.sleep(0.05)






if __name__ == '__main__':
    drawMap()

