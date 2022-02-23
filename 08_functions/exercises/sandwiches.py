def make_sandwich(*items):
    """make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(f"... adding {item} to your sandwich.")
    print("Your sandwich is ready!")


make_sandwich('lettuce', 'tomatoes', 'cheddar', 'chicken breast')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')
