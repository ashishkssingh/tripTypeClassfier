import processing
import json
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
  inputValue = request.json['value']
  triptype = processing.predict(inputValue)
  return jsonify({'triptype':triptype})

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.json['check']
      
      recommendedProducts = processing.recommendProducts(result)
      
      return jsonify({'products':recommendedProducts})
    
if __name__ == "__main__":
  app.run(debug=True)