from tkinter import *
import wikipedia

def on_press():
    query = question_entry.get()
    result.delete(1.0, END)  # Clear previous result
    result.insert(INSERT, wikipedia.summary(query))

def clear_fields():
    question_entry.delete(0, END)
    result.delete(1.0, END)

root = Tk()
root.title('Wikipedia Search GUI')

question = Label(root, text='Question')
question.pack()
question_entry = Entry(root, bd=5)
question_entry.pack()

button_frame = Frame(root)  # Create a frame to hold the buttons
button_frame.pack()

search_button = Button(button_frame, text='Search', command=on_press)
search_button.pack(side=LEFT)  # Pack to the left within the frame

clear_button = Button(button_frame, text='Clear', command=clear_fields)
clear_button.pack(side=LEFT)  # Pack to the left within the frame

result = Text(root)
result.pack()

root.mainloop()
