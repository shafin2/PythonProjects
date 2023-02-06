#This program is design for your alarming of water,eye exercise and physical exercise of programmer
#you can add time in respective list and the program will remind you

import datetime as da
import time
import pygame
pygame.mixer.init()
now = da.datetime.now().strftime("%I:%M:%S %p")
print(now)
water_timings = ["10:00:02 AM", "11:00 AM", "12:00:02 PM", "01:00:02 PM", "02:00:02 PM",
                 "01:16:20 PM", "04:00:02 PM", "05:00:02 PM"]
eye_timings = ["09:20:02 AM", "09:50:02 AM", "10:20:02 AM", "10:50:02 AM", "11:20:02 AM",
               "11:50:02 AM", "12:35:02 PM", "12:50:02 PM", "01:20:02 PM", "01:50:02 PM",
               "02:20:02 PM", "02:50:02 PM", "2:06:02 PM", "03:50:02 PM", "04:20:02 PM",
               "04:50:02 PM"
               ]
exercise_timings = ["09:45:02 AM", "10:30:02 AM", "12:15:02 PM", "12:00:02 PM", "12:45:02 PM",
                    "01:30:02 PM", "02:15:02 PM", "03:00:02 PM",
                    "03:45:02 PM", "04:30:02 PM"
                    ]


def water_program():
    print("Its water time")
    pygame.mixer.music.load("C:\\Users\\HUZAIFA CCTV CAMERA\\Downloads\\Music\\hello.mp3")
    pygame.mixer.music.play()
    print("Press d for done")
    user_input = input()
    pygame.mixer.music.pause()
    if user_input == "d":
        print("ok you drink water at", now)
        f = open("water intake", "a")
        content = f"you drink water at {now} \n"
        f.write(content)
        f.close
    else:
        print("You don't drink water at", now)
        f = open("water intake", "a")
        content = f"you Don't drink water at {now} \n"
        f.write(content)
        f.close


def eye_program():
    print("Its time for eye exercise")
    pygame.mixer.music.load("C:\\Users\\HUZAIFA CCTV CAMERA\\Downloads\\Music\\hello.mp3")
    pygame.mixer.music.play()
    print("Press d for done")
    user_input = input()
    pygame.mixer.music.pause()
    if user_input == "d":
        print("ok you done your eye exercise at", now)
        f = open("eye exercise", "a")
        content = f"you done your eye exercise at {now} \n"
        f.write(content)
        f.close
    else:
        print("You dont do eye exercise", now)
        f = open("eye exercise", "a")
        content = f"You dont do eye exercise {now} \n"
        f.write(content)
        f.close


def exercise_program():
    print("Its time for exercise")
    pygame.mixer.music.load("C:\\Users\\HUZAIFA CCTV CAMERA\\Downloads\\Music\\hello.mp3")
    pygame.mixer.music.play()
    print("Press d for done")
    user_input = input()
    pygame.mixer.music.pause()
    if user_input == "d":
        print("ok you done your exercise at", now)
        f = open("exercise", "a")
        content = f"you done your exercise at {now} \n"
        f.write(content)
        f.close
    else:
        print("You dont do exercise", now)
        f = open("exercise", "a")
        content = f"You dont do exercise {now} \n"
        f.write(content)
        f.close


while True:
    now = da.datetime.now().strftime("%I:%M:%S %p")
    if now in water_timings and now in exercise_timings:
        print("you have to do two  tasks")
        water_program()
        exercise_program()
    elif now in water_timings:
        water_program()
    elif now in eye_timings:
        eye_program()
    elif now in exercise_timings:
        exercise_program()
    else:
        continue
