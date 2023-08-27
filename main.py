import requests
from bs4 import BeautifulSoup
import pandas as pd

def search_price(product_name):
  """Searches for the price of a product on a few notable websites."""
  prices = []
  websites = ["amazon.com", "walmart.com", "target.com", "bestbuy.com"]
  for website in websites:
    response = requests.get(website + "/product/" + product_name)
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find("span", class_="price").text
    prices.append(price)
  return prices

def compare_prices(prices):
  """Compares the prices of different products and returns the best deal."""
  best_deal = prices[0]
  for price in prices:
    if price < best_deal:
      best_deal = price
  return best_deal

def display_best_deal(product_name, best_deal):
  """Displays the best deal for a product."""
  print("The best deal for {} is {} on {}".format(product_name, best_deal, websites[prices.index(best_deal)]))

if __name__ == "__main__":
  product_name = input("Enter the product name: ")
  prices = search_price(product_name)
  best_deal = compare_prices(prices)
  display_best_deal(product_name, best_deal)
