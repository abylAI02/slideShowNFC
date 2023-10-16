import tkinter as tk

import PIL
from PIL import Image, ImageTk
import requests
from io import BytesIO
import time

# Define the image URLs
image_urls = [
    "https://coffee-broad-hookworm-789.mypinata.cloud/ipfs/QmPpqXjceKY2Zk6p4bT4zakESK6ro1qZTGg3ChvwvyGDUa/1.jpg",
    "https://coffee-broad-hookworm-789.mypinata.cloud/ipfs/QmPpqXjceKY2Zk6p4bT4zakESK6ro1qZTGg3ChvwvyGDUa/2.jpg",
    "https://coffee-broad-hookworm-789.mypinata.cloud/ipfs/QmPpqXjceKY2Zk6p4bT4zakESK6ro1qZTGg3ChvwvyGDUa/3.jpg",
    "https://coffee-broad-hookworm-789.mypinata.cloud/ipfs/QmPpqXjceKY2Zk6p4bT4zakESK6ro1qZTGg3ChvwvyGDUa/4.jpg",
    "https://coffee-broad-hookworm-789.mypinata.cloud/ipfs/QmPpqXjceKY2Zk6p4bT4zakESK6ro1qZTGg3ChvwvyGDUa/5.jpg",
    "https://coffee-broad-hookworm-789.mypinata.cloud/ipfs/QmPpqXjceKY2Zk6p4bT4zakESK6ro1qZTGg3ChvwvyGDUa/6.jpg",
]

# Create the main window
root = tk.Tk()
root.title("Image Slideshow")

# Create a label to display the images
image_label = tk.Label(root)
image_label.pack()

# Function to update the image in the label
def update_image(image_url):
    response = requests.get(image_url)
    image_data = BytesIO(response.content)
    img = Image.open(image_data)
    img = img.resize((800, 600), Image.LANCZOS)  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
    image_label.config(image=photo)
    image_label.image = photo

# Function to start the slideshow
def start_slideshow():
    for image_url in image_urls:
        update_image(image_url)
        root.update()
        time.sleep(3)  # Display each image for 3 seconds (adjust as needed)

# Start the slideshow when the "Start" button is clicked
start_button = tk.Button(root, text="Start Slideshow", command=start_slideshow)
start_button.pack()

# Close the window when the "Exit" button is clicked
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()
