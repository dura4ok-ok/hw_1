#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    while True:
        if wall_is_above() and wall_is_on_the_left():
            while not wall_is_on_the_right():
                move_right()
            while not wall_is_beneath():
                move_down()
            if wall_is_beneath() and wall_is_on_the_right():
                break
        if wall_is_above() and wall_is_on_the_right ():
            while not wall_is_on_the_left():
                move_left()
            while not wall_is_beneath():
                move_down()
            if wall_is_beneath() and wall_is_on_the_left():
                break
        if wall_is_beneath() and wall_is_on_the_left():
            while not wall_is_above():
                move_up()
            while not wall_is_on_the_right():
                move_right()
            if wall_is_above() and wall_is_on_the_right():
                break
        if wall_is_beneath() and wall_is_on_the_right():
            while not wall_is_above():
                move_up()
            while not wall_is_on_the_left():
                move_left()
            if wall_is_above() and wall_is_on_the_left():
                break
pass


if __name__ == '__main__':
    run_tasks()
