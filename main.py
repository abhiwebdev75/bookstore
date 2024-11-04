from tkinter import *
import pymysql
from PIL import ImageTk,Image
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
mypass = "Codelover@988"
mydatabase="library"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library Management system - Abhinash")
root.minsize(width=400,height=400)
root.geometry("1800x1200")

same=True
n=0.25

from PIL import Image, ImageTk

# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
from PIL import Image, ImageTk

# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

n = 2  # Scaling factor
same = True  # Flag to maintain aspect ratio

newImageSizeWidth = int(imageSizeWidth * n)
newImageSizeHeight = int(imageSizeHeight * n) if same else int(imageSizeHeight / n)

# Resize the image with the correct tuple and resampling filter
background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.LANCZOS)

# Convert the image to a Tkinter-compatible format
img = ImageTk.PhotoImage(background_image)

# Create and configure the Canvas
Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image=img)      
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)


headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to Book store by Abhinash", bg='Red', fg='yellow', font=('Courier',16))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()


