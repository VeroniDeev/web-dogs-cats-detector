from tensorflow.keras.models import load_model

def load_model():
    model = load_model("cats_and_dogs_small_1.h5")
    return model