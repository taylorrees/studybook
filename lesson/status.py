# Author: Taylor Rees

class LessonStatus(object):
    """
    This class is responsible for the
    creation and management of a lesson
    status. The lesson status is used to
    provide details about a lesson instance.
    """

    def __init__(self, student_id, lesson_id):
        """
        Construct a lesson status. The default
        value for a lesson view is set to False.

        @param {string} student_id
        @param {string} lesson_id
        @return {void}
        """

        self.student_id = student_id
        self.lesson_id = lesson_id
        self.viewed = False


    def viewed(self, viewed):
        """
        A method to set the viewed attribute.
        This will provide details as to whether
        a student has view a lesson.

        @param {boolean} viewed
        @return {void}
        """

        self.viewed = viewed


    def get(self, student_id, lesson_id):
        """
        Returns the value of the viewed
        attribute, providing details as to
        whether a student has viewed a lesson.

        @param {string} student_id
        @param {string} lesson_id
        @return {boolean}
        """

        if (self.student_id == student_id) and (self.lesson_id == lesson_id):
            return self.viewed
