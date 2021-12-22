from tkinter import *
import random

root = Tk()
root.title("Lucky friend Wheel")
root.geometry("400x400")

alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(alpha_list)
label1 = Label(root)

def random_word():
    random_no1 = random.randint(0, 25)
    random_no2 = random.randint(0, 25)
    random_no3 = random.randint(0, 25)
    random_no4 = random.randint(0, 25)
    random_no5 = random.randint(0, 25)
    q = alpha_list[random_no1]
    w = alpha_list[random_no2]
    e = alpha_list[random_no3]
    r = alpha_list[random_no4]
    t = alpha_list[random_no5]
    label1["text"] = q + w + e + r + t

btn1 = Button(root)
btn1 = Button(root, text = "Generate Random Word", command = random_word)
btn1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label1.place(relx = 0.5, rely = 0.7, anchor = CENTER)
root.mainloop()
