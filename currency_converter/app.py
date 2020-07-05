from flask import Flask, request, render_template, redirect
from flask import session
from flask_debugtoolbar import DebugToolbarExtension
from currency_converter.currencies import SUPPORTED_CURRENCIES, convert


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Assessment3SecretKeyWowie'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True
toolbar = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """Page for inputting currency to convert from and currency
    to convert to, and amount to convert."""
    prev_conversion = session.get('prev_conversion', False)
    return render_template('index.html', currencies=SUPPORTED_CURRENCIES, prev_conversion=prev_conversion)


@app.route('/convert')
def convert_curr():
    """Convert a provided amount from one currency to another using forex_converter.CurrencyRates().convert."""
    requests = request.args
    print(requests)

    # Call convert from currencies.py
    conversion = convert(requests)

    # Store information in session for displaying after redirect
    session['prev_conversion'] = conversion

    return redirect('/')
