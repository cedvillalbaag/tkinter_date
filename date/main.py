from tkinter import *
from datetime import date

root = Tk()
root.title("Dates - Python")
root.geometry("750x350")
root.iconbitmap('year.ico')
root.configure(bg='#454545')


panic = Label(root, text= "Don´t Panic!!", font = ("Courier", 28, 'bold'), bg='#454545', fg='#FF6000')
panic.pack(pady= 20, ipadx= 10, ipady= 10)

#Get date
today = date.today()
#format date
f_today= today.strftime("%A , %d - %B - %Y")

#Output date
today_label = Label(root, text= f'Today is: {f_today}', font=("Courier", 22), bg='#454545', fg='#FF6000')
today_label.pack(pady=20)

# Countdown
days_in_year = 365
today_is_number = int(today.strftime("%j"))
countdown = days_in_year- today_is_number

countdown_label = Label(root, text= f'There are only {countdown} days \n left in this year!!!', font=("Courier", 22), bg='#454545', fg='#FF6000')
countdown_label.pack(pady= 10)

root.mainloop()

