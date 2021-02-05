import time
from tkinter import *
import pyautogui
import json
import constants
import pytesseract
from PIL import ImageGrab
from pytesseract import Output
import sqlite3
import configparser

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#moving mouse to message icon and clicking

# pyautogui.moveTo(1997, 35, 2)
# pyautogui.click()
# time.sleep(2)

#Taking sss of only message box
snapshot = ImageGrab.grab(constants.mbox)
save_path = "C:\\Users\\cihan.akinci\\Desktop\\MySnapshot.png"
snapshot.save(save_path)


scdict = pytesseract.image_to_data(save_path, lang=None, config='', nice=0, output_type=Output.DICT, timeout=0, pandas_config=None)

scdict.pop("level")
scdict.pop("page_num")
scdict.pop("block_num")
scdict.pop("par_num")
scdict.pop("line_num")
scdict.pop("word_num")
scdict.pop("left")
scdict.pop("top")
scdict.pop("width")
scdict.pop("height")
scdict.pop("conf")

for x in list(scdict.keys()):
    if scdict[x] == [] or scdict[x] == ' ':
        del scdict[x]
json.dumps(scdict)
print(json.dumps(scdict))
#
# for var in constants.msgcoordinates:
#     pyautogui.moveTo(var[0],var[1],var[2])


config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45', 'Compression': 'yes', 'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hgfdsfa'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)

def printRecords():
    connection = sqlite3.connect('your_DB_name')
    cur = connection.cursor()
    cur.execute("select column_name  from table_name where  book_name = ?", (z.get(),))
    connection.commit()
    variablename = cur.fetchall()
    print (variablename)

root = Tk()
root.title ( "Search a Book")

z= StringVar()

#Label
Label(root, text = "Enter the name of the book you are searching for:      ").grid()
#Textbox
bookSearchEntry = Entry(root, textvariable = z)
bookSearchEntry.grid(row = 0, column = 1)
#Button
bookSearchButton = Button(root, text = "Search", command = printRecords)
bookSearchButton.grid(row = 0, column = 2)

root.mainloop()
