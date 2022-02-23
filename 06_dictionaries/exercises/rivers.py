# Dictionary containing some major rivers
# and the country each river runs through.
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

# loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

# loop to print the name of each river included in the dictionary
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f" - {river.title()}")

# loop to print the name of each country included in the dictionary
print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")
