import finnhub, json
finnhub_client = finnhub.Client(api_key="cualgahr01qof06ir99gcualgahr01qof06ir9a0")

def grab_info():
    data = finnhub_client.stock_symbols('US')
    with open("info.json", "w") as f:
        json.dump(data, f, indent=4)

with open("info.json") as f:
    context = json.load(f)

name = context[0]["displaySymbol"]
print(name)

with open("individual_Stats.json", "w") as f:
    data = finnhub_client.company_basic_financials(name, 'all')["metric"]
    json.dump(data, f, indent=4)
    