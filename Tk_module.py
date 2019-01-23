from tkinter import *
class Window(Frame):
    def __init__(self, master = None):      #parent widget
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("Frame") #name of frame
        self.pack(fill=BOTH, expand=1) #packs content into frame
        #quitButton = Button(self, text='Quit', command = self.client_exit)
        #quitButton.place(x=0, y=0)
        '''To create a menu list using tk you define your parameters
        from the bottom-up i.e menu items -> menu-> append menu to frame'''
        menu = Menu(self.master) #menu of the master window
        self.master.config(menu=menu)
        file = Menu(menu)

    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")#specifies the dimension of the window
app = Window(root)
root.mainloop() #initializes and generates the window
