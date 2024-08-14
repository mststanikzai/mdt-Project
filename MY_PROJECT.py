#print("IN THE NAME OF ALLAH")
#11:00 AM, Friday, 7/12/2024 started
from msilib.schema import File
from tkinter import *    #برنامه برای کارخانگی می سازیم tkinter امروز با استفاده از کتابخانه
from tkinter import filedialog
from PIL import ImageTk , Image
from tkinter import messagebox
import tkinter as tk
mustafa = Tk()
mustafa.geometry("800x470")
mustafa.title("Welcome to my project.")
#here i want to add my photo
frame1 = LabelFrame(mustafa, text="MY PHOTO", padx=128, pady=154, colormap="new", bg="green", font=20, fg="black", relief="flat")
frame1.grid(row=0, column=1)
Button(frame1, text="click to see my photo", fg="white", bg="black", padx=42, pady=20, font=18, activeforeground="gray", activebackground="blue").grid(row=0, column=0)
#   what is this?   (import os)
#and this frame is for my H.W. , and it how four buttons fot my h.w. if you click on each button, you will see a new window
frame = LabelFrame(mustafa, text="MY PROJECT", padx=15, pady=49, colormap="new", bg="green", font=20, fg="black", relief="flat")
frame.grid(row=0, column=0)


def load_file():
      global top
      top =Toplevel()
      top.geometry("500x500")
      top.title("this is my first H.W.")
      file_path = filedialog.askopenfilename(filetypes=[("text file", "*,txt"), ("All files", "*,*")])
      if file_path:
            try:
                  with open(file_path, "r") as files:
                        content = File.read()
                        text_area.delete("1.0", tk.End)
                        text_area.insert(tk.END, content)
                  messagebox.showinfo("Info", r"file loaded sucessfully from {file_path}")
            except Exception as e:
                  messagebox.showerror("Error", r"failed to load file: {e}")


      text_area = tk.Text(mustafa, wrap='word', height=160, width=240)
# text_area.pack()



Button(frame, text="click to see my 1th H.W.", fg="white", bg="black", padx=42, pady=20, font=18, activeforeground="gray", activebackground="blue", command=load_file).grid(row=0, column=0)

def open1():
      top =Toplevel()
      top.geometry("500x500")
      top.title("this is my second H.W.")
      btn1 = Button(top, text="close the window.", command=top.destroy, padx=40, pady=20).grid()
Button(frame, text="click to see my 2th H.W.", fg="white", bg="black", padx=42, pady=20, font=18, activeforeground="gray", activebackground="blue", command=open1).grid(row=1,column=0)

def open2():
      top =Toplevel()
      top.geometry("500x500")
      top.title("this is my third H.W.")
      btn1 = Button(top, text="close the window.", command=top.destroy, padx=40, pady=20).grid()
Button(frame, text="click to see my 3th H.W.", fg="white", bg="black", padx=42, pady=20, font=18, activeforeground="gray", activebackground="blue", command=open2).grid(row=2,column=0)

def open3():
      top =Toplevel()
      top.geometry("500x500")
      top.title("this is my fourth H.W.")
      btn1 = Button(top, text="close the window.", command=top.destroy, padx=40, pady=20).grid()
Button(frame, text="click to see my 4th H.W.", fg="white", bg="black", padx=42, pady=20, font=18, activeforeground="gray", activebackground="blue", command=open3).grid(row=3,column=0)

def load_file2():
      global top
      top =Toplevel()
      top.geometry("500x500")
      top.title("this is my first H.W.")
      file_path = filedialog.askopenfilename(filetypes=[("text file", "*,txt"), ("All files", "*,*")])
      if file_path:
            try:
                  with open(file_path, "r") as files:
                        content = File.read()
                        text_area.delete("1.0", tk.End)
                        text_area.insert(tk.END, content)
                  messagebox.showinfo("Info", f"file loaded sucessfully from {file_path}")
            except  Exception as e:
                  messagebox.showerror("Error", f"failed to load file: {e}")


      text_area = tk.Text(mustafa, wrap='word', height=160, width=240)
      text_area.pack()

#In first button i want to add my information and the second button is for exiting progrom
Button(mustafa, text="MY DETAILS", fg="white", bg="black", padx=95.4999, pady=20, font=18, activeforeground="gray", activebackground="blue", command=load_file2).grid(row=4,column=0)
Button(mustafa, text="EXIT", fg="white", bg="black", padx=230, pady=20, font=18, activeforeground="gray", activebackground="blue", command=mustafa.destroy).grid(row=4,column=1)

mustafa.mainloop()