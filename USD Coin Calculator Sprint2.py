import re

# Coin to Dollars
_DENOMINATIONS = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25
}

def _singularize(coin_word: str) -> str:
    """
    Convert plural forms like 'pennies' or regular plurals ending in 's'
    back to their singular form.
    """
    if coin_word.endswith('ies'):
        return coin_word[:-3] + 'y'   # pennies to penny
    if coin_word.endswith('s'):
        return coin_word[:-1]         # nickels to nickel
    return coin_word                  

def convert_to_dollars(description: str) -> float:
    """
    Scan the input string for patterns "<number> <coin>" and sum their values.
    Ignores any segments that don't match or coins we don't recognize.
    """
    total = 0.0
    description = description.lower()
    # Find all occurrences of a number followed by a word
    tokens = re.findall(r'(\d+)\s+([a-z]+)', description)

    for quantity_str, coin_str in tokens:
        qty = int(quantity_str)
        coin = _singularize(coin_str)
        value = _DENOMINATIONS.get(coin)
        if value:
            total += qty * value

    # Round to two decimal places
    return round(total, 2)

if __name__ == '__main__':
    examples = [
        "1 penny and 2 nickels",
        "4 dimes and 7 quarters",
        "1 quarter and 3 pennies",
        "21 pennies and 17 dimes and 52 quarters",
        "95 dimes and 73 quarters and 22 nickels and 36 pennies",
        "2 QuArTeRs and 3 PENNIES",
        "10 nickels and KSU ROCKS",
        "5 pennies and -3 dimes",
        
    ]
    for ex in examples:
        amount = convert_to_dollars(ex)
        print(f"Input: {ex!r} → ${amount:.2f}")
