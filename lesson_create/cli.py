from lesson.lesson import Lesson

def main():
    opt = 'y'
    count = 0

    print()
    print('Welcome to the lesson editor.')
    print()

    lesson = Lesson(input('Enter Lesson ID: '), input('Enter Lesson Name: '))

    print()
    print('Please follow the instructions \nto add slides to this lesson.')
    print()

    while opt != 'n':
        count += 1
        print('Slide ' + str(count))
        title = input('Title: ')
        body = input('Body: ')
        lesson.add(title, body)
        opt = input('Add another? (y/n): ').lower()
        print()

    print(lesson._id)

    lesson.store()
