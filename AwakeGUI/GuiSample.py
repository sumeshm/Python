import Tkinter as tk


def write_slogan():
	update_label("Hello again")

def update_label(message):
    print("Tkinter is easy to use!")
    label.config(text=str(message))


root = tk.Tk()
root.title("Awake")

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.RIGHT)

label = tk.Label(root, fg="dark green")
label.pack()

update_label("logs")

root.mainloop()
