"""
AI engine for ReliefOn: Categorizes disaster relief requests
"""

import spacy
from transformers import pipeline

# Load small English model for NLP
nlp = spacy.load("en_core_web_sm")

# Zero-shot classification pipeline from HuggingFace
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Predefined categories for disaster requests
categories = ["food", "water", "shelter", "medicine", "rescue", "other"]

def categorize_request(text):
    """
    Categorizes a request into predefined categories
    Returns dictionary with category and confidence score
    """
    result = classifier(text, candidate_labels=categories)
    return {
        "category": result['labels'][0],
        "confidence": float(result['scores'][0])
    }

if __name__ == "__main__":
    sample_request = "Need urgent water and medical help"
    print(categorize_request(sample_request))
