import json
import pandas as pd

corpus = {}

with open('app_data/corpus.json') as f:
    corpus = json.load(f)


def recommendProducts(pickedProductsArray):
    recommendedProductsArray = []

    for pickedProduct in pickedProductsArray:

        recommendedProductsArray.extend(corpus[pickedProduct])

    recommendedProductsArray = [
        pickedProduct for pickedProduct in recommendedProductsArray if pickedProduct not in pickedProductsArray]

    return list(dict.fromkeys(recommendedProductsArray))

def get_top_10_items():
  df = pd.read_csv("app_data/top10.csv")
  
  product = df["product_name"]
  count = df["count"]
  
  return product, count

def get_top_10_items_by_day(day):
  if day == "Sunday":
    df = pd.read_csv("app_data/top_ten_products_Sunday.csv")
  elif day == "Monday":
    df = pd.read_csv("app_data/top_ten_products_Monday.csv")
  elif day == "Tuesday":
    df = pd.read_csv("app_data/top_ten_products_Tuesday.csv")
  elif day == "Wednesday":
    df = pd.read_csv("app_data/top_ten_products_Wednesday.csv")
  elif day == "Thursday":
    df = pd.read_csv("app_data/top_ten_products_Thursday.csv")
  elif day == "Friday":
    df = pd.read_csv("app_data/top_ten_products_Friday.csv")
  else:
    df = pd.read_csv("app_data/top_ten_products_Sunday.csv")
    
  return json.dumps({
    "names":df["product_name"],
    "values":df["count"]
  })
    