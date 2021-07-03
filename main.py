import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

#------------------------------PULL PASSWORD------------------------------------- #

def pull():
    web_get=web_entry.get()
    try:
        with open('Data.json', 'r') as data:
            data_dict = json.load(data)
    except FileNotFoundError:
        messagebox.showwarning('Error', 'List is Empty')
    except KeyError:
        messagebox.showwarning('Error', f"No Password for {web_get}")
    else:
        pass_chosen = data_dict[web_get]['Password']
        messagebox.showwarning(f"for {web_get.title()} password is:", {pass_chosen})
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    pass_entry.delete(0, 'end')
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))] + \
                     [random.choice(numbers) for _ in range(random.randint(2, 4))] + \
                    [random.choice(symbols) for _ in range(random.randint(2, 4))]


    random.shuffle(password_list)

    pass_list= ''
    for char in password_list:
        pass_list += char

    final_list = "".join(pass_list)
    print(final_list)

    pass_entry.insert(0, final_list)
    pyperclip.copy(final_list)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    web_get = web_entry.get()
    email_get = email_entry.get()
    pass_get = pass_entry.get()
    new_data = {web_get: {'e-mail': email_get, 'Password': pass_get
                         }
                }

    if len(web_get) == 0 or len(email_get) == 0 or len(pass_get) == 0:
        messagebox.showwarning(title='Error', message="You haven't gave details")
    else:

        if_is_ok = messagebox.askokcancel(title=f"{web_get}", message=f"This are the details you entered:\n{email_get}\n{pass_get}\n"
                                                       f"is it ok to save?")
        if if_is_ok:
            try:
                with open('Data.json', "r") as data:
                    data_dict = json.load(data)

            except FileNotFoundError:
                with open('Data.json', 'w') as data:
                    json.dump(new_data, data, indent=4)
            else:
                data_dict.update(new_data)
                with open('Data.json','w') as data:
                    json.dump(data_dict, data, indent=4)

    web_entry.delete(0, 'end')
    pass_entry.delete(0, 'end')
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('My Password')
window.config(padx=50, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=220, height=200, bg=YELLOW, highlightthickness=0)
pass_img =tk.PhotoImage(file='/home/tamar-alter/PycharmProjects/High/my_pass/logo.png')
canvas.create_image(120, 100, image=pass_img)
canvas.grid(column=1, row=0)

web_label = tk.Label(text='Website:', bg=YELLOW)
web_label.grid(column=0, row=1)
web_entry = tk.Entry(width=22)
web_entry.grid(column=1, row=1)
web_entry.focus()
email_label = tk.Label(text='E-mail/Username:', bg=YELLOW)
email_label.grid(column=0, row=2)
email_entry = tk.Entry(width=36)
email_entry.grid(column=1, row=2,columnspan=2)
email_entry.insert(0,'Yaniv.Ayalon@gmail.com')
pass_label = tk.Label(text='Password:', bg=YELLOW)
pass_label.grid(column=0, row=3)

pass_entry = tk.Entry(width=24)
pass_entry.grid(column=1 ,row=3)

generate_button = tk.Button(text='Generate',width=8, bg=PINK, command=generate)
generate_button.grid(column=2, row=3, columnspan=2)

add_button = tk.Button(text='Add', width=36, bg=PINK, command=save)
add_button.grid(column=1, row=4, columnspan=2)

request_button = tk.Button(text='Request', width=14, bg=PINK, command=pull)
request_button.grid(column=2, row=1, columnspan=2)

window.mainloop()