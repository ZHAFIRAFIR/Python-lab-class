from tkinter import*

#def buttonPushed():
	#global myEntry
	#text=myEntry.get()
	#print("the text is:",text)

def buttonPushed():
	global root
	global display
	global myEntry
	text="the text is:" + myEntry.get()
	Label(root,text=text).pack()

def buttonPushed():

	global anotherwindow
	global display
	global myEntry
	text="the text is:" + myEntry.get()
	Label(anotherwindow,text=text).pack()



def createEntry(root):
	global myEntry
	myEntry=Entry(root)
	myEntry.pack()

def createEntry(anotherwindow):
	global myEntry
	myEntry=Entry(anotherwindow)
	myEntry.pack()




#import tkinter as anyVarable
#root=anyVarable.Tk()
def main():
	global root
	global display
	root=Tk()
	anotherwindow=Tk()
	root.title("Root")
	anotherwindow.title("anotherwindow")
	root.minsize(width=200,height=200)
	anotherwindow.minsize(width=200,height=200)
	myButton=Button(root,text="submit",command=buttonPushed)
	myButton.pack()
	createEntry(root)
	myButton=Button(anotherwindow,text="enter",command=buttonPushed)
	myButton.pack()
	createEntry(anotherwindow)
	root.mainloop()
	anotherwindow.mainloop()





#myLabel=Label(root,text="hello guys")
#myLabel.pack()

#Label(root,text="hi guys").pack()


#row=4
#col=3

#for i in range(row):
	#for j in range(col):
		#text="row %d col %d"%(i,j)
		#Label(root,text=text).grid(row=i,column=j)




main()

