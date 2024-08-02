import joblib

# Load your pre-trained model
model = joblib.load('app/models/classifier_model.pkl')

def classify_text(text: str) -> str:
    return model.predict([text])[0]
