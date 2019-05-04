#!python3
import sys
import piexif
from PIL import Image

fname = sys.argv[1]
todate = sys.argv[2]
img = Image.open(fname)
exif_dict = piexif.load(img.info['exif'])

exif_dict['Exif'][36867] = todate
exif_dict['Exif'][36868] = todate

print(exif_dict['Interop'])

exif_dict['0th'][306] = todate

dateForEdit = exif_dict['Exif'][36867]
dateForCreate = exif_dict['Exif'][36868]

piexif.insert(piexif.dump(exif_dict), fname)

print(dateForEdit)
print(dateForCreate)
