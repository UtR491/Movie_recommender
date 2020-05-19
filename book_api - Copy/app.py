from flask import Flask, jsonify, request, render_template
import Untitled
import sys
import joblib
import json
import os

app=Flask(__name__)
#model= pickle.load()

@app.route('/')
def home():
    print('home')
    return "Hi"

# @app.route('/query')
# def query():
#     book=request.args.get('book')
#     return jsonify(book=book)


@app.route('/predict', methods=['GET'])
def predict():
    book=request.args.get('book')
    recommendations=Untitled.recommender(book)
    recommendations=json.dumps(recommendations)
    print(type(recommendations))
    rec=json.loads("[]")
    rec=json.loads(recommendations)
    recommendations=""
    return rec

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))    
    app.run(port=port, debug=True)
