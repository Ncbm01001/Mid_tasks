#написать игру Камень-Ножницы-Бумага

import tkinter as tk
import random

root = tk.Tk ()
root.title("Камень/Ножницы/Бумага")
root.geometry("500x300+600+180")
global you_check
you_check = tk.StringVar()
you_check.set ("0")
you_check_t = tk.Label(root, text="Ваш счет - ")
you_check_t.grid(row=4,column=4)
you_check_t2 = tk.Label(root, textvariable = you_check)
you_check_t2.grid(row=4,column=5)

global enemy_check
enemy_check = tk.StringVar()
enemy_check.set ("0")
enemy_check_t = tk.Label(root, text="Счет противника -")
enemy_check_t.grid(row=4,column=6)
enemy_check_t2 = tk.Label(root, textvariable=enemy_check)
enemy_check_t2.grid(row=4,column=7)

def rock_ch():
    enemy_weapon = ["rock","paper","scissors"]
    enemy_choice = random.choice(enemy_weapon)
    if enemy_choice == "paper":
        lose = tk.Label(root, text="Вы проиграли!")
        lose.grid(row=8,column=12)
        current_score = int(enemy_check.get())
        enemy_check.set(str(current_score + 1))
    elif enemy_choice == "scissors":
        win = tk.Label(root, text="Вы выграли!")
        win.grid(row=8,column=12)
        current_score = int(you_check.get())
        you_check.set(str(current_score + 1))
    else:
        pary = tk.Label(root, text="Ничья!")
        pary.grid(row=8, column=12)
rock = tk.Button(root,text = "Камень", command=rock_ch)
rock.grid(row=5,column=4)

def paper_ch():
    enemy_weapon = ["rock","paper","scissors"]
    enemy_choice = random.choice(enemy_weapon)
    if enemy_choice == "scissors":
        lose = tk.Label(root, text="Вы проиграли!")
        lose.grid(row=8,column=12)
        current_score = int(enemy_check.get())
        enemy_check.set(str(current_score + 1))
    elif enemy_choice == "rock":
        win = tk.Label(root, text="Вы выграли!")
        win.grid(row=8,column=12)
        current_score = int(you_check.get())
        you_check.set(str(current_score + 1))
    else:
        pary = tk.Label(root, text="Ничья!")
        pary.grid(row=8, column=12)
paper = tk.Button(root,text = "Бумага>", command=paper_ch)
paper.grid(row=5,column=5)

def scissors_ch():
    enemy_weapon = ["rock","paper","scissors"]
    enemy_choice = random.choice(enemy_weapon)
    if enemy_choice == "rock":
        lose = tk.Label(root, text="Вы проиграли!")
        lose.grid(row=8,column=12)
        current_score = int(enemy_check.get())
        enemy_check.set(str(current_score + 1))
    elif enemy_choice == "paper":
        win = tk.Label(root, text="Вы выграли!")
        win.grid(row=8,column=12)
        current_score = int(you_check.get())
        you_check.set(str(current_score + 1))
    else:
        pary = tk.Label(root, text="Ничья!")
        pary.grid(row=8, column=12)
scissors = tk.Button(root,text = "Ножницы", command=scissors_ch)
scissors.grid(row=5,column=6)

root.mainloop()