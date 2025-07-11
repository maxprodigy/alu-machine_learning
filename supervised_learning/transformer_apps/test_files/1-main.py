#!/usr/bin/env python3

Dataset = __import__('1-dataset').Dataset
import tensorflow as tf

data = Dataset()
for pt, en in data.data_train.take(1):
    print(data.encode(pt, en))
for pt, en in data.data_valid.take(1):
    print(data.encode(pt, en))
