# vat_calculator.py
from vat_rates import VAT_RATES


def calculate_vat(prices, countries):
    results = {}
    for price, country in zip(prices, countries):
        country = country.title()
        if country in VAT_RATES:
            vat_rate = VAT_RATES[country]
            vat_amount = price * vat_rate
            results[country] = vat_amount
        else:
            results[country] = "VAT rate not available"
    return results


def get_vat_rate(country):
    country = country.title()
    return VAT_RATES.get(country, "VAT rate not available")


def main():
    print("""
    ******************************************
    *       Welcome to the VAT Calculator    *
    *            for African Countries       *
    ******************************************
    """)

    while True:
        choice = input(
            "Enter 1 to calculate VAT, 2 to get VAT rate, or 3 to exit: ")
        if choice == '1':
            prices = input("Enter prices separated by commas: ").split(',')
            prices = [float(price) for price in prices]
            countries = input(
                "Enter countries separated by commas: ").split(',')
            results = calculate_vat(prices, countries)
            for country, vat in results.items():
                print(f"VAT amount for {country}: {vat}")
        elif choice == '2':
            country = input("Enter country: ")
            vat_rate = get_vat_rate(country)
            print(f"VAT rate for {country}: {vat_rate}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
