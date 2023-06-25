import jetson.inference
import jetson.utils

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be:  googlenet, resnet-18, ect. (see --help for others)")
opt = parser.parse_args()


img = jetson.utils.loadImage(opt.filename)

net = jetson.inference.imageNet(opt.network)

class_idx, confidence = net.Classify(img)

class_desc = net.GetClassDesc(class_idx)

day_counter = 0
day_dictionary = {"day": 0}

night_counter = 0
night_dictionary = {"night": 0}

if "day" or "Day" in class_desc:
    day_counter += 1
    elif "night" in class_desc:
        night_dictionary["night"] += 1


print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))
