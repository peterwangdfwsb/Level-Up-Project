from flask import Flask,render_template,request,send_file,send_from_directory,jsonify,request
import numpy as np
import spacy
import re
from grammar_1 import grammar
import pandas as pd
import matplotlib
import pickle
matplotlib.use('WebAgg')








app = Flask(__name__,static_folder='static',template_folder='templates')
en_nlp = spacy.load("en_core_web_sm")


@app.route('/',methods=['POST','GET'])
def main():
  if request.method=='GET':
    return render_template('index.html')


@app.route('/test_1',methods=['POST','GET'])
def get_table():
    test=request.get_json(force=True)
    sentence = test['text_json']
    my_dict = {}
    sentence_1 = sentence.split(".")
    test_1 = [re.sub('\s+', ' ', i) for i in sentence_1]
    test_2 = [i.lstrip().replace("’s", " is").replace("n’t", " not") for i in test_1]
    result = [grammar(i) for i in test_2 if grammar(i) != {}]
    for d in result:
      for key, val in d.items():
        if key not in my_dict:
          my_dict[key] = val
        else:
          my_dict[key] += val

    #new function
    for i in my_dict:
        my_dict[i] = list(dict.fromkeys(my_dict[i]))

    for key in my_dict:
        str_1 = ''
        for i in my_dict[key]:
            str_1 += i + ', '

        str_1=str_1[:-2]
        my_dict[key] = str_1

    df = pd.read_csv("./levelup.csv")

    dict_test = {}
    for i in range(len(df['key'])):
        cache = []
        if df['key'][i] in my_dict:
            cache.append(my_dict[df['key'][i]])
            cache.append(str(df['level_path'][i]))
            cache.append(df['value'][i])
            dict_test[df['key'][i]] = cache

    with open('cache.pickle', 'wb') as handle:
        pickle.dump(dict_test, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print(my_dict)
    print(dict_test)
    return jsonify(dict_test)



@app.route('/bubble_backend',methods=['POST','GET'])
def draw_bubble():
    if request.method == 'GET':
        #cat = {'A1_1': ['hot and humid', 1, 'A-->B | and-->as well as | CC JJ CC'],
               #'C2_13': ['even better', -1, 'C-->B | better --> good | use even']}
        with open('cache.pickle', 'rb') as handle:
            cat = pickle.load(handle)

        return jsonify(cat)


@app.route('/pie_backend', methods=['POST', 'GET'])
def draw_pie():
    if request.method == 'GET':
        #cat = {'A1_1': ['hot and humid', 1, 'A-->B | and-->as well as | CC JJ CC'],
               #'C2_13': ['even better', -1, 'C-->B | better --> good | use even']}
        with open('cache.pickle', 'rb') as handle:
            cat = pickle.load(handle)

        return jsonify(cat)

if __name__=='__main__':
  app.run()

