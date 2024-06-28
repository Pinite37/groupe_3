from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import time
import threading
import requests

API_URL = "https://api-inference.huggingface.co/models/hf-internal-testing/tiny-stable-diffusion-pipe"
head = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

# Function to generate image
def query(payload):
	response = requests.post(API_URL, headers=head, json=payload)
	return response.content

# Function to simulate image generation
def generate_image():
    threading.Thread(target=simulate_loading).start()
    

def simulate_loading():
    spinner.grid(row=1, column=1, padx=10, pady=10)
    spinner.start()  # Start the spinner
    for i in range(100):
        time.sleep(0.05)
        progress_var.set(i + 1)
    display_image()

def display_image():
    spinner.stop()  # Stop the spinner
    spinner.grid_remove()  # Hide the spinner
    # Load an example image (replace with actual image generation)
    img = Image.open(image_bytes)  # Ensure this image is in the same directory
    img = img.resize((500, 300), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label['image'] = img

# Create main window
Win = Tk()
Win.title("Visualizer")
Win.geometry("1100x800") 
Win.minsize(1000, 800)
Win.config(background="#FFFFFC")

# Title of the application
titre = Label(Win, text="Visualizer", font=("Arial", 30), bg="#FFFFFC")
titre.pack(pady=20)

# Guide for image description
info1 = Label(Win, text="Description:", font=("Arial", 15), bg="#FFFFFC")
info1.pack()

# Description input
descr = StringVar()
descript=str(descr)
entree = Entry(Win, textvariable=descr, bg="#d6cdcd", font=("Arial", 17))
entree.pack(fill="x", padx=200, pady=20)

# Image generating
image_bytes = query({"inputs": descript,})

# Button to generate image
crea = Button(Win, text="Generate Image", font=("Arial", 20), bg="#d6cdcd", command=generate_image)
crea.pack(pady=20)

# Frame for image display area and spinner
image_frame = Frame(Win, bg="#FFFFFC")
image_frame.pack(pady=20)

# Spinner (loading indicator)
progress_var = DoubleVar()
spinner = Progressbar(image_frame, mode='indeterminate', length=100, variable=progress_var)

# Image display area
image_label = Label(image_frame, bg="#FFFFFC", width=500, height=300)
image_label.grid(row=0, column=0, padx=10, pady=10)

# Display window
Win.mainloop()
