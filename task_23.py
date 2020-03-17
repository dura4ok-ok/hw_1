#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.00000000000000000001)
def task_6_6():
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_above():
            move_up()
            fill_cell()
            while not wall_is_above():
                fill_cell()
                move_up()
                fill_cell()
            while not wall_is_beneath():
                move_down()
    while not wall_is_on_the_left():
        move_left()
    move_right()
pass


if __name__ == '__main__':
    run_tasks()
