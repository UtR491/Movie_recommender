import numpy as np
from flask import Flask, jsonify, request, render_template
import pickle
import pandas as pd
import Untitled
import sys
from sklearn.externals import joblib
import json

app=Flask(__name__)
#model= pickle.load('movie_recommender.pkl')

@app.route('/query')
def query():
    book=request.args.get('book')
    return jsonify(book=book)


@app.route('/predict', methods=['GET'])
def predict():
    book=request.args.get('book')
    #print(type(movies))
    #print(movies)
    #query=pd.DataFrame(movies)
    #print(query.shape)
    #query=pd.get_dummies(query_df)
    recommendations=Untitled.recommender(book)
    recommendations=json.dumps(recommendations)
    print(type(recommendations))
    rec=json.loads("[]")
    rec=json.loads(recommendations)
    recommendations=""
    return rec

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    model = joblib.load("book_recommender.pkl") # Load "model.pkl"
    print ('Model loaded')
    #model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    #print ('Model columns loaded')

    app.run(port=port, debug=True)
