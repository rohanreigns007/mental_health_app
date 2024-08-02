import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_classifier():
    # Load dataset
    data = pd.read_csv('data/mental_health_dataset.csv')

    # Preprocessing
    X = data['text']
    y = data['label']
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model training
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Save model and vectorizer
    joblib.dump(model, 'app/models/classifier_model.pkl')
    joblib.dump(vectorizer, 'app/models/vectorizer.pkl')

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model accuracy: {accuracy}')
