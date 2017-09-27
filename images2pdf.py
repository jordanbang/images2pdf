#!/usr/bin/env python

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import argparse
import os

IMAGE_TYPES = ["jpg", "jpeg", "png"]

def combine_images(name, image_list):
    if ".pdf" not in name:
        name = name + ".pdf"
    c = canvas.Canvas(name, pagesize=letter)
    width, height = letter
    for image in image_list:
        try:
            c.drawImage(image, 0, 0, width*0.98, height*0.98)
            c.showPage()
        except:
            continue
    c.save()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Combine files into a pdf')
    parser.add_argument('name', metavar='name', help='name of the pdf')
    parser.add_argument('--images', metavar='file', nargs='+', help='images to combine')
    parser.add_argument('--dir', metavar='directory', help='directory of images to use')

    args = parser.parse_args()

    if (not args.images and not args.dir) or (args.dir and args.images):
        print("Error: include one of --images or --dir")
        exit()

    if args.images:
        images = args.images

    if args.dir:
        images = []
        for root, dirs, files in os.walk(args.dir):
            for f in files:
                parts = f.split('.')
                if parts[-1] in IMAGE_TYPES:
                    images.append(os.path.normpath(os.path.join(root, f)))

    print("Images combined: ")
    print(images)
    combine_images(args.name, images)
