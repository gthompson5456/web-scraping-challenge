{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)



@app.route("/")
def index():
    listings = mongo.db.listings.find_one()
    # listing = jsonify(listing)
    # listings = [data for data in mongo.db.listings.find()]
    # print(listing)
    return render_template("index.html", listings=listings)


@app.route("/scrape")
def scrape():
    listings = mongo.db.listings

    listings_data = scrape_mars.scrape()
    
    listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
    