# Simple Currency Converter with hardcoded exchange rates

# Hardcoded exchange rates (Base currency is USD)
exchange_rates = {
    'USD': 1.0,    # US Dollar
    'EUR': 0.92,   # Euro
    'GBP': 0.78,   # British Pound
    'JPY': 138.95, # Japanese Yen
    'INR': 82.43,  # Indian Rupee
    'AUD': 1.55,   # Australian Dollar
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates:
        # Convert the amount from the base currency to the target currency
        base_amount = amount / exchange_rates[from_currency]  # Convert from 'from_currency' to USD
        converted_amount = base_amount * exchange_rates[to_currency]  # Convert from USD to 'to_currency'
        return converted_amount
    else:
        return None

def main():
    print("Available currencies:", ", ".join(exchange_rates.keys()))
    
    from_currency = input("Enter the currency you want to convert from (e.g., USD, EUR, GBP): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., USD, EUR, GBP): ").upper()
    amount = float(input(f"Enter the amount in {from_currency}: "))
    
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency code.")
        return
    
    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Error in conversion.")

if __name__ == "__main__":
    main()
