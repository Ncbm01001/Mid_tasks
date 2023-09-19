#написать калькулятор с кнопками
import tkinter as tk

main_wind = tk.Tk ()
main_wind.title("Калькулятор кнопочный)")
main_wind.geometry("300x500+600+180")

pull = tk.Entry(main_wind)
pull.grid(row=4,column=3)

def add_1():
    pull.insert(tk.END,"1")
one = tk.Button(main_wind,text="1",command=add_1)
one.grid(row=5,column=4)
def add_2():
    pull.insert(tk.END,"2")
two = tk.Button(main_wind,text="2",command=add_2)
two.grid(row=5,column=5)
def add_3():
    pull.insert(tk.END,"3")
three = tk.Button(main_wind,text="3",command=add_3)
three.grid(row=5,column=6)
def add_4():
    pull.insert(tk.END,"4")
four = tk.Button(main_wind,text="4",command=add_4)
four.grid(row=6,column=4)
def add_5():
    pull.insert(tk.END,"5")
five = tk.Button(main_wind,text="5",command=add_5)
five.grid(row=6,column=5)
def add_6():
    pull.insert(tk.END,"6")
six = tk.Button(main_wind,text="6",command=add_6)
six.grid(row=6,column=6)
def add_7():
    pull.insert(tk.END,"7")
seven = tk.Button(main_wind,text="7",command=add_7)
seven.grid(row=7,column=4)
def add_8():
    pull.insert(tk.END,"8")
eight = tk.Button(main_wind,text="8",command=add_8)
eight.grid(row=7,column=5)
def add_9():
    pull.insert(tk.END,"9")
nine = tk.Button(main_wind,text="9",command=add_9)
nine.grid(row=7,column=6)
def add_0():
    pull.insert(tk.END,"0")
null = tk.Button(main_wind,text="0",command=add_0)
null.grid(row=8,column=5)
def add_del():
    pull.delete(0,tk.END)
null = tk.Button(main_wind,text="del",command=add_del)
null.grid(row=9,column=10)

def pl_do():
    global result1
    result1 = int(pull.get())
    pull.delete(0, tk.END)
    global do
    do = "+"
pl = tk.Button(main_wind,text="+",command=pl_do)
pl.grid(row=5,column=9)

def min_do():
    global result1
    result1 = int(pull.get())
    pull.delete(0, tk.END)
    global do
    do = "-"
min = tk.Button(main_wind,text="-",command=min_do)
min.grid(row=5,column=10)

def pr_do():
    global result1
    result1 = int(pull.get())
    pull.delete(0, tk.END)
    global do
    do = "*"
pr = tk.Button(main_wind,text="*",command=pr_do)
pr.grid(row=6,column=9)

def delen_do():
    global result1
    result1 = int(pull.get())
    pull.delete(0, tk.END)
    global do
    do = "/"
delen = tk.Button(main_wind,text="/",command=delen_do)
delen.grid(row=6,column=10)

def step_do():
    global result1
    result1 = int(pull.get())
    pull.delete(0, tk.END)
    global do
    do = "**"
step = tk.Button(main_wind,text="**",command=step_do)
step.grid(row=7,column=9)

def eq_do():
    global result2
    result2 = int(pull.get())
    if do == "+":
        global result3
        result3 = result1 + result2
        pull.delete (0, tk.END)
        pull.insert(0, str(result3))
    elif do == "-":
        result3 = result1 - result2
        pull.delete (0, tk.END)
        pull.insert(0, str(result3))
    elif do == "*":
        result3 = result1 * result2
        pull.delete (0, tk.END)
        pull.insert(0, str(result3))
    elif do == "/":
        result3 = result1 / result2
        pull.delete (0, tk.END)
        pull.insert(0, str(result3))
    elif do == "**":
        result3 = result1 ** result2
        pull.delete (0, tk.END)
        pull.insert(0, str(result3))
    else:
        print(1)
eq = tk.Button(main_wind,text="=",command=eq_do)
eq.grid(row=6,column=10)


main_wind.mainloop()
