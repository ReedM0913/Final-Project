#!/usr/bin/python3
import jetson.inference
import jetson.utils

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
opt = parser.parse_args()


img = jetson.utils.loadImage(opt.filename)

net = jetson.inference.imageNet(argv=['--model=models/dayornight/resnet18.onnx', '--input-blob=input_0', '--output_blob=output_0', '--labels=data/dayornight/labels.txt'])

class_idx, confidence = net.Classify(img)

class_desc = net.GetClassDesc(class_idx)
if class_idx == 0:
    class_desc="Day"
elif class_idx == 1:
    class_desc="Night"  
else:
    class_desc="other"




print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))
