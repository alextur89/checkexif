#!python3
import sys
import piexif
from PIL import Image
import argparse
import datetime

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Change date in image metadata.')
    parser.add_argument('--filename', '-f', dest='filename', type=open, help='File to be change', nargs='+', required=True)
    parser.add_argument('--date', '-d', dest='date', help='New date')
    parser.add_argument('--show', '-s', action='store_true', help='Show date')

    args = parser.parse_args()

    for fname in args.filename:
        try:
            img = Image.open(fname.name)
        except IOError:
            print ("File not exist")
            sys.exit(-1)

        try:
            exif_dict = piexif.load(img.info['exif'])
        except KeyError:
            print ('No exif data')
            sys.exit(0)


        if args.show:
            print ("Initial date: " + str(exif_dict['Exif'][36867]) )
            print ("Date of digitization: " + str(exif_dict['Exif'][36868]) )
            print ("Date: " + str(exif_dict['0th'][306]))

        if args.date:
            todate = str(args.date)
            try:
                exif_dict['Exif'][36867] = todate
                exif_dict['Exif'][36868] = todate
                exif_dict['0th'][306] = todate
            except KeyError:
                print ("Error in file's metadata")
                sys.exit(-1)

            piexif.insert(piexif.dump(exif_dict), fname.name)
