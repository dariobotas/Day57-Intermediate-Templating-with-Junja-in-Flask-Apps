import datetime
import requests
import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  current_year = datetime.datetime.now().year
  random_number = random.randint(1, 10)
  return render_template('index.html', num=random_number, year=current_year)

@app.route("/guess/<name>")
def guess(name):
  api_link_gender = f"https://api.genderize.io?name={name}"
  gender_response = requests.get(api_link_gender)
  gender_data = gender_response.json()
  gender = gender_data['gender']
  api_link_year = f"https://api.agify.io?name={name}"
  year_response = requests.get(api_link_year)
  year_data = year_response.json()
  age = year_data['age']
  return render_template('guess.html', name=name, gender=gender, years=age)

@app.route("/blog")
def blog():
  blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
  response = requests.get(blog_url)
  all_posts = response.json()
  return render_template(
    'blog.html', posts=all_posts)


def main():
  app.run(debug=True)