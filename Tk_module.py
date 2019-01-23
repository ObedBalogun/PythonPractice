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
        from the bottom-up i.e menu commands -> menu-> append menu to frame'''
        master_menu = Menu(self.master)
        self.master.config(menu=master_menu)
        #File Button
        file_button = Menu(master_menu)
        file_button.add_command(label="Exit", command = self.client_exit)
        master_menu.add_cascade(label = "File", menu=file_button)
        #Edit Button
        edit_button = Menu(master_menu)
        edit_button.add_command(label = "Undo")
        master_menu.add_cascade(label = "Edit", menu = edit_button)
        #View button
        view_button = Menu(master_menu)
        view_button.add_command(label="Tools")
        master_menu.add_cascade(label="View", menu=view_button)


    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")#specifies the dimension of the window
app = Window(root)
root.mainloop() #initializes and generates the window
