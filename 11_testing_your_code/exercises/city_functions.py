def get_formatted_city_country(city_name, country_name, population=""):
    """Return a neatly formated City, Country - Population."""
    if population:
        city_country = f"{city_name}, {country_name} - population {population}"
    else:
        city_country = f"{city_name}, {country_name}"
    return city_country.title()