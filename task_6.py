#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    a = False
    while True:
        if wall_is_beneath():
            a = True
        if not wall_is_beneath() and a:
            break
        move_right()
    pass

if __name__ == '__main__':
    run_tasks()
