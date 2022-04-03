import tkinter as tk
#import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk
#from tkinter.ttk import *
#   from Pillow import ImageTK, Image
#class Temp():
    
from scan import Scan
from add_classmate import Add_Classmate


class GUI(Frame):
    #def __init__(self, name):
        
    #inTex = Text()
    # def getText(inputText):
    #     tempString = inputText.get("1.0", "end")
    #     print(tempString)

    # def button2Press(self):
    #     print("Edit Class Name")
    #     tempWindow = Tk()
    #     tempWindow.geometry("200x100+650+400")
    #     tempWindow.title("Edit Class Name")
    #     tempWindow.configure(background = '#25274D')
    #     #tempWindow.resizable(False, False)
    #     inputText = Text(tempWindow, height = 1, width = 20)
    #     inputText.place(x = 17, y = 20)
    #     tempButton = Button(tempWindow, text="Confirm", bg='#464866', activebackground = "#29648A", 
    # width = 5, height = 1, fg = "gray11", font = ("Helvetica", 10), command = self.getText(inputText))
    #     tempButton.place(x = 17, y = 30)
        
        #inTex = inputText
        
        
        #Label(tempWindow, text = "Enter new class name", font = ('Calibri 12')).pack()
        #x = Entry(tempWindow, width = 10)
        

    def button1Press():
        print("Add New Students")
        add = Add_Classmate()
        add.start()

    def button2Press():
        print("How to use")
        tempWindow = Tk()
        tempWindow.geometry("600x300+650+400")
        tempWindow.title("How to use")
        tempWindow.configure(background = '#25274D')
        displayText = Text(tempWindow, height = 10, width = 40, font = ('Calibri', 20), bg = '#25274D', fg = '#AAABB8', bd = 0,)
        displayText.insert(INSERT, "1.) \"S\" is to snap shots during data collection ")
        displayText2 = Text(tempWindow, height = 10, width = 40, font = ('Calibri', 20), bg = '#25274D', fg = '#AAABB8', bd = 0,)
        displayText2.insert(INSERT, "2.) \"X\" is used to terminate the data collection.")
        displayText3 = Text(tempWindow, height = 10, width = 40, font = ('Calibri', 20), bg = '#25274D', fg = '#AAABB8', bd = 0,)
        displayText3.insert(INSERT, "3.) \"Q\" is used to quit the live feed for attendance")
        displayText.place(x = 17, y = 20)
        displayText2.place(x = 17, y = 60)
        displayText3.place(x = 17, y = 100)


    def button3Press():
        # print("Start Attendance")
        live_feed = Scan()
        live_feed.start()

    window = Tk()
    window.title("OnSite")

#'''
#    canvas = Canvas(window, width = 200, height = 200)
#    canvas.pack()
#    img = PhotoImage(r'C:\Users\nicka\OneDrive\Desktop\VS_code_python_projects\INSIGHT.png')
#    canvas.create_image(20, 20, image = img)
#    
#    #imgPath = PhotoImage(file = 'C:\Users\nicka\OneDrive\Desktop\VS_code_python_projects\INSIGHT.png')
    #Label(window, image = imgPath).pack()
#'''



    #helv36 = tkFont.Font(family =  "Helvetica", size = 36, weight = "normal")

    #style1 = Style()
    #style1.configure('testStyle', background = "#345", foreground = 'black', font = ('Arial', 14))
    #style2 = Style()
    #style2.configure('testStyle2', background = "#345", foreground = 'black', font = helv36)

    #st = Style()
    #st.configure('testStyle3', background='#345', foreground='black', font=('Arial', 14 ))
    
    #btn1 = Button(window, text = "Start Program")
    #btn1.bg = "#556B2F"
    #btn1.place(x = 100, y = 300)
    #btn2 = Button(window, text="test", fg='blue')

    btn1 = Button(window, text="Add new students", bg='#464866', activebackground = "#29648A", 
    width = 15, height = 2, fg = "gray11", font = ("Helvetica", 16), command = button1Press, cursor = "cross")
    btn1.place(x =  410, y = 420)
    btn2 = Button(window, text = "How to use", bg='#464866', activebackground = "#29648A", 
    width = 15, height = 2, fg = "gray11", font = ("Helvetica", 16), command = button2Press, cursor = "pirate")
    btn2.place( x = 410, y = 320)

    btn3 = Button(window, text="Start Attendance", bg='#464866', activebackground = "#29648A", 
    width = 15, height = 2, fg = "gray11", font = ("Helvetica", 16), command = button3Press)
    btn3.place( x = 410, y = 220)

        #btn3 = Button(window, text='blah blah', style= 'testStyle3', command=None).pack()
    #btn2.grid(row = 50, column = 100)
    #startText = Text(window, bg = "#AAABB8", font = ("Helvetica, 30"), text = "On Site")
    #startText.place( x = 410, y = 100)
    startText = Text(window, height = 1, width = 8, font = ('Calibri', 50), bg = '#25274D', fg = '#AAABB8', bd = 0, cursor = "heart")
    startText.insert(INSERT, "ON ")
    startText.insert(END, "SITE")
    startText['state'] = 'disabled'
    startText.place( x = 395, y = 100)
    
    #startText.pack()
    window.geometry("1024x526+250+130")
    window.configure(background = '#25274D')
    window.mainloop()
    #25274D



"""
class karl( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("INSIGHT")
        self.button1 = Button( self, text = "CLICK HERE", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
    def new_window(self):
        self.newWindow = karl2()
class karl2(Frame):     
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("karlos More Window")
        new.button = tk.Button(  text = "PRESS TO CLOSE", width = 25,
                                 command = self.close_window )
        new.button.pack()
    def close_window(self):
        self.destroy()
def main(): 
    karl().mainloop()
if __name__ == '__main__':
    main()
    """