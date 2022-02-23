def describe_city(city, country='united states'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)


describe_city('austin')
describe_city('manila', 'philippines')
describe_city('miami')