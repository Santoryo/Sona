import spotilib
import asyncio

import lcuwrapper
import sys

import atexit

import configparser
import readchar

config = configparser.ConfigParser()

import os
from os import system

from simple_colors import *

import win32api

state = True



async def originalStatus():
    isRunning = False
    try:
        while isRunning == False:
            ogStatus = await lcuwrapper.lcuCall("GET", "/lol-chat/v1/me")
            if(ogStatus[0] != 200):
                config.read('config.ini', encoding='utf-8')
                os.system('cls')
                print(red('League Client is not running'))
                print(f'The League of Legends installation you setup is: {config["SETTINGS"]["LeaguePath"]}')
                print('Make sure you set the correct path to League Installation or run League of Legends if not running yet')
                print('')
                await asyncio.sleep(10)
            else:
                isRunning = True
    except:
        sys.exit()

    return ogStatus

ogStatus = asyncio.run(originalStatus())


def exit_handler():
    print("leaving")
    asyncio.run(lcuwrapper.lcuCall("PUT", "/lol-chat/v1/me", f"{ogStatus[1]}"))
    sys.exit()

win32api.SetConsoleCtrlHandler(exit_handler, True)

async def main(state):
    system("title " + "Sona")
    atexit.register(exit_handler)
    _song = ""
    _artist = ""

    wasPaused = False

    while state:
        config.read('config.ini', encoding='utf-8')
        artist = spotilib.artist()
        song = spotilib.song()
        message = ""


        isLcuRunning = await lcuwrapper.lcuCall("GET", "/lol-chat/v1/me")

        if isLcuRunning[0] == 200:
            if (song != "There is nothing playing at this moment" and (song != _song or wasPaused == True)):
                message = blue("Song has changed, updating LCU status")
                wasPaused = False
                _song = song
                _artist = artist

                try:
                    await lcuwrapper.lcuCall("PUT", "/lol-chat/v1/me", str(config['SETTINGS']['format']).format(song = _song, artist = _artist))
                except:
                    message = red('[ERROR] Song cant be updated, probably due to lockfile eror')

            elif(song == "There is nothing playing at this moment" and _song):
                wasPaused = True
                if(config['SETTINGS']['onMusicStopReverseStatus'] == "False"):
                    status = str(config['SETTINGS']['formatStop']).format(song = _song, artist = _artist)
                    message = blue("Song has been paused/stopped")
                else:
                    status = ogStatus[1]

                try:
                    await lcuwrapper.lcuCall("PUT", "/lol-chat/v1/me", f"{status}")
                except:
                    message = red('[ERROR] Song cant be updated, probably due to lockfile eror')

            #else:
                #print("The song is still the same")

        else:
            message = red("League Client is not running")

        await showOnScreen(song, artist, message)
        await asyncio.sleep(int(config['SETTINGS']['updateTime']))
    




async def showOnScreen(artist, song, message):
    if(song != "There is nothing playing at this moment"):
        os.system('cls')
        print(f'Now playing: {green(artist)} - {green(song)}')
        print(f'If you wish to close the app and revert to original status, exit with CTRL+C')
        print(message)
    else:
        os.system('cls')
        print("Nothing is being played at the moment.")
        print(f'If you wish to close the app and revert to original status, exit with {cyan("CTRL+C", "underlined")}')


asyncio.run(main(True))
