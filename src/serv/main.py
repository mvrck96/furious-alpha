from os import getenv

import requests

from dotenv import load_dotenv
from fastapi import FastAPI


load_dotenv()
app = FastAPI()

YAHOO_URL = "https://yfapi.net/v8/finance/spark"
YAHOO_TOKEN = getenv("YAHOO_TOKEN")


@app.get("/history")
def test(ticker: str = None):
    querystring = {"symbols": ticker}
    headers = {"x-api-key": YAHOO_TOKEN}
    res = requests.request(
        "GET", YAHOO_URL, headers=headers, params=querystring
    )
    return res.text
