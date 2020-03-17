#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    flag=True
    move_down()
    for i in range(13):
        for j in range(i+1):
            move_right()
            fill_cell()
        move_left(i+1)
        move_down()
    move_right()


if __name__ == '__main__':
    run_tasks()
