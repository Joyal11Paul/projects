import finnhub
finnhub_client = finnhub.Client(api_key="cub7alhr01qsc2sl2eigcub7alhr01qsc2sl2ej0")

top_30_sp500_symbols = [
    "AAPL",  # Apple Inc.
    "MSFT",  # Microsoft Corporation
    "GOOGL", # Alphabet Inc.
    "AMZN",  # Amazon.com, Inc.
    "BRK.B", # Berkshire Hathaway Inc.
    "NVDA",  # NVIDIA Corporation
    "META",  # Meta Platforms, Inc.
    "TSLA",  # Tesla, Inc.
    "JNJ",   # Johnson & Johnson
    "PG",    # Procter & Gamble Co.
    "UNH",   # UnitedHealth Group Incorporated
    "V",     # Visa Inc.
    "JCI",   # Johnson Controls International plc
    "HD",    # Home Depot, Inc.
    "PFE",   # Pfizer Inc.
    "CVX",   # Chevron Corporation
    "XOM",   # Exxon Mobil Corporation
    "ABBV",  # AbbVie Inc.
    "ABT",   # Abbott Laboratories
    "MRK",   # Merck & Co., Inc.
    "KO",    # Coca-Cola Company
    "PEP",   # PepsiCo, Inc.
    "MCD",   # McDonald's Corporation
    "WMT",   # Walmart Inc.
    "INTC",  # Intel Corporation
    "CSCO",  # Cisco Systems, Inc.
    "VZ",    # Verizon Communications Inc.
    "T",     # AT&T Inc.
    "LMT"    # Lockheed Martin Corporation
]

mine = []

for names in range(25):
    metrics = finnhub_client.company_basic_financials(top_30_sp500_symbols[names], 'all')["metric"]["currentRatioQuarterly"]
    mine.append(metrics)
    
print(max(mine))
print(min(mine))