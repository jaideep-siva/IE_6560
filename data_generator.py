import pandas as pd

# Generating a random data set 
data = {
    'location': [
        'Detroit', 'Ann Arbor', 'Grand Rapids', 'Mackinac Island', 'Traverse City', 'Lansing',
        'Holland', 'Saugatuck', 'Frankenmuth', 'Petoskey', 'Marquette', 'Kalamazoo',
        'Bay City', 'Flint', 'Muskegon', 'Sault Ste. Marie', 'Alpena', 'Battle Creek',
        'Charlevoix', 'Houghton'
    ],
    'description': [
        'Major city known for its automotive history.',
        'City with a vibrant arts scene and the University of Michigan.',
        'City with a rich history and many breweries.',
        'Island known for its fudge, forts, and biking.',
        'City famous for its wineries and cherry festival.',
        'Capital city with many government buildings and museums.',
        'City known for its Dutch heritage and tulip festival.',
        'Resort town known for its beaches and art galleries.',
        'City known for its Bavarian-style architecture.',
        'City with beautiful waterfront and Victorian architecture.',
        'City known for its scenic beauty and outdoor activities.',
        'City with a vibrant arts scene and historic downtown.',
        'City with a rich maritime history.',
        'City known for its automotive industry history.',
        'City known for its beautiful lakeshore and outdoor activities.',
        'City with a rich history and access to Lake Superior.',
        'City known for its maritime heritage and lighthouses.',
        'City known for its cereal production and historic sites.',
        'City known for its charming downtown and lakefront.',
        'City known for its proximity to Lake Superior and outdoor activities.'
    ],
    'cost': [
        200, 150, 180, 250, 220, 160, 140, 130, 170, 210, 240, 180, 170, 150, 200, 230,
        160, 190, 220, 250
    ],
    'satisfaction': [
        85, 90, 88, 92, 91, 87, 89, 86, 88, 90, 93, 89, 87, 85, 90, 92, 86, 88, 91, 94
    ],
    'travel_time': [
        0, 1, 2, 3, 4, 2, 3, 2, 1, 3, 5, 2, 3, 1, 3, 4, 4, 2, 3, 5
    ],
    'latitude': [
        42.3314, 42.2808, 42.9634, 45.8483, 44.7631, 42.7325, 42.7875, 42.6544, 43.3317, 45.3734,
        46.5476, 42.2917, 43.5945, 43.0125, 43.2342, 46.4953, 45.0617, 42.3212, 45.3186, 47.1211
    ],
    'longitude': [
        -83.0458, -83.7430, -85.6681, -84.6162, -85.6206, -84.5555, -86.1089, -86.2016, -83.7385, -84.9553,
        -87.3956, -85.5872, -83.8889, -83.6875, -86.2484, -84.3453, -83.4328, -85.1797, -85.2586, -88.5690
    ]
}

locations = pd.DataFrame(data)
locations.to_csv('michigan_locations.csv', index=False)