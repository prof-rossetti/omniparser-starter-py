import os

from omniparser.stock_prices_parser import calculate_latest_closing_price_from_json

def test_latest_closing_price():
    aapl_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices_aapl.json")
    assert calculate_latest_closing_price_from_json(aapl_filepath) == "190.1500"

    goog_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices_goog.json")
    assert calculate_latest_closing_price_from_json(goog_filepath) == "1066.0400"

    msft_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices_msft.json")
    assert calculate_latest_closing_price_from_json(msft_filepath) == "131.4000"
