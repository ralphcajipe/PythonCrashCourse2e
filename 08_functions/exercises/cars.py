def make_car(manufacturer, model, **options):
    """make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        # add new key-value pair
        car_dict[option] = value

    return car_dict


my_model_s = make_car('tesla', 'model s', color='gray', autopilot=True)
print(my_model_s)

my_old_x = make_car('tesla', 'model x', year=2021, color='white',
                    headlights='popup')
print(my_old_x)
