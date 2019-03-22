import flask
from flask import Flask, render_template, request
import numpy as np
from scipy import ndimage
from scipy import misc
from keras.models import load_model, model_from_json
import os
import json
from matplotlib import pyplot as plt
from PIL import Image
import tensorflow as tf

app = Flask(__name__)

graph = tf.get_default_graph()

# Load in our model
model = model_from_json(open("./model.json").read())
model.load_weights("./model.h5")


@app.route('/')
def index():
    return "<html><pre>" + open("./README.md").read() + "</pre></html>"


@app.route('/predict', methods=["POST"])
def predict():
    global graph
    imagefile = flask.request.files.get('imagefile', '')

    # P.S. this isn't secure for public facing stuff
    filepath = "./uploads/" + imagefile.filename
    imagefile.save(filepath)

    img = np.array(Image.open(filepath).convert("L").resize((64,64)).getdata())

    img = img.reshape((64,64,1))

    # plt.imshow(img.reshape((64,64)))

    with graph.as_default():
        output = model.predict(img.reshape(1,64,64,1)).reshape((6,6))

    # plt.imshow(output)

    (yi,xi) = ndimage.center_of_mass(output)

    x,y = (xi / 5, yi / 5)

    os.remove(filepath)

    return json.dumps({"x": x, "y": y})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
