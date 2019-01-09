import requests
proxies = {
    "http": "http://tx123321z@45.62.104.115:12300",
    'https': 'https://tx123321z@45.62.104.115:12300',
}
res = requests.get("https://httpbin.org/get", proxies=proxies)
print(res.status_code)

