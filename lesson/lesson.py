# Author: Taylor Rees

from lesson.slide import Slide
import shelve

class Lesson(object):
    """
    This class is responsible for the
    creation and management of lessons.
    A lesson consists of 1 or more slides
    and can have an associated test.
    """

    def __init__(self, _id, name, published = False):
        self._id = _id
        self.name = name
        self.slides = []
        self.test = None
        self.published = published


    def add(self, title, body, image = ''):
        """
        Add a slide to the current list of
        slides.
        """

        self.slides.append(Slide(title, body, image))


    def remove(self, slide_number):
        """
        Remove a slide from the current
        list of slides using the slide
        order.

        @param {integer} slide_number
        """

        del self.slides[slide_number]


    def has_test(self):
        """
        Determines whether the lesson has
        an associated test.
        """

        if self.test:
            return True

        return False


    def set_test(self, test):
        """
        Sets the test attribute of the lesson,
        thus providing the lesson with an
        associated test.
        """

        self.test = test


    def store(self):
        """
        Store a lesson as a persistent object
        using python shelving. This will allow
        lessons to be accessed in the future.
        """

        # Initialise the datastore
        try:
            # Open existing
            store = shelve.open('lesson/store', 'w')
        except Exception:
            # Create new
            # Only if doesn't exist
            store = shelve.open('lesson/store', 'n')

        # Store the lesson
        store[self._id] = self
        store.close()
