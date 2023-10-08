import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from flask import Flask, request, jsonify
import pickle
import re

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

ps = PorterStemmer()

tfidf = pickle.load(open('model/TFIDFvectorizer.pkl', 'rb'))
model = pickle.load(open('model/bestmodel.pkl', 'rb'))


@app.route('/predict', methods=['POST'])
def predict():
    requestBody = request.json
    cleanText = clean_text(requestBody["message"])
    transformedText = transform_text(cleanText)
    vector_input = tfidf.transform([transformedText])
    result = model.predict(vector_input)[0]
    if result == 1:
        resMessage = "You are being bullied..."
    else:
        resMessage = "All good!!!"
    data = {
        "verdict" : resMessage
    }
    return jsonify(data)


def clean_text(tweet):
    # remove URL
    tweet = re.sub(r'http\S+', '', tweet)
    # Remove usernames
    tweet = re.sub(r'@[^\s]+[\s]?', '', tweet)
    # Remove hashtags
    tweet = re.sub(r'#[^\s]+[\s]?', '', tweet)
    # Remove emojis
    tweet = re.sub(r':[^\s]+[\s]?', '', tweet)
    # remove special characters
    tweet = re.sub('[^ a-zA-Z0-9]', '', tweet)
    # remove RT
    tweet = re.sub('RT', '', tweet)
    # remove Numbers
    tweet = re.sub('[0-9]', '', tweet)

    return tweet


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


if __name__ == "__main__":
    app.run(debug=True)
