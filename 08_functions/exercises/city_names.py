def city_country(city_name, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city_name.title()}, {country.title()}"


city = city_country('new york city', 'united states')
print(city)

city = city_country('manila', 'philippines')
print(city)

city = city_country('abu dhabi', 'united arab emirates')
print(city)
