#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_right(2)
    for i in range(3):
        move_down()
        fill_cell()
    move_up()
    for i in range(1):
        move_right()
        fill_cell()
        move_left()
    for i in range(1):
        move_left()
        fill_cell()
        move_up()


    pass


if __name__ == '__main__':
    run_tasks()
