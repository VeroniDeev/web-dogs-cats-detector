def predict(model, data):
    prediction = model.predict(data, verbose=0)
    return prediction