from datetime import datetime 
from tkinter import *
import requests

dt=datetime.now()
root=Tk()
root.title("Sunshine")

icon=PhotoImage(file='sun.png')
root.tk.call('wm','iconphoto',root._w,icon)

frame1 = Frame(root)
frame1.grid(row=0,column=0)

L=Label(frame1,text="City")
L.configure(font='None 20 ')
L.grid(row=0,column=0,sticky="E")

userE=Entry(frame1)
userE.configure(width=20)
userE.grid(row=0,column=1,sticky="w",padx=10)
userE.focus()

def fun():
    frame2 = Frame(root)
    frame2.grid(row=1,column=0)
    try:
        text=userE.get()
        api="http://api.openweathermap.org/data/2.5/weather?appid=1188b9f9148675e6007f8dba06208427&q="
        url=api+text
        json=requests.get(url).json()
        
        l1=Label(frame2,text=text)
        l1.configure(font="None 22")
        l1.grid(row=4,columnspan=3,)
    
        l2=Label(frame2,text=dt.strftime("%d-%m-%y"))
        l2.configure(font="None 22 bold")
        l2.grid(row=5,columnspan=3)

        l3=Label(frame2,text="Rain")
        l3.configure(font="None 18 bold",anchor="center")
        l3.grid(row=6,column=0)

        l4=Label(frame2,text="Temperature:")
        l4.grid(row=8,column=0)
        l4.configure(font="None 12 bold")

        l5=Label(frame2,text="Preessure")
        l5.grid(row=10,column=0)
        l5.configure(font="None 12")

        l6=Label(frame2,text="Humidity")
        l6.grid(row=11,column=0)
        l6.configure(font="None 12")

        l7=Label(frame2,text="Wind Speed")
        l7.grid(row=12,column=0)
        l7.configure(font="None 12")

        l8=Label(frame2,text="Wind Direction")
        l8.grid(row=13,column=0)
        l8.configure(font="None 12")
    
        l9=Label(frame2,text="Cloudness")
        l9.grid(row=14,column=0)
        l9.configure(font="None 12")

        l10=Label(frame2,text="Rain")
        l10.grid(row=15,column=0)
        l10.configure(font="None 12")

        
        data10=json['weather'][0]['description']
        label10=Label(frame2,text=data10)
        label10.configure(font="None 10 bold")
        label10.grid(row=6,column=1)
    
        data7=json['main']['temp_min']
        X=(data7-273.15)
        label7=Label(frame2,text="Maximum: %.2f \u2103" %X).grid(row=8,column=1)

        data8=json['main']['temp_max']
        Y=(data8-273.15)
        label8=Label(frame2,text="Minimum: %.2f \u2103" %Y).grid(row=9,column=1)

        data9=json['main']['temp']
        Z=(data9-273.15)
        label9=Label(frame2,text="%.2f \u2103"% Z).grid(row=9,column=0)

        data=json['main']['pressure']
        label=Label(frame2,text="{} hPa".format(data)).grid(row=10,column=1)

        data2=json['main']['humidity']
        label2=Label(frame2,text="{} %".format(data2)).grid(row=11,column=1)

        data3=json['wind']['speed']
        labe3=Label(frame2,text="{} M/S".format(data3)).grid(row=12,column=1)

        data4=json['wind']['deg']
        label4=Label(frame2,text="{} Degree".format(data4)).grid(row=13,column=1)

        data5=json['clouds']['all']
        label5=Label(frame2,text="{} %".format(data5)).grid(row=14,column=1)
        try:
            data6=json['rain']['3h']
            label6=Label(frame2,text="{} MM".format(data6)).grid(row=15,column=1)
        except KeyError:
            label6=Label(frame2,text="No Rain").grid(row=15,column=1)

        but1=Button(frame2,text="Previous")
        but1.configure(font='Times 15',width=10)
        but1.grid(row=17,column=0,sticky=E)

        but2=Button(frame2,text="Next")
        but2.configure(font='Times 15',width=10)
        but2.grid(row=17,column=1)

    except:
        label17=Label(frame2,text="City Not Found")
        label17.configure(font="None 20 bold")
        label17.grid(row=4,column=0)

    
submitB=Button(frame1,text="Show Wheather",command=fun)
submitB.configure(font='Times 12',width=12)
submitB.grid(row=2,columnspan=3)

root.resizable(False,False)
root.mainloop()

