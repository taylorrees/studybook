#Author: Thomas Sweetman

#class TestView:

def main():
	
	window = tk.Tk()
	window.title('Studybook | Create Lesson')
	app = TestView(window)
	window.grid_columnconfigure(0, weight=1)
	window.mainloop()