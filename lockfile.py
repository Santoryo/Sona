import configparser

config = configparser.ConfigParser()

async def getCredentials():
    config.read('config.ini', encoding='utf-8')
    try:
        lockfile = open(f'{str(config["SETTINGS"]["LeaguePath"])}\lockfile', "r")
        lockfile = lockfile.read().split(":")

    except OSError:
        lockfile = []


    return lockfile