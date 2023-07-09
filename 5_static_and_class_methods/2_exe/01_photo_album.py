from math import ceil


class PhotoAlbum:
    PHOTO_PER_PAGES = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.build_photos_matrix()

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTO_PER_PAGES)

        return cls(pages)

    def add_photo(self, label):
        for row, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTO_PER_PAGES:
                page.append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(page) + 1}"

        return "No more free slots"

    def build_photos_matrix(self):
        result = []

        for _ in range(self.pages):
            result.append([])

        return result

    def display(self):
        delimiter = "-" * 11
        result = delimiter + "\n"

        for page in self.photos:
            page_str = " ".join(['[]' for _ in page])
            result += page_str + "\n" + delimiter + "\n"

        return result.strip()


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())

# baby photo added successfully on page 1 slot 2
# first grade photo added successfully on page 1 slot 3
# eight grade photo added successfully on page 1 slot 4
# party with friends photo added successfully on page 1 slot 5
# [['baby', 'first grade', 'eight grade', 'party with friends'], []]
# prom photo added successfully on page 2 slot 2
# wedding photo added successfully on page 2 slot 3
# -----------
# [] [] [] []
# -----------
# [] []
# -----------
