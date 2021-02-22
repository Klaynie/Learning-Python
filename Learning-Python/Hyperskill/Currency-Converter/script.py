conicoins_amount = float(input())
conversion_rates = {
    "RUB": 2.98,
    "ARS": 0.82,
    "HNL": 0.17,
    "AUD": 1.9622,
    "MAD": 0.208
}
for currency, rate in conversion_rates.items():
    print(
        f"I will get {(conicoins_amount * rate):.2f} {currency} from the sale of {conicoins_amount} conicoins.")
