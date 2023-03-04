# Sona
Sona takes your Spotify current song and displays it as your League status.


## Setup
1. To use Sona out of the box you can download it from [Releases](https://github.com/Santoryo/Sona/releases)
2. Sona uses lockfile to connect to [LCU API](https://hextechdocs.dev/getting-started-with-the-lcu-api/), the default installation for League of Legends is for `C:\Riot Games\League of Legends` if you have League installed in other place, please edit `config.ini` to your matching League of Legends installation

## Customization
You might want to customize your status a little bit, it is possible with `config.ini` that is located in the installation directory.
``` ini
[SETTINGS]
format =  ▶️ {artist} - {song} #format of the song, use wildcards {artist} or {song} to display the info respectively.
onMusicStopReverseStatus = False #if its True then it will reverse to original status that you had setup before turning on Sona.
formatStop = ⏸️ {artist} - {song} #if onMusicStopReverseStatus = False then formatStop is taken into the accountant
updateTime = 1 #update time of statusMessage, 1-3 seconds are recommended
LeaguePath = C:\Riot Games\League of Legends #League of Legends installation folder
```



Sona isn't endorsed by Riot Games and doesn't reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc.
