from unittest import TestCase, main

from Python_OOP.Skeleton_OOP_Retake_Problem.project.gallery import Gallery

from unittest import TestCase, main

import unittest


class TestGallery(unittest.TestCase):
    def setUp(self):
        self.gallery = Gallery("ArtGallery123", "NewYork", 150.5)

    def test_initialization(self):
        self.assertEqual(self.gallery.gallery_name, "ArtGallery123")
        self.assertEqual(self.gallery.city, "NewYork")
        self.assertEqual(self.gallery.area_sq_m, 150.5)
        self.assertTrue(self.gallery.open_to_public)
        self.assertEqual(self.gallery.exhibitions, {})

    def test_invalid_gallery_name(self):
        with self.assertRaises(ValueError):
            self.gallery.gallery_name = "Invalid Name!"

    def test_empty_gallery_name(self):
        with self.assertRaises(ValueError):
            self.gallery.gallery_name = " "

    def test_invalid_city_name(self):
        with self.assertRaises(ValueError):
            self.gallery.city = "123City"

    def test_city_with_spaces(self):
        self.gallery.city = "Los Angeles"
        self.assertEqual(self.gallery.city, "Los Angeles")

    def test_invalid_area(self):
        with self.assertRaises(ValueError):
            self.gallery.area_sq_m = -50.0

    def test_zero_area(self):
        with self.assertRaises(ValueError):
            self.gallery.area_sq_m = 0.0

    def test_add_exhibition(self):
        result = self.gallery.add_exhibition("Impressionism", 2023)
        self.assertEqual(result, 'Exhibition "Impressionism" added for the year 2023.')
        self.assertIn("Impressionism", self.gallery.exhibitions)
        self.assertEqual(self.gallery.exhibitions["Impressionism"], 2023)

    def test_add_existing_exhibition(self):
        self.gallery.add_exhibition("ModernArt", 2022)
        result = self.gallery.add_exhibition("ModernArt", 2022)
        self.assertEqual(result, 'Exhibition "ModernArt" already exists.')

    def test_remove_exhibition(self):
        self.gallery.add_exhibition("Renaissance", 2021)
        result = self.gallery.remove_exhibition("Renaissance")
        self.assertEqual(result, 'Exhibition "Renaissance" removed.')
        self.assertNotIn("Renaissance", self.gallery.exhibitions)

    def test_remove_nonexistent_exhibition(self):
        result = self.gallery.remove_exhibition("NonExistent")
        self.assertEqual(result, 'Exhibition "NonExistent" not found.')

    def test_list_exhibitions_open(self):
        self.gallery.add_exhibition("Cubism", 2020)
        self.gallery.add_exhibition("Abstract", 2019)
        exhibitions_list = self.gallery.list_exhibitions()
        self.assertEqual(exhibitions_list, "Cubism: 2020\nAbstract: 2019")

    def test_list_exhibitions_closed(self):
        self.gallery.open_to_public = False
        result = self.gallery.list_exhibitions()
        self.assertEqual(result, "Gallery ArtGallery123 is currently closed for public! Check for updates later on.")

    def test_stress_add_exhibitions(self):
        for i in range(1000):
            self.gallery.add_exhibition(f"Exhibition{i}", 2000 + i)
        self.assertEqual(len(self.gallery.exhibitions), 1000)
        self.assertEqual(self.gallery.exhibitions["Exhibition999"], 2999)

    def test_stress_remove_exhibitions(self):
        for i in range(100):
            self.gallery.add_exhibition(f"Exhibition{i}", 2000 + i)
        for i in range(100):
            self.gallery.remove_exhibition(f"Exhibition{i}")
        self.assertEqual(len(self.gallery.exhibitions), 0)


if __name__ == "__main__":
    unittest.main()