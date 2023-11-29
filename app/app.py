from flask import Flask, render_template, request
from PIL import Image
from io import BytesIO
from tensorflow.keras.utils import img_to_array
from models.predict import predict
import numpy as np

app = Flask(__name__)

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
        # Stocker le fichier dans une variable
        image_bytes = file.read()
        
        # Utiliser Pillow pour ouvrir l'image à partir des bytes
        img = Image.open(BytesIO(image_bytes))

        # Exemple : Redimensionner l'image
        img_resized = img.resize((150, 150))

        img_to_arr = img_to_array(img_resized)

        # prediction = predict(model, img_to_arr)    
        img_to_arr = np.expand_dims(img_to_arr, axis=0)

        prediction = predict(model, img_to_arr)

        return f'Fichier téléchargé et traité avec succès ! {str(prediction)}'

def run(load_model):
    global model
    model = load_model
    app.run(debug=True)