import ast

def get_kms(route):
    # Gets the kilometers from a route
    return route["features"][0]["properties"]["segments"][0]["distance"]

def get_coordinates_route(route):
    # Get the coordinates from the route to draw it in the map
    return route["features"][0]["geometry"]["coordinates"]

def drop_zeros(s):
    # Eliminates the zeros from a series so when we do min() we don't get the same location
    return s[s != 0]

def get_coordinates(location):
    # Get the coordinates from a geolocated location. Returns a tuple with the coordinates
    return (location.latitude, location.longitude)

def coordinates_dict(coordinates_string):
    #Takes a string with the coorinates and returns a dictionary with the format {"latitude": float, "longitude": float}
    
    coordinate_tuple = ast.literal_eval(coordinates_string)

    return {"latitude": coordinate_tuple[0], "longitude": coordinate_tuple[1]}

def predetection_errors(geolocated_list):
    # Check for nan values and for repeated directions

    coordinates = [get_coordinates(l) for l in geolocated_list]

    if len(coordinates) != len(set(coordinates)):
        print(len(coordinates))
        print(len(list(set(coordinates))))
        
        # The list comprehension returns the coordinates and the position in the list of the location that is repeated
        duplicates = [(x, i) for x, i in enumerate(coordinates) if coordinates.count(x) > 1]
        print(f"Repeated values: {duplicates}")

        raise ValueError("The geolocated list has repeated values")
    
    print("Geolocated list without errors!")