from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(True, True)

# Icons here
image_path = "Images/weather_app_logo.png"
original_image = Image.open(image_path)
resized_image = original_image.resize((80, 140))  # Replace width and height with your desired values
photo = ImageTk.PhotoImage(resized_image)

# Set the resized image as the window icon
root.iconphoto(False, photo)
Round_box=PhotoImage(file="images/rounded_corner_image_pradyumna.png")
Label(root,image=Round_box,bg="#57adff").place(x=30,y=110)
#labels
label1=Label(root,text="Temprature",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=50,y=120)

root.mainloop()
