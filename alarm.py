#!/usr/bin/env python3
import os
import sched
import time


def runner(s, t):
    if time.time() - t < 20:
        os.system("aplay /home/ab/Code/alarm/buzzer.wav")
        print("Do it!")
    else:
        print("skipped:", time.ctime(t))
    print_queue(s, "remaining:")


def print_queue(s, text):
    for k in s.queue:
        print(text, time.ctime(k.time))


def main():
    now = time.localtime()
    hour = now.tm_hour
    r = range(hour if hour > 10 else 10, 20)
    s = sched.scheduler(time.time)
    for i in r:
        t = time.mktime(
                (now.tm_year, now.tm_mon, now.tm_mday, i, 0, 0, 0, 0, 0))
        if t < time.time():
            continue
        s.enterabs(t, 1, runner, argument=(s, t))

    print_queue(s, "scheduled:")

    s.run()


if __name__ == "__main__":
    main()
