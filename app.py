import processing
import json
from pandas.io.json import json_normalize
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
  
  product, count = processing.get_top_10_items()
  count = '*'.join(str(x) for x in count.to_list())
  return render_template("index.html", product = "*".join(product.to_list()), count = count)

@app.route('/recommendation.html')
def renderRecommendationPage():
  return render_template("recommendation.html")

@app.route('/classifier.html')
def classifier():
  return render_template("classifier.html")

@app.route('/predict',methods = ['POST', 'GET'])
def predict():
  inputValue = json_normalize(request.json['value'])
  print(inputValue.values.tolist())
  triptype = processing.predict(inputValue)
  print(triptype.tolist())
  return json.dumps(triptype.tolist())

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.json['check']
      
      recommendedProducts = processing.recommendProducts(result)
      
      return jsonify({'products':recommendedProducts})
    
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80,debug=True)