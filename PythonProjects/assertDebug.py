market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'

    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)
    # this means that this is an issue that must always be taken into consideration... I 'ASSERT' THIS MUST BE THE CASE
    # "sanity check"
print(market_2nd)
switchLights(market_2nd)
print(market_2nd)
