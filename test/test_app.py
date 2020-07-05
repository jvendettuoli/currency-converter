from unittest import TestCase
from flask import Flask, request, render_template, redirect
from flask import session
from flask_debugtoolbar import DebugToolbarExtension
from currency_converter import currencies
from currency_converter.app import app


app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):

    def test_home_page(self):
        """Test if homepage shows initial HTML, and notice if there is no conversion session data."""
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Currency Converter</h1>', html)

            with client.session_transaction() as session:
                session['prev_conversion'] = False
            res = client.get('/')
            self.assertIn(
                '<p>No conversion has been requested this session.</p>', html)

    def test_convert_curr(self):
        """Test if convert route redirects"""
        with app.test_client() as client:
            res = client.get(
                '/convert?from-currency=EUR&to-currency=IDR&amount=100')
            self.assertEqual(res.status_code, 302)

    def test_convert(self):
        """Test if convert function returns dictionary of conversion values"""
        with app.test_client() as client:
            requests = {
                'from-currency': 'EUR', 'to-currency': 'IDR', 'amount': '100'}
            self.assertEqual(currencies.convert(requests), {
                'from_curr': 'EUR', 'to_curr': 'IDR', 'amount_in': '100', 'converted_amount': '1628602.00', 'in_symbol': '€', 'converted_symbol': 'Rp'})
