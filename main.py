from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    passwordentry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    passwordentry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
  website=ws_entry.get()
  email=email_entry.get()
  passcode=passwordentry.get()

  new_data={
    website:{
      "email":email,
      "password":passcode
    }
  }
  
  if len(email)==0 or len(website)==0 or len(passcode)==0:
    messagebox.showinfo(title="Oops",message="You've let some field(s) empty")
  else:
    is_ok=messagebox.askokcancel(title="Confirmation",message=f"These are the details you've entered:\nWebsite: {website}\nEmail: {email}\nPassword: {passcode}")
    if is_ok:
      try:
        with open("data.json",'r') as data_file:
          data=json.load(data_file)
          data.update(new_data)
      except FileNotFoundError:
        with open("data.json",'w') as data_file:
          json.dump(new_data,data_file,indent=4)
      else:
        with open("data.json",'w') as data_file:
          json.dump(data,data_file,indent=4)
      finally:
        ws_entry.delete(0,END)
        passwordentry.delete(0,END)

# ---------------------------- DATA SEARCH ------------------------------- #
def find_password():
  search=ws_entry.get()
  try:
    with open("data.json",'r') as datafile:
      data=json.load(datafile)
  except FileNotFoundError:
    messagebox.showinfo(title="Error",message="No data file found")
  else:
    if search in data:
      cred=data[search]
      messagebox.showinfo(title="Credentials",message=f"Email: {cred['email']}\nPassword: {cred['password']}")
    else:
      messagebox.showinfo(title="Error",message=f"No details for {search} is found.")



    

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pasword Manager")
window.config(padx=50,pady=50,bg="white")
canvas=Canvas(height=200,width=370,bg="white",highlightthickness=0)
logo=PhotoImage(file="logo.png")


canvas.create_image(170,100,image=logo)
canvas.grid(row=0,column=1)


ws_label=Label(text="Website:",bg="white")
ws_label.grid(row=1,column=0)
ws_entry=Entry(width=35)
ws_entry.grid(row=1,column=1,columnspan=2)
ws_entry.focus()

email_label=Label(text="Email/Username:",bg="white")
email_label.grid(row=2,column=0)
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
#email_entry.insert(0,"xyz@mail.com")
'''
uncomment the above line if you are going to use the same mail for the every
webisites ,app or accounts.
P.S: You can change the email/username anytime during the execution.
'''


passwordlabel=Label(text="Password:",bg="white")
passwordlabel.grid(row=3,column=0)
passwordentry=Entry(width=35)
passwordentry.grid(row=3,column=1,columnspan=2)


gen_pass=Button(text="Generate Password",width=30,command=generate_password)
gen_pass.grid(row=4,column=1,columnspan=2)

add_btn=Button(text="Add",width=30,command=save)
add_btn.grid(row=5,column=1,columnspan=2)

search_btn=Button(text="Search",width=30,command=find_password)
search_btn.grid(row=6,column=1,columnspan=2)





window.mainloop()


