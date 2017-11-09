from skimage.io import imread
from skimage.io import imsave
from skimage.transform import resize
from matplotlib import pyplot as plt
import os

train = open("val.txt", "r+")

def process(file_):
	im = imread(file_)
	image = resize(im, (224, 224))
	output = file_.split("/")
	fname = os.path.join("val", output[2], output[3])
	imsave(fname,image)

for line in train:
	values = line.split()[0]
	process(values)
