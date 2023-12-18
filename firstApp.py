from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
root = Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)

# Icons here
image_path = "Images/weather_app_logo.png"
original_image = Image.open(image_path)
resized_image = original_image.resize((290, 140))  # Replace width and height with your desired values
photo = ImageTk.PhotoImage(resized_image)

# Set the resized image as the window icon
root.iconphoto(False, photo)
Round_box=PhotoImage(file="images/rounded_corner_image_pradyumna.png")
Label(root,image=Round_box,bg="#57adff").place(x=30,y=130)
#labels
label1=Label(root,text="Temprature",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=50,y=150)

label2=Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="#203243")
label2.place(x=50,y=170)

label3=Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=50,y=190)

label4=Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=50,y=210)

label4=Label(root,text="Description",font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=50,y=230)

#Search box
Search_image=PhotoImage(file="Images/RoundCornerOne.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=170)

weat_image=PhotoImage(file="Images/resized_cloud_image.png")#I need video here
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=185)

textfield=tk.Entry(root,justify='center',width=15,font=(
    'poppins',
    25,
    'bold'
),bg="#203243",
border=0,
fg="white")
textfield.place(x=390,y=180)
textfield.focus()





root.mainloop()