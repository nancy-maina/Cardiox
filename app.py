#from pyexpat import model
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import matplotlib as plt

from keras.utils import load_img, img_to_array
from keras.applications import vgg16

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def hello_world():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def predict():
    model = vgg16.VGG16(
            include_top=True,
            weights="imagenet",
            input_tensor=None,
            input_shape=None,
            pooling=None,
            classes=1000,
            classifier_activation="softmax",
        )

    imagefile = request.files["imagefile"]
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)

    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    yhat = model.predict(image)
    label = vgg16.decode_predictions(yhat)
    label = label[0][0]

    classification = '%s (%.2f)' % (label[1], label[2]*100)


    return render_template("index.html", prediction =classification)


if __name__ == '__main__':
    app.run()