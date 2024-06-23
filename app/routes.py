# app/routes.py
from flask import render_template, request, redirect, url_for
from app import app
from vat_rates import VAT_RATES


def calculate_vat(prices, countries):
    results = {}
    for price, country in zip(prices, countries):
        country = country.title()
        if country in VAT_RATES:
            vat_rate = VAT_RATES[country]
            vat_amount = price * vat_rate
            results[country] = vat_amount
        else:
            results[country] = "VAT rate not available"
    return results


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prices = request.form.get('prices')
        countries = request.form.getlist('countries')

        if not prices or not countries:
            return render_template('index.html', error="Please provide both prices and select at least one country.", vat_rates=VAT_RATES.keys())

        try:
            prices = [float(price.strip()) for price in prices.split(',')]
        except ValueError:
            return render_template('index.html', error="Invalid price input. Please enter valid numbers.", vat_rates=VAT_RATES.keys())

        results = calculate_vat(prices, countries)
        return render_template('index.html', results=results, vat_rates=VAT_RATES.keys())

    return render_template('index.html', vat_rates=VAT_RATES.keys())


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/rate', methods=['GET', 'POST'])
def rate():
    if request.method == 'POST':
        country = request.form.get('country')
        if not country:
            return render_template('rate.html', error="Please provide a country.", vat_rates=VAT_RATES.keys())

        country = country.title()
        vat_rate = VAT_RATES.get(country, "VAT rate not available")
        return render_template('rate.html', vat_rate=vat_rate, country=country, vat_rates=VAT_RATES.keys())

    return render_template('rate.html', vat_rates=VAT_RATES.keys())


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        country = request.form.get('country')
        if not country:
            return render_template('search.html', error="Please provide a country.", vat_rates=VAT_RATES.keys())

        country = country.title()
        vat_rate = VAT_RATES.get(country, "VAT rate not available")
        return render_template('search.html', vat_rate=vat_rate, country=country, vat_rates=VAT_RATES.keys())

    return render_template('search.html', vat_rates=VAT_RATES.keys())
