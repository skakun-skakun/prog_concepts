import requests
import os
from dotenv import load_dotenv
from pprint import pprint
import pandas as pd

load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5"

resp = requests.get(f"{BASE_URL}/weather?q=Kyiv&appid={API_KEY}")
print(resp.status_code)
pprint(resp.json())

