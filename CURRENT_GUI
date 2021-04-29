from tkinter import *
import tkinter as tk
import requests

root=Tk()
root.geometry('500x500')
root.title("CURRENCY GUI")


to=tk.StringVar()
from1=tk.StringVar()
response1=tk.StringVar()
amount=tk.StringVar()





#Label
label1=Label(root,text="Which Currency do you want to convert to:")
label1.place(x=0,y=10)

label2=Label(root,text="Which Currency do you want to convert from:")
label2.place(x=0,y=50)

label4=Label(root,text="What amount do you want to convert:")
label4.place(x=0,y=90)




#Entry_Widget

e1=Entry(root,width=10,borderwidth=3,textvariable=to)
e1.place(x=250,y=10)

e2=Entry(root,width=10,borderwidth=3,textvariable=from1)
e2.place(x=250,y=50)

e3=Entry(root,width=10,borderwidth=3,textvariable=amount)
e3.place(x=250,y=90)



url = "https://currency-exchange.p.rapidapi.com/exchange"



headers = {
    'x-rapidapi-key': "API-KEY",
    'x-rapidapi-host': "currency-exchange.p.rapidapi.com"
    }




def submit():
    to1 = to.get()
    from2 = from1.get()
    amount1=amount.get()

    amountFLOAT=(float)(amount1)

    querystring = {"to": to1, "from": from2, "q": "1.0"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    response1=response.text

    responseFLOAT=(float)(response1)

    ans=responseFLOAT*amountFLOAT
    ansSTR=(str)(ans)

    label3=Label(root,text="CONVERSION RATE: "+response1,borderwidth=6,width=29,bg='cyan')
    label3.place(x=125,y=250)

    label5=Label(root,text="Your amount after conversion : "+ansSTR,borderwidth=6,width=29)
    label5.place(x=125, y=300)



sub_btn=tk.Button(root,text = 'Submit', command = submit)
sub_btn.place(x=135,y=150)







root.mainloop()
