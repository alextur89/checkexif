#!python3
import sys
import piexif
from PIL import Image


if __name__ == '__main__':

    fname = sys.argv[1]
    todate = sys.argv[2]

    try:
        img = Image.open(fname)
    except IOError:
        print ("File not exist")
        sys.exit(-1)

    exif_dict = piexif.load(img.info['exif'])

    try:
        exif_dict['Exif'][36867] = todate
        exif_dict['Exif'][36868] = todate
        exif_dict['0th'][306] = todate
    except KeyError:
        print ("Error in file's metadata")
        sys.exit(-1)

    piexif.insert(piexif.dump(exif_dict), fname)
