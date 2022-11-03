from discord_webhook import DiscordWebhook, DiscordEmbed
from tkinter import messagebox
from tkinter import Tk
import os
import time
import pydirectinput

# Tool for helping with t10 AFK
# Alerts you when a fighter is destroyed or your shields are popped
# Alerts through both Windows and Discord
# It can also close the game when the shields are popped IF the game is focused.
# Only enable this when going truly AFK.
closeWhenPopped = True

# FighterDestroyed
# Music (MusicTrack: MainMenu)
# ShieldState (ShieldsUp: false)


global journal_directory
journal_directory = ""


def load_settings():
    global journal_directory

    try:
        settingsFile = open("settings.txt", "r")
        a = settingsFile.read().split('\n')

        try:
            for line in a:
                if line.startswith("journal_directory="):
                    print(line)
                    journal_directory = line.split("=")[1]
                    journal_directory = latest_journal()

        except Exception as e:
            print(e)


    except Exception as e:
        print(e)


def latest_journal():
    global journal_directory
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


global firstRun
firstRun = True
global lastJournalText
lastJournalText = ""


def process_journal():
    global journal_directory
    global lastJournalText
    global firstRun

    journal = open(journal_directory, "r")
    journalText = journal.read()
    journal.close()

    if journalText != lastJournalText:

        newText = journalText.replace(lastJournalText, "").strip()

        for line in newText.split("\n"):
            event = line.split(':')[4].split('"')[1].strip()
            #print(event)

            if event == "Bounty":
                credits = line.split(':')[7].split(' ')[0].strip()
                print("Bounty gained: " + credits)

            if event == "Music":
                track = line.split(':')[5].split('"')[1].strip()
                # print("Music track: " + track)

                if track == "MainMenu" and not firstRun:
                    print("Ship destroyed")
                    messagebox.showerror("F", "Your ship has been destroyed!")


            if event == "FighterDestroyed" and not firstRun:
                print("Fighter down")
                if not closeWhenPopped:
                    messagebox.showwarning("Fighter down", "Your NPC fighter has been destroyed - redeploy.")

            if event == "FighterRebuilt" and closeWhenPopped and not firstRun:
                time.sleep(3)
                pydirectinput.press("3")
                time.sleep(0.1)
                pydirectinput.press("space")
                time.sleep(0.1)
                pydirectinput.press("space")
                time.sleep(2)
                pydirectinput.press("d")
                time.sleep(0.1)
                pydirectinput.press("space")
                time.sleep(0.1)
                pydirectinput.press("d")
                time.sleep(0.1)
                pydirectinput.press("space")
                time.sleep(0.1)
                pydirectinput.press("3")


            if event == "ShieldState" and not firstRun:
                state = line.split(':')[5].split(' ')[0].strip()

                if state == "false":
                    print("Shields down")
                    if closeWhenPopped:
                        pydirectinput.press("escape")
                        time.sleep(1)
                        pydirectinput.press("w")
                        time.sleep(0.1)
                        pydirectinput.press("space")
                        time.sleep(16)
                        pydirectinput.press("space")
                        messagebox.showwarning("Game closed", "Your shields were taken down so the game was closed.")
                    else:
                        messagebox.showwarning("Shields down", "Your ship's shields have been taken down - be careful!")




            if event == "HullDamage" and not firstRun:
                if line.split(':')[7].split(' ')[0] == "false":
                    print("Hull: " + line.split(':')[5].split(',')[0])

        lastJournalText = journalText
    firstRun = False


def main():
    root = Tk()
    root.title("AFKHelper")
    root.withdraw()

    load_settings()
    print("Initialising...")
    process_journal()
    while True:
        print("Checking journal...")
        process_journal()
        time.sleep(20)


if __name__ == '__main__':
    main()
