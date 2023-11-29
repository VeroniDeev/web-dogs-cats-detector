from tensorflow.keras.models import load_model

def predict(model, data):
    model = load_model("cats_and_dogs_small_1.h5")
    prediction = model.predict(data)
    return prediction