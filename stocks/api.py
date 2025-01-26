import finnhub, json, time, webbrowser
import pandas as pd

finnhub_client = finnhub.Client(api_key="cub7alhr01qsc2sl2eigcub7alhr01qsc2sl2ej0")

def grab_info():
    data = finnhub_client.stock_symbols('US')
    with open("info.json", "w") as f:
        json.dump(data, f, indent=4)

with open("info.json") as f:
    context = json.load(f)

info = []

for stock in range(50):    
    name = context[stock]["displaySymbol"]
    data = finnhub_client.quote(name)
    metrics = finnhub_client.company_basic_financials(name, 'all')["metric"]
    
    try:
        if metrics["52WeekLow"] * 3 < metrics["52WeekHigh"]:
            info.append({
                "Name": name,
                "Current Price" : data['c'],
                "Daily Low": data['h'],
                "Daily High": data['l'],
                "52 Week High": metrics["52WeekHigh"],
                "52 Week Low": metrics["52WeekLow"],
            })
    except KeyError:
        pass
    
    time.sleep(0.5)

info = tuple(info)
df = pd.DataFrame(info)

print("\n", df, "\n")

time.sleep(5)

for tabs in info:
    webbrowser.open(f"https://finance.yahoo.com/quote/{tabs["Name"]}/")
    time.sleep(1)
    break
