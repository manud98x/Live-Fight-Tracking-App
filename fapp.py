import tkinter as tk
from tkinter import font
import requests 
import json


HEIGHT= 750
WIDTH=600

#flight_iata':QK8512'
    
        

def get_flight(code,date):
    
  try:  
      key = '28ee04abad6baa334bfa2b8638f610a2'
      url = 'http://api.aviationstack.com/v1/flights'
      params ={'access_key': key,'flight_iata':code,'airline_name':date}    
      response = requests.get(url,params=params)


      'f_dict=response.json()''
  
      print(f_dict['data'])

      lbldepdata['text'] = (f_dict['data'][1]['departure']['airport'])
      lblarridata['text'] = (f_dict['data'][1]['arrival']['airport'])
      lblnodata['text'] = (f_dict['data'][1]['flight']['iata']) 
      lblIATADataD['text'] = (f_dict['data'][1]['departure']['iata']) 
      lblIATADataA['text'] = (f_dict['data'][1]['arrival']['iata']) 
      lblgateDataD['text'] = (f_dict['data'][1]['departure']['gate']) 
      lblgateDataA['text'] = (f_dict['data'][1]['arrival']['gate']) 

  except:

      lblnodata['text'] = str("Not Available")
      lbldepdata.config(text="")
      lblarridata.config(text="")
      lblIATADataD.config(text="")
      lblIATADataA.config(text="")
      lblgateDataD.config(text="")
      lblgateDataA.config(text="")

     


  #DL1108 2020-05-10 TV9807'






root=tk.Tk()
root.title("Flight App")
root.resizable(False, False)

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

bg_image = tk.PhotoImage(file="fg.png")
bg_label = tk.Label(root,image=bg_image)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

frame = tk.Frame(root,bg="#b3cccc",bd=5)
frame.place(relx=0.5,rely=0.02,relwidth=0.65,relheight=0.2,anchor="n")

entry = tk.Entry(frame,font="40" )
entry.grid(column=1, row=0,padx=10, pady=10)

lbl1 = tk.Label(frame,text="Flight Number",bg='#b3cccc')
lbl1.grid(column=3, row=0,padx=10, pady=10)
lbl1.config(font=("Courier",10,'bold'))

entry2 = tk.Entry(frame,font="40")
entry2.grid(column=1, row=4)

lbl2 = tk.Label(frame,text="AirLine",bg='#b3cccc',justify='left')
lbl2.grid(column=3, row=4,padx=10, pady=10)
lbl2.config(font=("Courier",10,'bold'))


button = tk.Button(frame,text="Get Details",bg="#6699ff",fg='black',font="15",command= lambda:get_flight(entry.get(),entry2.get()))
button.place(height=30, width=110,relx=0.38,rely=.68)
button.config(font=("Courier",10,'bold'))


lframe = tk.Frame(root,bg="#6699ff",bd=10)
lframe.place(relx=0.5,rely=0.25,relwidth=0.9,relheight=0.6,anchor="n")

######################################################################

lbldepdata = tk.Label(lframe,bg='white')
lbldepdata.place(height=30, width=150,relx=0.05,rely=.2)
lbldepdata.config(font=("Courier",11))

lbldep = tk.Label(lframe,text="Depature",bg='#6699ff')
lbldep.place(height=30, width=110,relx=0.085,rely=.28)
lbldep.config(font=("Courier",10,'bold'))


######################################################################

lblnodata = tk.Label(lframe,bg='white')
lblnodata.place(height=30, width=120,relx=0.4,rely=.07)
lblnodata.config(font=("Courier",11))

lblno = tk.Label(lframe,bg='#6699ff',text="Flight Number")
lblno.place(height=30, width=110,relx=0.415,rely=.15)
lblno.config(font=("Courier",10,'bold'))


######################################################################

lblarridata = tk.Label(lframe,bg='white')
lblarridata.place(height=30, width=150,relx=0.68,rely=.2)
lblarridata.config(font=("Courier",11))

lblarri = tk.Label(lframe,text="Arrival",bg='#6699ff')
lblarri.place(height=30, width=110,relx=0.725,rely=.28)
lblarri.config(font=("Courier",10,'bold'))

######################################################################

lblIATADataD = tk.Label(lframe,bg='white')
lblIATADataD.place(height=30, width=110,relx=0.085,rely=.420)
lblIATADataD.config(font=("Courier",11))

lblIATAD = tk.Label(lframe,text="IATA",bg='#6699ff')
lblIATAD.place(height=30, width=110,relx=0.085,rely=.5)
lblIATAD.config(font=("Courier",10,'bold'))


######################################################################


lblIATADataA = tk.Label(lframe,bg='white')
lblIATADataA.place(height=30, width=110,relx=0.725,rely=.420)
lblIATADataA.config(font=("Courier",11))

lblIATAA = tk.Label(lframe,text="IATA",bg='#6699ff')
lblIATAA.place(height=30, width=110,relx=0.725,rely=.5)
lblIATAA.config(font=("Courier",10,'bold'))
######################################################################

lblgateDataD = tk.Label(lframe,bg='white')
lblgateDataD.place(height=30, width=110,relx=0.085,rely=.6)
lblgateDataD.config(font=("Courier",11))

lblgateD = tk.Label(lframe,text="Gate",bg='#6699ff')
lblgateD.place(height=30, width=110,relx=0.085,rely=.68)
lblgateD.config(font=("Courier",10,'bold'))

######################################################################

lblgateDataA = tk.Label(lframe,bg='white')
lblgateDataA.place(height=30, width=110,relx=.725,rely=.6)
lblgateDataA.config(font=("Courier",11))

lblgateA = tk.Label(lframe,text="Gate",bg='#6699ff')
lblgateA.place(height=30, width=110,relx=0.725,rely=.68)
lblgateA.config(font=("Courier",10,'bold'))






root.mainloop()


