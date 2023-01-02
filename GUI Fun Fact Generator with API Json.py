#Import the Llibrary 
import json
import requests 
from tkinter import *

#Tkinter interface
window = Tk()
window.title("Fun Fact Generator")
window.geometry('1000x90')

#API functions and functions the GUI interface
def get_fun_fact():
    url ="https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    useless_fact = data['text']
    lbl.configure(text=useless_fact)

btn = Button(window,text='Click Me Now!', command=get_fun_fact)
btn.pack()

lbl = Label(window, text='Click the button to get a random Facts in the World')
lbl.pack()

window.mainloop()