import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import load_model
from app import app

def panel():
    first_arg = sys.argv[1]
    if first_arg == "help":
        print("voici")
    elif first_arg == "run":
        model = load_model("cats_and_dogs_small_1.h5")
        # model = "salut"
        app.run(model)
    else:
        print("Erreur")

if __name__ == "__main__":
    panel()