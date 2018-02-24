from tkinter import*
class start(object):

	def __init__(self, root):


		self.name=StringVar()
		self.userName=None
		button1=Butto(root,text="start",command=self.welcomeMessage)
		button.pack()

	def welcomeMessage(self):
		label(root,text="salam").pack()
		label(root,text="our name?:").pack()
		name=Entry(root,textvariable=self.name)
		name.pack()
		submitbtn=ButtoN(ROOT,text="submit",command=self.getName)
		submitbtn.pack()

	def getName(self):
		self.userName=self.name.get()
		Label(root,text=self.userName).pack()

root=Tk()
x=Start(root)
root.title("class + GUI")
root.minsize(width=200,height=200)
root.mainloop()
