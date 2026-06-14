# Spam Message Detection

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    "message": [
        "Congratulations! You won a free ticket",
        "Call now to claim your prize",
        "Hello friend how are you",
        "Let's meet tomorrow",
        "Win money now",
        "Important update about your account",
        "Free entry in a contest",
        "Are you coming to class today"
    ],
    "label": [
        "spam",
        "spam",
        "ham",
        "ham",
        "spam",
        "ham",
        "spam",
        "ham"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert labels into numbers
df["label_num"] = df.label.map({"ham": 0, "spam": 1})

# Input and Output
X = df["message"]
y = df["label_num"]

# Convert text into vectors
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Test custom message
while True:
    msg = input("\nEnter a message: ")

    if msg.lower() == "exit":
        print("Program closed.")
        break

    msg_vector = vectorizer.transform([msg])
    prediction = model.predict(msg_vector)

    if prediction[0] == 1:
        print("Spam Message ")
    else:
        print("Not Spam ")