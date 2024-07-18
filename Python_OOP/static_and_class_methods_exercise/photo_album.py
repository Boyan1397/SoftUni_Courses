from typing import List


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = self.__make_the_matrix() #matrix

    def __make_the_matrix(self):
        my_photos_matrix = [[] for r in range(self.pages)]
        return my_photos_matrix


