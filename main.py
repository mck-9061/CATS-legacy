import os
import time
import pydirectinput
import pyautogui
import random
import threading
import pyperclip
import datetime

import journalwatcher
from discordhandler import post_to_discord
from screenreader import time_until_jump

import pygetwindow as gw

# ----Options----
# How many up presses to reach tritium in carrier hold:
global tritium_slot
# Time to refill trit
hold_time = 10

global route_file

window_name = "Elite - Dangerous (CLIENT)"

# Test webhook
# webhook_url = "https://discord.com/api/webhooks/985215199034351696/dsV5EQQO0bvPTwwP0l-8E3FJltFL7B3h8MHnuK3zIzG5BqNjaERE8ZLO87Q0I7t9Nw_P"
# Prod webhook
global webhook_url

global journal_directory


def load_settings():
    global tritium_slot
    global webhook_url
    global journal_directory
    global route_file

    try:
        settingsFile = open("settings.txt", "r")
        a = settingsFile.read().split('\n')

        try:
            for line in a:
                if line.startswith("webhook_url="): webhook_url = line.split("=")[1]
                if line.startswith("journal_directory="): journal_directory = line.split("=")[1]

                latest_journal()

                if line.startswith("tritium_slot="): tritium_slot = int(line.split("=")[1])
                if line.startswith("route_file="): route_file = int(line.split("=")[1])
        except:
            print("There seems to be a problem with your settings file. Make sure of the following:\n"
                  "- Your tritium slot is a valid integer. It should be the number of up presses it takes to reach "
                  "tritium in your carrier's cargo hold from the transfer menu.\n"
                  "- The journal directory is a valid directory for your operating system, and contains the Elite"
                  " Dangerous journal files.")


    except:
        settingsFile = open("settings.txt", "w+")
        settingsFile.write("webhook_url=\n"
                           "journal_directory=\n"
                           "tritium_slot=\n")

        print("Settings file created, please set up and run again")


def latest_journal():
    dir_name = journal_directory
    # Get list of all files only in the given directory
    list_of_files = filter(lambda x: os.path.isfile(os.path.join(dir_name, x)),
                           os.listdir(dir_name))
    # Sort list of files based on last modification time in ascending order
    list_of_files = sorted(list_of_files,
                           key=lambda x: os.path.getmtime(os.path.join(dir_name, x))
                           )
    list_of_files.reverse()

    journalName = ""
    i = 0
    while not journalName.startswith("Journal"):
        journalName = list_of_files[i]
        i += 1

    return journal_directory + journalName.strip()


def slight_random_time(time):
    return random.random() + time


def restock_tritium():
    # Navigate menu
    pydirectinput.press('4')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('e')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('e')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('e')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('e')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('d')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('w')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('d')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('space')
    time.sleep(slight_random_time(0.1))

    for i in range(tritium_slot):
        pydirectinput.press('up')
        time.sleep(slight_random_time(0.1))

    pydirectinput.keyDown('left')
    time.sleep(slight_random_time(hold_time))
    pydirectinput.keyUp('left')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('space')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('space')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('backspace')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('q')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('q')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('q')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('q')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('4')
    time.sleep(slight_random_time(0.1))

    # Refill tank
    pydirectinput.press('space')
    time.sleep(slight_random_time(5))
    pydirectinput.press('s')
    time.sleep(slight_random_time(0.2))
    pydirectinput.press('s')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('space')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('space')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('w')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('space')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('backspace')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('s')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('space')
    time.sleep(slight_random_time(0.1))

    # Navigate back to menu
    pydirectinput.press('backspace')

    print("Tritium successfully refuelled.")


def jump_to_system(system_name):
    # Navigate menu
    pydirectinput.press('space')
    time.sleep(slight_random_time(5))
    pydirectinput.press('d')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('s')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('d')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('space')

    time.sleep(slight_random_time(6.0))

    # Navigate carrier menu
    pydirectinput.press('s')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('space')
    time.sleep(slight_random_time(0.1))

    # Select system
    pydirectinput.press('space')
    time.sleep(slight_random_time(4.0))
    pyautogui.moveTo(921, 115)
    time.sleep(slight_random_time(0.1))
    pyautogui.moveTo(930, 115)
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('space')

    pyperclip.copy(system_name.lower())
    time.sleep(slight_random_time(1.0))

    # pydirectinput.write(system_name.lower())
    pydirectinput.keyDown("ctrl")
    time.sleep(slight_random_time(0.1))
    pydirectinput.press("v")
    time.sleep(slight_random_time(0.1))
    pydirectinput.keyUp("ctrl")

    time.sleep(slight_random_time(3.0))
    pydirectinput.press('down')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('space')
    time.sleep(slight_random_time(0.1))
    pyautogui.moveTo(1496, 422)
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('space')

    time.sleep(6)

    # Navigate carrier menu
    pydirectinput.press('s')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('space')

    if journalwatcher.last_carrier_request() != system_name:
        print(journalwatcher.lastCarrierRequest)
        print(system_name)
        print("Jump appears to have failed.")
        print("Re-attempting...")
        pydirectinput.press('backspace')
        time.sleep(slight_random_time(0.1))
        pydirectinput.press('backspace')
        time.sleep(slight_random_time(0.1))
        pydirectinput.press('backspace')
        time.sleep(slight_random_time(0.1))
        pydirectinput.press('backspace')
        time.sleep(slight_random_time(0.1))
        pydirectinput.press('backspace')
        time.sleep(slight_random_time(0.1))
        pydirectinput.press('backspace')
        time.sleep(slight_random_time(0.1))
        pydirectinput.press('w')
        time.sleep(slight_random_time(0.1))
        pydirectinput.press('w')
        time.sleep(slight_random_time(0.1))
        pydirectinput.press('w')
        time.sleep(slight_random_time(0.1))
        pydirectinput.press('w')
        time.sleep(slight_random_time(0.1))
        pydirectinput.press('w')
        time.sleep(slight_random_time(0.1))
        pydirectinput.press('s')
        time.sleep(slight_random_time(0.1))
        return 0

    timeToJump = time_until_jump()
    print(timeToJump.strip())

    failCount = 0

    while len(timeToJump.split(':')) == 1:
        print("Trying again... (" + str(failCount) + ")")
        timeToJump = time_until_jump()
        print(timeToJump.strip())
        failCount += 1

    time.sleep(6)
    pydirectinput.press('backspace')
    time.sleep(slight_random_time(0.1))
    pydirectinput.press('backspace')

    return timeToJump.strip()


global lineNo


def main_loop():
    global lineNo
    global tritium_slot
    global webhook_url
    global journal_directory
    global route_file


    latestJournal = latest_journal()

    currentTime = datetime.datetime.now(datetime.timezone.utc)
    arrivalTime = currentTime

    th = threading.Thread(target=process_journal, args=(latestJournal,))
    th.start()

    win = gw.getWindowsWithTitle(window_name)[0]
    win.activate()

    lineNo = 0
    saved = False

    if os.path.exists("save.txt"):
        print("Save file found. Setting up...")
        lineNo = int((open("save.txt", "r")).read())
        os.remove("save.txt")

        saved = True

    print("Beginning in 5...")
    time.sleep(5)
    # print("Stocking initial tritium...")
    # restock_tritium()

    routeFile = open(route_file, "r")
    route = routeFile.read()

    finalLine = route.split("\n")[len(route.split("\n")) - 1]
    jumpsLeft = len(route.split("\n")) + 1

    routeName = "Carrier Updates: Route to " + finalLine

    a = route.split("\n")

    delta = datetime.timedelta()
    for i in a:
        if a.index(i) < lineNo: continue
        delta = delta + datetime.timedelta(seconds=1320)
    arrivalTime = arrivalTime + delta

    doneFirst = False
    for i in range(len(a)):
        jumpsLeft -= 1
        if i < lineNo: continue

        line = a[i]

        win.activate()
        time.sleep(3)

        print("Next stop: " + line)
        print("Beginning navigation.")
        print("Please do not change windows until navigation is complete.")

        print(arrivalTime.strftime("%d %b %Y %H:%M %Z"))

        try:
            timeToJump = jump_to_system(line)
            while timeToJump == 0: timeToJump = jump_to_system(line)
            print("Navigation complete. Jump occurs in " + timeToJump + ". Counting down...")

            hours = int(timeToJump.split(':')[0])
            minutes = int(timeToJump.split(':')[1])
            seconds = int(timeToJump.split(':')[2])

            totalTime = (hours * 3600) + (minutes * 60) + seconds - 7

            if totalTime > 900:
                arrivalTime = arrivalTime + datetime.timedelta(seconds=totalTime - 900)
                print(arrivalTime.strftime("%d %b %Y %H:%M %Z"))

            if doneFirst:
                previous_system = a[i - 1]
                post_to_discord("Carrier Jump", webhook_url,
                                "The carrier has jumped to the " + previous_system + " system.\n"
                                                                                     "Jumps remaining: " + str(
                                    jumpsLeft) +
                                "\nNext system: " + line +
                                "\nEstimated time until next jump: " + timeToJump +
                                "\nEstimated time of route completion: " + arrivalTime.strftime("%d %b %Y %H:%M %Z") +
                                "\no7", routeName)
            else:
                if not saved:
                    post_to_discord("Flight Begun", webhook_url,
                                    "The Flight Computer has begun navigating the Carrier.\n"
                                    "The Carrier's route is as follows:\n" +
                                    route +
                                    "\nEstimated time until first jump: " + timeToJump +
                                    "\nEstimated time of route completion: " + arrivalTime.strftime(
                                        "%d %b %Y %H:%M %Z") +
                                    "\no7", routeName
                                    )
                else:
                    post_to_discord("Flight Resumed", webhook_url,
                                    "The Flight Computer has resumed navigation after a failure.\n"
                                    "Estimated time until first jump: " + timeToJump +
                                    "\nEstimated time of route completion: " + arrivalTime.strftime(
                                        "%d %b %Y %H:%M %Z") +
                                    "\no7", routeName
                                    )


        except Exception as e:
            print(e)
            print("An error has occurred. Saving progress and aborting...")
            post_to_discord("Critical Error", webhook_url,
                            "An error has occurred with the Flight Computer.\n"
                            "It's possible the game has crashed, or servers were taken down.\n"
                            "Please wait for the carrier to resume navigation.\n"
                            "o7", routeName)
            print("Message sent...")
            saveFile = open("save.txt", "w+")
            saveFile.write(str(lineNo))
            saveFile.close()
            print("Progress saved...")
            return False

        while totalTime > 0:
            print(totalTime)
            time.sleep(1)
            totalTime -= 1

        print("Jumping!")
        lineNo += 1

        if not line == finalLine:
            print("Counting down until next jump...")
            totalTime = 360
            while totalTime > 0:
                print(totalTime)
                time.sleep(1)
                totalTime -= 1

                if totalTime == 150:
                    print("Restocking tritium...")
                    win.activate()
                    time.sleep(2)
                    th = threading.Thread(target=restock_tritium)
                    th.start()

        else:
            print("Counting down until jump finishes...")
            totalTime = 60
            while totalTime > 0:
                print(totalTime)
                time.sleep(1)
                totalTime -= 1

        doneFirst = True

    print("Route complete!")
    post_to_discord("Carrier Arrived", webhook_url,
                    "The route is complete, and the carrier has arrived at " + finalLine + ".\n"
                                                                                           "o7", routeName)
    return True


def process_journal(file_name):
    while True:
        c = journalwatcher.process_journal(file_name)
        if not c:
            print("An error has occurred. Saving progress and aborting...")
            post_to_discord("Critical Error", webhook_url,
                            "An error has occurred with the Flight Computer.\n"
                            "It's possible the game has crashed, or servers were taken down.\n"
                            "Please wait for the carrier to resume navigation.\n"
                            "o7", "")
            print("Message sent...")
            saveFile = open("save.txt", "w+")
            saveFile.write(str(lineNo))
            saveFile.close()
            print("Progress saved...")
            raise SystemExit(0)

        time.sleep(1)


if not main_loop():
    print("Aborted.")
raise SystemExit(0)
