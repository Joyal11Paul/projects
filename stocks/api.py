import finnhub, json, time, webbrowser
import pandas as pd

finnhub_client = finnhub.Client(api_key="cub7alhr01qsc2sl2eigcub7alhr01qsc2sl2ej0")

def grab_info():
    data = finnhub_client.stock_symbols('US')
    with open("jsons_needed/info.json", "w") as f:
        json.dump(data, f, indent=4)
#grab_info()

with open("jsons_needed/info.json") as f:
    context = json.load(f)

info = []

with open("my_texts/range.txt") as f:
    my_range_1 = "".join(f.readlines(1))
    my_range_2 = "".join(f.readlines(2))



### Adding Wanted Stocks ###
for stock in range(int(my_range_1), int(my_range_2)):    
    name = context[stock]["displaySymbol"]
    data = finnhub_client.quote(name)
    metrics = finnhub_client.company_basic_financials(name, 'all')["metric"]
    '''
    with open("facts.json", "w") as f:
        json.dump(name, fp = f, indent=4)
        json.dump(data, fp = f, indent=4)
        json.dump(metrics, fp = f, indent=4)
    ''' 
    
    try:
        if metrics["monthToDatePriceReturnDaily"] >= -10 and metrics["5DayPriceReturnDaily"] <= -2.5 and metrics["marketCapitalization"] >= 1_000 and data['c'] != 0:
            info.append({
                "Name": name,
                "Current Price" : data['c'],
                "Daily Low": data['h'],
                "Daily High": data['l'],
                "52 Week High": metrics["52WeekHigh"],
                "52 Week Low": metrics["52WeekLow"],
                "5 Day Price Return": metrics["5DayPriceReturnDaily"],
                "Month Price Return": metrics["monthToDatePriceReturnDaily"],
                "Market Cap (Billions)": metrics["marketCapitalization"] / 1000
            })
            
    except KeyError:
        pass
    except TypeError:
        pass
    
    time.sleep(0.5)
    
with open("my_texts/range.txt", "w") as f:
    f.write(str(int(my_range_1) + 60) + '\n')
    f.write(str(int(my_range_2) + 60))

info = tuple(info)
df = pd.DataFrame(info)

if not df.empty:
    with open("my_texts/current_stock_list.txt", "a") as f:
        f.write(df.to_string())
else:
    print("This set was empty")



### Opening Tabs ###
time.sleep(5)

for tabs in info:
    webbrowser.open(f"https://finance.yahoo.com/quote/{tabs["Name"]}/chart?p={tabs["Name"]}F&interval=1mo")
    time.sleep(1)
    try:
        if tabs == info[4]:
            break
    except IndexError:
        pass
        