from flask import request, jsonify
from sklearn.externals import joblib
from google.cloud import storage
import pandas as pd
import requests
import traceback

client = storage.Client()
bucket = client.get_bucket('huhuhang-model')
blob = bucket.get_blob('sklearn/titanic.pkl')
with open('/tmp/titanic.pkl', 'wb') as file_obj:
    blob.download_to_file(file_obj)


def predict(request):
    try:
        json_ = request.json
        query_df = pd.DataFrame(json_)
        columns_onehot = ['pclass', 'sex_female', 'sex_male',
                          'embarked_C', 'embarked_Q', 'embarked_S']
        query = pd.get_dummies(query_df).reindex(
            columns=columns_onehot, fill_value=0)
        clf = joblib.load('/tmp/titanic.pkl')
        prediction = clf.predict(query)
        return jsonify({'prediction': list(prediction)})
    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()})
