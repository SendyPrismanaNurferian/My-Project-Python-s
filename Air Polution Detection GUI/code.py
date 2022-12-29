from tkinter import*
import requests
from bs4 import BeautifulSoup

#links to extract html data
def getdata(url):
    r=requests.get(url)
    return r.text

def airinfo():
    htmldata = getdata("") #You can copy links in here from weather and pass the URL into get data function and covert that data into HTML Code
    soup = BeautifulSoup(htmldata, 'html.parser') 
    res_data = soup.find(class_="").text #Traverse the air quality
    air_data = soup.find_all(class_="") #traverse the content
    air_data =[data.text for data in air_data]

    ar.set(res_data)
    o3.set(air_data[0])
    no2.set(air_data[1])
    so2.set(air_data[2])
    pm.set(air_data[3])
    pml.set(air_data[4])
    co.set(air_data[5])
    res = int(res_data)
#this parameter is used image in my folders and is from geeksforgeeks.com
    if res <= 50:
        remark = "Good"
        impact = "Minimum Impact"
    elif res <= 100 and res > 51:
        remark = "Satisfactory Air"
        impact = "Minor breathing discomfort to sensitive persons"
    elif res <= 200 and res >= 101:
        remark = "Moderate"
        impact = "Breathing discomfort to the persons with lungs, asthma and heart diseases"
    elif res <= 400 and res >= 201:
        remark = "Very Poor"
        impact = "Breathing discomfort to most persons on prolonged exposure"
    elif res <= 500 and res >= 401:
        remark = "Dangerous"
        impact = "Affects healthy people and seriously impacts those with existing diseases"
    res_remark.set(remark)
    res_imp.set(impact)

# the object of tkinter and make background set to grey color
master = Tk()
master.configure(bg='lightgrey')
#variable for Classes in tkinter
air_data = StringVar()
ar = StringVar()
o3 = StringVar()
no2 = StringVar()
so2 = StringVar()
pm = StringVar()
pml = StringVar()
co = StringVar()
res_remark = StringVar()
res_imp = StringVar()

# Creating label for each information and the name using widget label
Label(master, text="Air Quality : ",
      bg="light grey").grid(row=0, sticky=W)
Label(master, text="O3 (μg/m3) :", 
      bg="light grey").grid(row=1, sticky=W)
Label(master, text="NO2 (μg/m3) :", 
      bg="light grey").grid(row=2, sticky=W)
Label(master, text="SO2 (μg/m3) :", 
      bg="light grey").grid(row=3, sticky=W)
Label(master, text="PM2.5 (μg/m3) :", 
      bg="light grey").grid(row=4, sticky=W)
Label(master, text="PM10 (μg/m3) :",
      bg="light grey").grid(row=5, sticky=W)
Label(master, text="CO (μg/m3) :", 
      bg="light grey").grid(row=6, sticky=W)
Label(master, text="Remark :", 
      bg="light grey").grid(row=7, sticky=W)
Label(master, text="Possible Health Impacts :",
      bg="light grey").grid(row=8, sticky=W)

# Creating label for class variable and thr name using widget Entry
Label(master, text="", textvariable=ar,
      bg="light grey").grid(
    row=0, column=1, sticky=W)
Label(master, text="", textvariable=o3, 
      bg="light grey").grid(
    row=1, column=1, sticky=W)
Label(master, text="", textvariable=no2,
      bg="light grey").grid(
    row=2, column=1, sticky=W)
Label(master, text="", textvariable=so2,
      bg="light grey").grid(
    row=3, column=1, sticky=W)
Label(master, text="", textvariable=pm, 
      bg="light grey").grid(
    row=4, column=1, sticky=W)
Label(master, text="", textvariable=pml, 
      bg="light grey").grid(
    row=5, column=1, sticky=W)
Label(master, text="", textvariable=co, 
      bg="light grey").grid(
    row=6, column=1, sticky=W)
Label(master, text="", textvariable=res_remark,
      bg="light grey").grid(row=7, column=1, sticky=W)
Label(master, text="", textvariable=res_imp,
      bg="light grey").grid(row=8, column=1, sticky=W)
 
 # created a button using the widget
b = Button(master, text="Check", command=airinfo, bg="Red")
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)
mainloop()