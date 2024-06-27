from tkinter import *
from PIL import Image, ImageTk
import json
from difflib import get_close_matches

dictionary = open("dictionary.json", encoding="utf-8")
data_load = json.load(dictionary)

def search_word(word):
    if word in data_load:
        meaning_word.delete(1.0, END)
        meaning_word.config(fg='black')
        meaning_word.insert(END, data_load[word])
    elif len(get_close_matches(word, data_load.keys()))>0:
        meaning_word.config(fg="dark green")
        meaning_word.delete(1.0, END)
        meaning_word.insert(END, "Were you finding {} and meaning is : {}".format(get_close_matches(word, data_load.keys())[0], data_load[get_close_matches(word, data_load.keys())[0]]))
        final = get_close_matches(word, data_load.keys())
        
root = Tk()
root.title("DICTIONARY")

image = Image.open('dict.jpg')
image_picture = ImageTk.PhotoImage(image)
dest_pic = Label(root, image=image_picture)
dest_pic.pack()

a = StringVar()
word_1 = Entry(root, textvariable=a, background="white", fg="black", font=('arial', 40, "bold"))
word_1.place(relx=.185, rely=0.70, relwidth=.63, relheight=.082)

button_1 = Button(root, text="SEARCH THE WORD", command=lambda:search_word(a.get()), background="ForestGreen", fg="black", font=('arial', 35, "bold"))
button_1.place(relx=.25, rely=.85, relwidth=.50, relheight=.052)

meaning_word = Text(root, background="white", font=('arial', 25, "bold"))
meaning_word.place(relx=.010, rely=.05, relwidth=.98, relheight=.5)

root.mainloop()
