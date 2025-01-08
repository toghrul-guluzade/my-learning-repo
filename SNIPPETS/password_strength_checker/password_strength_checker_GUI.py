import string
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Label, PhotoImage

# Paths for assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"files")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Load common passwords list
try:
    with open('files\common_passwords.txt', 'r') as file:
        common_passwords = file.read().splitlines()
except FileNotFoundError:
    common_passwords = []


# Password strength logic with real-time feedback
def check_password_strength_real_time(event=None):
    password = entry_1.get()  # Get user input from Entry widget

    # Initialize variables
    upper_case = [1 if c in string.ascii_uppercase else 0 for c in password]
    lower_case = [1 if c in string.ascii_lowercase else 0 for c in password]
    special = [1 if c in string.punctuation else 0 for c in password]
    digits = [1 if c in string.digits else 0 for c in password]
    length = len(password)

    # Real-time validation messages
    if password in common_passwords:
        feedback_label.config(text="Password is too common. Choose another.")
        return
    if length < 8:
        feedback_label.config(text="Password must be at least 8 characters long.")
        return
    if sum(upper_case) == 0:
        feedback_label.config(text="Add at least one uppercase letter.")
        return
    if sum(lower_case) == 0:
        feedback_label.config(text="Add at least one lowercase letter.")
        return
    if sum(digits) == 0:
        feedback_label.config(text="Include at least one digit.")
        return

    # Calculate score
    score = 0
    if sum(upper_case) > 1:
        score += 1
    if sum(lower_case) > 1:
        score += 1
    if sum(special) >= 1:
        score += 1
    if sum(special) >= 2:
        score += 2
    if length >= 8:
        score += 1
    if length >= 9:
        score += 1
    if length >= 10:
        score += 1

    # Display password strength feedback
    feedback_label.config(text=f"Password strength: {score}/8")


# GUI setup
window = Tk()
window.title("Password Strength Checker")
window.geometry("300x300")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=300,
    width=300,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Image assets
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(150.0, 150.0, image=image_image_1)

# Title text
canvas.create_text(
    32.0,
    38.0,
    anchor="nw",
    text="Password Strength Checker",
    fill="#3B4640",
    font=("InriaSans Regular", 20 * -1)
)

# Entry box for password input
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
canvas.create_image(149.5, 129.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place(x=36.0, y=109.0, width=227.0, height=38.0)

# Bind the Entry widget to the real-time feedback function
entry_1.bind("<KeyRelease>", check_password_strength_real_time)

# Feedback label
feedback_label = Label(window, text="", bg="#D9D9D9", fg="#000000", wraplength=250, justify="center")
feedback_label.place(x=28.0, y=163.0, width=243.0, height=70.0)

# Disable resizing
window.resizable(False, False)
window.mainloop()
