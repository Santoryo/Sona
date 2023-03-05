import win32gui
import win32api
import psutil
import win32process
import os

###Virtual-KeyCodes###
Media_Next = 0xB0
Media_Previous = 0xB1
Media_Pause = 0xB3 ##Play/Pause
Media_Mute = 0xAD



###SpotifyInfo###
def getwindow(Title="TidalMainWindow"):
	window_id = win32gui.FindWindow(Title, None)
	return window_id


###SpotifyInfoForUwpVersion###
def getwindow_uwp(hwnd, hwnds):
		song_info= win32gui.GetWindowText(hwnd)
		if win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_1" and len(song_info) > 0:
			pid = win32process.GetWindowThreadProcessId(hwnd)
			for e in pid:
				try:
					proc_name = psutil.Process(int(e)).name()
					if(proc_name == "TIDAL.exe"):
						hwnds.append(song_info)
				except:
					pass


def song_info():
	try:
		song_info = win32gui.GetWindowText(getwindow())
		if len(song_info) == 0:
			hwnds = []
			win32gui.EnumWindows(getwindow_uwp, hwnds)
			song_info = hwnds[0]
	except:
		pass
	return song_info

def artist():
	try:
		temp = song_info()
		song, artist = temp.split(" - ",1)
		artist = artist.split(",", 1)
		artist = artist[0]
		artist = artist.strip()
		return artist
	except:
		return "There is nothing playing at this moment"
	
def song():
	try:
		temp = song_info()
		song, artist = temp.split(" - ",1)
		song = song.strip()
		return song
	except:
		return "There is nothing playing at this moment"

	
###SpotifyBlock###
def createfolder(folder_path="C:\SpotiBlock"):
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)
	else:
		pass
	
def createfile(file_path="C:\SpotiBlock\Block.txt" ):
	if not os.path.exists(file_path):
		file = open(file_path, "a")
		file.write("ThisFirstLineWillBeIgnoredButIsNecessaryForUse")

def blocklist(file_path="C:\SpotiBlock\Block.txt"):
	block_list = []
	for line in open(file_path, "r"):
		if not line == "":
			block_list.append(line.strip())
	return block_list
	
def add_to_blocklist(file_path="C:\SpotiBlock\Block.txt"):
	with open(file_path, 'a') as text_file:
		text_file.write("\n" + song_info())
		
def reset_blocklist(file_path="C:\SpotiBlock\Block.txt"):
	with open(file_path, 'w') as text_file:
		text_file.write("ThisFirstLineWillBeIgnored")
		pass
	
	

	
###Media Controls###
def hwcode(Media):
	hwcode = win32api.MapVirtualKey(Media, 0)
	return hwcode

def next():
	win32api.keybd_event(Media_Next, hwcode(Media_Next))
	
def previous():
	win32api.keybd_event(Media_Previous, hwcode(Media_Previous))
	
def pause():
	win32api.keybd_event(Media_Pause, hwcode(Media_Pause))
	
def play():
	win32api.keybd_event(Media_Pause, hwcode(Media_Pause))
	
def mute():
	win32api.keybd_event(Media_Mute, hwcode(Media_Mute))
	
	
