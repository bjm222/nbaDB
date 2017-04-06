import numpy as np

def linear_regression(raw_data):
    # Initialize
    y = np.zeros(len(raw_data))
    x = np.zeros([len(raw_data)])
    w = 0.0
    b = 0.0

    max_iter = 5000
    learning_rate = 0.001

    # Process raw data
    for i in range(len(raw_data)):
        y[i] = raw_data[i]['points']
        x[i] = raw_data[i]['year'] - raw_data[0]['year']

   
    # Start learning
    for i in range(max_iter):
        wg = 0.0
        bg = 0.0
        for j in range(len(y)):
            bg += -(2.0/len(y)) * (y[j] - (w*x[j] + b))
            wg += -(2.0/len(y)) * x[j] * (y[j] - (w*x[j] + b))
        b = b - learning_rate * bg
        w = w - learning_rate * wg


    prediction = w * (raw_data[len(raw_data)-1]['year'] + 1 - raw_data[0]['year']) + b

    year =  raw_data[len(raw_data)-1]['year'] + 1

    predictor = {}
    predictor['year'] = year
    predictor['points'] = prediction

    return predictor
