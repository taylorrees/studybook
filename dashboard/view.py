import tkinter as tk
import templates.ui as ui
import lesson_list.view as lesson_list_view
import lesson_publish.view as lesson_publish_view
import lesson_create.view as lesson_create_view
import user.view as add_user_view
import test_create.view as test_create_view
import test_list.view as test_list_view
import result.view as result_view
import result_list.view as result_list_view
import login
from user.user import User

class Dashboard:

    def __init__(self, root, window, user_id, login_status):
        self.root = root
        self.window = window
        self.user_id = user_id
        self.login_status = login_status
        self.build()

    def logout(self):
        """
        Log the user out of the system and
        present the login screen.
        """

        self.window.destroy()
        login.view.main()


    def build(self):

        # Quick and dirty dashboard.
        # Needs work once all views are
        # in place.
        #

        row = 0

        # Interface

        ui.title(self.root, text='Dashboard', row=row)
        row += 1
        ui.margin_y(self.root, px=10, row=row)
        row += 1

        tk.Label(self.root, text="User: " + self.user_id).grid(row=row)
        row += 1
        ui.margin_y(self.root, px=10, row=row)
        row += 1

        # If a lecturer is logged in
        # show them the lecturer specific actions
        if self.login_status == 1:
            tk.Button(self.root, text='Create Lesson', command=lesson_create_view.main, width=30).grid(row=row)
            row += 1
            tk.Button(self.root, text='Create Test', command=test_create_view.main, width=30).grid(row=row)
            row += 1
            tk.Button(self.root, text='Create Student', command=add_user_view.main, width=30).grid(row=row)
            row += 1
            tk.Button(self.root, text='Publish Lessons', command=lesson_publish_view.main, width=30).grid(row=row)
            row += 1

            ui.margin_y(self.root, px=5, row=row)
            row += 1
            tk.Button(self.root, text='View Results', command=result_list_view.main, width=30).grid(row=row)
            row += 1

        tk.Button(self.root, text='View Lessons', command=lesson_list_view.main, width=30).grid(row=row)
        row += 1

        view_test_list = lambda user_id = self.user_id : test_list_view.main(user_id)
        tk.Button(self.root, text='View Tests', command=view_test_list, width=30).grid(row=row)
        row += 1

        ui.margin_y(self.root, px=5, row=row)
        row += 1
        tk.Button(self.root, text='Logout', command=self.logout, width=30).grid(row=row)
        row += 1
        ui.margin_y(self.root, px=20, row=row)
        row += 1

def main(user_id, login_status):
    window = tk.Tk()
    window.title('Studybook | Dashboard')
    centered_frame = tk.Frame(window)

    app = Dashboard(centered_frame, window, user_id, login_status)

    centered_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    window.geometry(ui.center(window))
    window.mainloop()
