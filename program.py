import ast
import random
from tkinter import *
g = open('songlist.txt', 'r')
with g as document:
    for line in document:
        songlist = line
    g.close()

songlist = ast.literal_eval(songlist) #convert dictionary in the form of string to dictionary

def addartist():
	addartistroot = Tk()
	artist = StringVar()
	artistEntry = Entry(textvariable = artist)
	artistEntry.pack()
	artist = str(artist)
	artist = artist.replace(" ","")
	artist = artist.lower()
	print(artist)
	addartistroot.mainloop()
	if artist in songlist:
		print('The artist already exists in our database. You might want to add songs for your chosen artist. Please type Q to quit.')
		prompt = input('Type Q: ')
		prompt = prompt.lower()
		if prompt == 'q':
			quit()
		while prompt != 'q':
			print('Wrong command. Type Q to quit.')
			prompt = input('Type Q: ')
			prompt.lower()
			if prompt == 'q':
				quit()
	tries = int(input('Number of Songs to add: ')) #number of times someone will add a new song
	for song in range(tries):
			artistsong = input('Name of Song'+' '+str(song+1)+': ')
			artistsong = artistsong.split(',')
			songlist.update({artist:artistsong})
	f = open('songlist.txt','w+')
	f.write(str(songlist))
	f.close()
def searchsongs():
	search = input('Type Name of Artist: ')
	search = search.replace(" ","")
	search = search.lower()
	if search in songlist:
		song_artist = songlist[search]
		def printing():
			for composition in songlist[search]:
				print(composition)
		print('Song(s): ', end = '')
		printing()
	else:
		print('We currently have no record regarding this artist. Please type Q to quit and open the program again to add a record to that artist.')
		prompt = input('Type Q: ')
		prompt = prompt.lower()
		if prompt == 'q':
			quit()
		while prompt != 'q':
			print('Wrong command. Type Q to quit.')
			prompt = input('Type Q: ')
			prompt.lower()
			if prompt == 'q':
				quit()

def addsongs():
	artist = input('Type Name of Artist: ')
	artist = artist.replace(" ","")
	artist = artist.lower()
	if artist in songlist:
		tries = int(input('Number of Songs to Add: ')) #number of songs to add
		for song in range(tries):
			print('Type the name of the song. Only one song at a time is allowed.')
			newsong = input('Song'+' '+str(song+1)+': ')
			listofartistsong = songlist[artist]
			if newsong not in listofartistsong:
				listofartistsong.append(newsong)
			songlist.pop(artist)
			songlist.update({artist:listofartistsong})
			f = open('songlist.txt','w+')
			f.write(str(songlist))
			f.close()
	else:
		print('We currently have no record regarding this artist. Please type Q to quit and open the program again to add a record to that artist.')
		prompt = input('Type Q: ')
		prompt = prompt.lower()
		if prompt == 'q':
			quit()
		while prompt != 'q':
			print('Wrong command. Type Q to quit.')
			prompt = input('Type Q: ')
			if prompt == 'q':
				quit()

def randomizer():
	artist = input('Name of Artist: ')
	artist = artist.replace(" ","")
	artist = artist.lower()
	if artist in songlist:
		song = random.choice(songlist[artist])
		print(song)
	else:
		print('We currently have no record regarding this artist. Please type Q to quit and open the program again to add a record to that artist.')
		prompt = input('Type Q: ')
		prompt = prompt.lower()
		if prompt == 'q':
			quit()
		while prompt != 'q':
			print('Wrong command. Type Q to quit.')
			prompt = input('Type Q: ')
			prompt.lower()
			if prompt == 'q':
				quit()


#Source Codes:
#https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
#https://www.guru99.com/python-dictionary-beginners-tutorial.html#3
#https://stackoverflow.com/questions/4803999/how-to-convert-a-file-into-a-dictionary
#https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#https://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-file