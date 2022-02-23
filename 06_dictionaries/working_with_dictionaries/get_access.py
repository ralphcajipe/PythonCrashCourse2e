# Using get() to Access Values

alien_0 = {'color': 'green', 'speed': 'slow'}

# KeyError: 'points'
# print(alien_0['points'])

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)