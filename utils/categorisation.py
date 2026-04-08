def categorise_transaction(description):
    description = description.lower()

    rules = {
        "groceries": ["tesco", "asda", "aldi", "sainsbury"],
        "entertainment": ["netflix", "spotify", "cinema"],
        "transport": ["uber", "trainline", "tfl", "bus"],
        "rent": ["rent", "landlord"],
        "utilities": ["british gas", "edf", "octopus"],
        "subscriptions": ["netflix", "spotify", "amazon prime"]
    }

    for category, keywords in rules.items():
        if any(keyword in description for keyword in keywords):
            return category

    return "other"
