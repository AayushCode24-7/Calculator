from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import ImageOps
# 🎨 Color Theme
BG_COLOR      = "#121212"
ENTRY_BG      = "#1F1F1F"
ENTRY_FG      = "#FFE0B2"
BTN_BG        = "#FFB74D"
BTN_FG        = "#40E0D0"
BTN_ACTIVE    = "#00ACC1"
BTN_HIGHLIGHT = "#FF4081"
WINDOW_BORDER = "#2C2C2C"

# 🪟 Main window
root = Tk()
root.title("Aayush's Calculator")
root.geometry("410x410")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# 🧠 Expression holder
expression = ""

# 🖼️ Background image function
def set_background_image():
    file_path = filedialog.askopenfilename(
        title="Select Background Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if file_path:
        img = Image.open(file_path)
        img = ImageOps.fit(img, (410, 410), Image.Resampling.LANCZOS, centering=(0.5, 0.5))
        bg_img = ImageTk.PhotoImage(img)

        bg_label = Label(root, image=bg_img)
        bg_label.image = bg_img
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Raise widgets above background
        for widget in root.winfo_children():
            if isinstance(widget,(Entry, Button)):
                widget.lift()

# 🖊️ Entry widget
entry = Entry(root, width=12, font=('Arial', 24), bd=10, justify='right',
              bg=ENTRY_BG, fg=ENTRY_FG, highlightbackground=WINDOW_BORDER)
entry.grid(row=0, column=0, columnspan=4)

# 🔢 Core functions
def press(key):
    global expression
    expression += str(key)
    entry.delete(0, END)
    entry.insert(END, expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, END)
        entry.insert(END, result)
        expression = result
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")
        expression = ""

def clear():
    global expression
    expression = ""
    entry.delete(0, END)

def backspace():
    global expression
    expression = expression[:-1]
    entry.delete(0, END)
    entry.insert(END, expression)

def key_event(event):
    key = event.char
    if key in '0123456789.+-*/()':
        press(key)
    elif key == '\r':
        equal()
    elif key == '\x08':
        backspace()
    elif key.lower() == 'c':
        clear()

# 🎛️ Button layout
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
    ('.', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        Button(root, text=text, width=6, height=2, font=('Arial', 18),
               bg=BTN_HIGHLIGHT, fg=BTN_FG, activebackground=BTN_ACTIVE,
               command=equal).grid(row=row, column=col)
    elif text == 'C':
        Button(root, text=text, width=26, height=2, font=('Arial', 18),
               bg=BTN_HIGHLIGHT, fg=BTN_FG, activebackground=BTN_ACTIVE,
               command=clear).grid(row=row, column=col, columnspan=4)
    else:
        Button(root, text=text, width=6, height=2, font=('Arial', 18),
               bg=BTN_BG, fg=BTN_FG, activebackground=BTN_ACTIVE,
               command=lambda t=text: press(t)).grid(row=row, column=col)

# 🎨 Background image button
bg_button = Button(root, text="Set Background", font=('Arial', 12),
                   bg=BTN_HIGHLIGHT, fg=BTN_FG, activebackground=BTN_ACTIVE,
                   command=set_background_image)
bg_button.place(x=150, y=370)

# ⌨️ Keyboard bindings
root.bind("<Key>", key_event)
root.bind("<Return>", lambda event: equal())
root.bind("<BackSpace>", lambda event: backspace())
root.bind("<Escape>", lambda event: clear())

# 🚀 Launch
root.mainloop()