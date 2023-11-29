from tensorflow.keras import layers, Sequential
from tensorflow.keras.optimizers import Adam 
from tensorflow.keras.models import load_model

def build_model():
    model = Sequential()
    model.add(layers.Rescaling(1./255))
    model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(150, 150, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation="relu"))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation="relu"))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation="relu"))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(512, activation="relu"))
    model.add(layers.Dense(1, activation="relu"))
    model.build(input_shape=(20, 150, 150, 3))

    model.compile(
    optimizer=Adam(learning_rate=1e-4),
    loss="binary_crossentropy",
    metrics=["acc"]
    )

    return model


def load_model():
    model = load_model("cats_and_dogs_small_1.h5")
    return model