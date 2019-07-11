<div align="center">
  <h1>🛳 Titanic Prediction</h1>
</div>

<br />

## Usage

Run `python run.py` locally to start the Flask web service, or use the Heroku API:

```python
import requests

sample = [{"pclass": 1, "sex": "male", "embarked": "C"},
          {"pclass": 2, "sex": "female", "embarked": "S"},
          {"pclass": 3, "sex": "male", "embarked": "Q"},
          {"pclass": 3, "sex": "female", "embarked": "S"}]
          
requests.post(url="https://titanic-demo.herokuapp.com", json=sample).content
```

```json
{"predict":["no","yes","no","no"]}
```
