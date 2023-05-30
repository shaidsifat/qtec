import requests
from itertools import permutations

API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"

# City Bank branch locations
branches = [
    {"id": 1, "latitude": 23.8728568, "longitude": 90.3984184, "address": "Uttara Branch"},
    {"id": 2, "latitude": 23.8513998, "longitude": 90.3944536, "address": "City Bank Airport"},
    {"id": 3, "latitude": 23.8330429, "longitude": 90.4092871, "address": "City Bank Nikunja"},
    {"id": 4, "latitude": 23.8679743, "longitude": 90.3840879, "address": "City Bank Beside Uttara Diagnostic"},
    {"id": 5, "latitude": 23.8248293, "longitude": 90.3551134, "address": "City Bank Mirpur 12"},
    {"id": 6, "latitude": 23.827149, "longitude": 90.4106238, "address": "City Bank Le Meridien"},
    {"id": 7, "latitude": 23.8629078, "longitude": 90.3816318, "address": "City Bank Shaheed Sarani"},
    {"id": 8, "latitude": 23.8673789, "longitude": 90.429412, "address": "City Bank Narayanganj"},
    {"id": 9, "latitude": 23.8248938, "longitude": 90.3549467, "address": "City Bank Pallabi"},
    {"id": 10, "latitude": 23.813316, "longitude": 90.4147498, "address": "City Bank JFP"},
]

# Calculate the distance between two locations using the Google Maps Distance Matrix API
def get_distance(origin, destination):
    print(origin)
    print(destination)
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json?"

    params = {
        "origins": f"{origin['latitude']},{origin['longitude']}",
        "destinations": f"{destination['latitude']},{destination['longitude']}",
        "key": API_KEY,
    }
    print("if you givr proper api_key it willß")
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        print(data)
        distance = data["rows"][0]["elements"][0]["distance"]["value"]
        return distance
    else:
        raise Exception("Error retrieving distance from Google Maps API.")

# Calculate the total distance of a route
def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        origin = route[i]
        destination = route[i + 1]
        distance = get_distance(origin, destination)
        total_distance += distance
    return total_distance

# Find the optimized route using TSP algorithm
def find_optimized_route(branches):
    start_branch = branches[0]
    remaining_branches = branches[1:]
    min_distance = float("inf")
    optimized_route = []

    for permutation in permutations(remaining_branches):
        route = [start_branch] + list(permutation) + [start_branch]
        total_distance = calculate_total_distance(route)
        if total_distance < min_distance:
            min_distance = total_distance
            optimized_route = route

    return optimized_route

# Print the optimized route
def print_optimized_route(route):
    print("Optimized Route:")
    for branch in route:
        print(branch["address"])

# Find the optimized route using the TSP algorithm
optimized_route = find_optimized_route(branches)

# Print the optimized route
print_optimized_route(optimized_route)
