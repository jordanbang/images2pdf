# NoteName

NoteName is simple python script to combine a list of images into a pdf.  It uses reportlabs python package and pdfgen to create the pdf.

NoteName can be run using the following command:

    python notename.py name --images image1.jpg image2.jpg image3.png

Or it can be run using a directory, only including the image files found:

    python notename.py name --dir path/to/some/directory

The result is a pdf with the name 'name' in the current working directory.
