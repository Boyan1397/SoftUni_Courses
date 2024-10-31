from typing import List
from math import ceil

class PhotoAlbum:

    page_info = 0
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List = self.__create_matrix()

    def __create_matrix(self):
        matrix = [[] for r in range(self.pages)]
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for _ in self.photos:
            try:
                if len(self.photos[PhotoAlbum.page_info]) == 4:
                    PhotoAlbum.page_info += 1
                self.photos[PhotoAlbum.page_info].append(label)
            except IndexError:
                return "No more free slots"

            return (f"{label} photo added successfully on page {PhotoAlbum.page_info+1}"
                    f" slot {len(self.photos[PhotoAlbum.page_info])}")

    def display(self):
        display_str = ""
        for page in self.photos:
            display_str += "-----------\n"
            if page:
                display_str += " ".join(["[]" for _ in page])
            display_str += "\n"
        display_str += "-----------"

        return display_str




album = PhotoAlbum(2)

print(album.add_photo("baby"))

print(album.add_photo("first grade"))

print(album.add_photo("eight grade"))

print(album.add_photo("party with friends"))

print(album.photos)

print(album.add_photo("prom"))

print(album.add_photo("wedding"))

print(album.display())

