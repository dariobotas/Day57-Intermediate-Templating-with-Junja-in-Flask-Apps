import datetime
import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  year = datetime.datetime.now().year
  random_number = random.randint(1, 10)
  return render_template('index.html', num=random_number, year=year)


def main():
  app.run(debug=True)
