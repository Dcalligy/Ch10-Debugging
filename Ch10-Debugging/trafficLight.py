#! python3
# Ch.10 Debugging - Using an Assertion in a Traffic Light Simulation (pg. 219-220)

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    return stoplight
    #assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
    
# Switching the parameter to mission_16th should give us the opposite output 
stoplight = switchLights(market_2nd)
switchLights(market_2nd)
assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
print(str(stoplight.values()))

stoplight = switchLights(mission_16th)
switchLights(mission_16th)
assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
print(str(stoplight.values()))