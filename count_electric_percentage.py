from PIL import Image
import os
from plotly import express


DIR_PATH = "img/"
WHITE = 255

FILENAMES_TO_AREAS = { #in km²
    "from-top-usa.tif": 9_833_517,
    "south-america.tif": 17_840_000,
    "center-russia.tif": 17_098_242,
    "bottom-australia.tif": 7_692_024,
    "top-central-America.tif": 1_000_000,
    "right-south-east-asia.tif": 4_545_000,
    "left-africa-europe.tif": 21_000_000,
    "top-canada.tif": 9_984_670
}

class Img:
    def __init__(self, filename, area):
        self.filename = filename
        self.area = area
        self.img = Image.open(DIR_PATH+filename)
        self.pixels = list(self.img.getdata())
        self.electric_pixels = self.pixels.count(WHITE)
        self.area_per_pixel = self.area / len(self.pixels)
        self.normalize = 0
            
    def normalized_weight(self):
        return self.electric_pixels * self.normalize

allImgs: list[Img] = []

for filename in os.listdir(DIR_PATH):

    with Image.open(DIR_PATH+filename) as img:
        allImgs.append(Img(filename, FILENAMES_TO_AREAS[filename]))

biggest_area_per_pixel = max([i.area_per_pixel for i in allImgs])

weighted_sum = 0

for img in allImgs:
    img.normalize = img.area_per_pixel / biggest_area_per_pixel
    weighted_sum += img.electric_pixels * img.normalize     

for img in allImgs:
    consumption_percentage = (img.normalized_weight() / weighted_sum) * 100
    print(f"{img.filename}: {consumption_percentage}%")

graph = express.pie(names=[img.filename for img in allImgs], 
                    values=[(img.normalized_weight() / weighted_sum) * 100 for img in allImgs])

graph.show()