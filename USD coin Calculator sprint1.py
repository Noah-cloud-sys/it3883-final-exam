# coin values in USD
COIN_VALUES = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25
}

# Converting plural coin names to them to singular
PLURAL_FORMS = {
    'pennies': 'penny',
    'nickels': 'nickel',
    'dimes': 'dime',
    'quarters': 'quarter'
}

def calculate_total(input_string):
    total = 0.0
    coin_parts = input_string.lower().split(" and ")

    for group in coin_parts:
        parts = group.strip().split()
        if len(parts) != 2:
            continue  # Ignore misspellings
        quantity = int(parts[0])
        coin_name = PLURAL_FORMS.get(parts[1], parts[1])
        if coin_name in COIN_VALUES:
            total += quantity * COIN_VALUES[coin_name]
    
    return round(total, 2)

# Example for testing
if __name__ == "__main__":
    user_input = "1 dime and 1 nickel and 1 penny and -1 quarter"
    print(f"${calculate_total(user_input):.2f}")
