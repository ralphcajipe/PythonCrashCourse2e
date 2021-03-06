from city_functions import get_formatted_city_country

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give a city name: ")
    if city == 'q':
        break
    country = input("Please give the country: ")
    if country == 'q':
        break
    population = input("Please give the population: ")
    if population == 'q':
        break

    formatted_city_country = get_formatted_city_country(city, country,
                                                        population)
    print(f"\tNeatly formatted City, Country: {formatted_city_country}")
