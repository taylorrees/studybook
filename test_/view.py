#Author: Thomas Sweetman

class TestView:

	def main(_id):
		store = shelve.open('test/store')
		test = store[_id]
		store.close()

		window = tk.Tk()
		window.title("Studybook | Test Viewer")
		app = TestView(window, test)
		window.mainloop()