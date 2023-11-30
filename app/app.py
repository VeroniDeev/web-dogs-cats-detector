from flask import Flask, render_template, request
from PIL import Image
from io import BytesIO
from tensorflow.keras.utils import img_to_array
from models.predict import predict
import numpy as np
import base64

app = Flask(__name__)

labels = ["cat", "dog"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Aucun fichier trouvé !'

    file = request.files['file']

    if file.filename == '':
        return 'Aucun fichier sélectionné !'

    if file:
        image_bytes = file.read()
        
        img = Image.open(BytesIO(image_bytes))

        img_resized = img.resize((150, 150))

        img_to_arr = img_to_array(img_resized)

        img_to_arr = np.expand_dims(img_to_arr, axis=0)

        prediction = predict(model, img_to_arr)[0][0]

        label = labels[round(prediction)]

        img_base64 = base64.b64encode(image_bytes).decode("utf-8")

        if prediction < 0.5:
            prediction = 1 - prediction

        return render_template("predict.html", score=str(round(prediction * 100)), label=label, image=img_base64)

def run(load_model):
    global model
    model = load_model
    app.run(debug=True)