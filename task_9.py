#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    while True:
        if wall_is_beneath() and not wall_is_above():
            fill_cell()
        if wall_is_on_the_right():
            break
        move_right()
    pass


if __name__ == '__main__':
    run_tasks()
