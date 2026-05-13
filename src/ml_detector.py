import joblib


class AIMisinformationDetector:
    def __init__(self):
        self.model = joblib.load("models/aegis_logistic_model_improved.pkl")
        self.vectorizer = joblib.load("models/aegis_tfidf_vectorizer_improved.pkl")

    def predict(self, text: str):
        text_vector = self.vectorizer.transform([text])

        prediction = self.model.predict(text_vector)[0]
        probabilities = self.model.predict_proba(text_vector)[0]

        misinformation_confidence = float(probabilities[1])

        if prediction == 1 or misinformation_confidence >= 0.45:
            return {
                "ai_flag": True,
                "ai_label": "Potential Misinformation",
                "ai_confidence": misinformation_confidence
            }
        else:
            return {
                "ai_flag": False,
                "ai_label": "Likely Reliable",
                "ai_confidence": misinformation_confidence
            }