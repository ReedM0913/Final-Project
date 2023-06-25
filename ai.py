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

pet_counter = 0
pet_dictionary = {"dog": 0, "cat": 0}

if "pet" or "Pet" in class_desc:
    pet_counter += 1
    if "dog" in class_desc:
        pet_dictionary["dog"] += 1
    elif "cat" in class_desc:
        pet_dictionary["cat"] += 1


print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))
