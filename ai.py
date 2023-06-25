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

bear_counter = 0
bear_dictionary = {"black bear": 0, "brown bear": 0}

if "bear" or "Bear" in class_desc:
    bear_counter += 1
    if "black bear" in class_desc:
        bear_dictionary["black bear"] += 1
    elif "brown bear" in class_desc:
        bear_dictionary["brown bear"] += 1


print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))
