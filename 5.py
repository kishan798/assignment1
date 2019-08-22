restaurants = [[ 'Acme', 'Italian', 2, 4, 3, 5],['Flintstone', 'Steak', 5, 2, 4, 3, 3, 4],['Bella Troy', 'Italian', 1, 4, 5]]
for rest in restaurants:
    if rest[1] == 'Italian' and (1 not in rest[2:]) and (5 in rest[2:]):
        print (rest[0])
