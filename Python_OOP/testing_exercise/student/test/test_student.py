from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student_with_courses = Student("Lora",
                                            {"OOP": ["OOP course is hard"]})

        self.student_without_courses = Student("Boyan", {})

    def test_the_correct_innit(self):
        self.assertEqual("Lora", self.student_with_courses.name)
        self.assertEqual("Boyan", self.student_without_courses.name)

        self.assertEqual({"OOP": ["OOP course is hard"]}, self.student_with_courses.courses)
        self.assertEqual({}, self.student_without_courses.courses)

    def test_if_we_have_the_same_course_name_in_our_courses_attribute_and_test_if_we_are_adding_correct_notes(self):
        notes_to_add = ["maybe OOP not that hard"]
        expected_notes = ["OOP course is hard", "maybe OOP not that hard"]

        result = self.student_with_courses.enroll("OOP", notes_to_add)

        self.assertEqual(expected_notes, self.student_with_courses.courses["OOP"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_if_we_have_y_or_nothing_as_additional_notes_and_test_we_are_adding_the_course_and_notes(self):
        result = self.student_without_courses.enroll("Advanced", "This is a good course", "Y")

        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual("This is a good course",self.student_without_courses.courses["Advanced"])

    def test_if_we_have_nothing_as_additional_notes_and_testif_we_are_adding_the_course_and_notes(self):
        result = self.student_without_courses.enroll("Advanced", "This is a good course", "")

        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual("This is a good course", self.student_without_courses.courses["Advanced"])


    def test_adding_the_new_course_if_it_doesnt_exist(self):
        result = self.student_without_courses.enroll("Basics", "first", "good")

        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student_without_courses.courses["Basics"])

    def test_adding_notes_if_course_exists_and_are_the_notes_the_same(self):
        result = self.student_with_courses.add_notes("OOP", "Boyan se spravi")

        self.assertEqual(['OOP course is hard', 'Boyan se spravi'], self.student_with_courses.courses["OOP"])
        self.assertEqual("Notes have been updated", result)

    def test_the_exception_error_if_course_name_is_not_in_courses(self):

        with self.assertRaises(Exception) as ex:
            self.student_with_courses.add_notes("Blala", "hihi")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leaving_the_course_string_and_popping_out_of_the_courses_dict(self):
        result = self.student_with_courses.leave_course("OOP")

        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student_with_courses.courses)

    def test_exception_error_if_we_dont_have_that_course_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_courses.leave_course("Unreal")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))






if __name__ == "__main__":
    main()
