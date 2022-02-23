def make_shirt(size, message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print(f"I'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"\n')


make_shirt('large')
make_shirt('medium')
make_shirt(size='small', message="I love Python3's f-strings!")
make_shirt('small', "I love Python3's f-strings!")
