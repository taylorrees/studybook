# Author: Taylor Rees

class Slide(object):
    """
    This class is responsible for the
    creation and management of lesson
    slides.
    """

    def __init__(self, title, body, image = ''):
        """
        Slide constructor.

        @param {string} title
        @param {string} body
        @param {string} img (optional)
        """

        self.title = title
        self.body = body
        self.image = image
