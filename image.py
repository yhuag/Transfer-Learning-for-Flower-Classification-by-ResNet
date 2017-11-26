from skimage.io import imread
from skimage.io import imsave
from skimage.transform import resize
from matplotlib import pyplot as plt
import os

FILE_NAME = "val.txt"

file = open(FILE_NAME, "r+")

def process(file_):
	im = imread(file_)
	image = resize(im, (224, 224))
	output = file_.split("/")
	fname = os.path.join("val", output[2], output[3])
	imsave(fname,image)

for line in file:
	values = line.split()[0]
	process(values)
