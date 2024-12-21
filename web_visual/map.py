import folium

# Coordinates for Moroccan cities (latitude, longitude)
city_coords = {
    "Casablanca": (33.5731, -7.5898),
    "Marrakech": (31.6295, -7.9811),
    "Rabat": (34.0209, -6.8417),
    "Tangier": (35.7595, -5.8340),
    "Agadir": (30.4278, -9.5981),
    "Fes": (34.0331, -5.0003),
    "Oujda": (34.6828, -1.9100)
}

# Routes data
routes = [
    {"origin": "Casablanca", "destination": "Marrakech", "distance": 240},
    {"origin": "Marrakech", "destination": "Rabat", "distance": 330},
    {"origin": "Tangier", "destination": "Rabat", "distance": 250},
    {"origin": "Tangier", "destination": "Casablanca", "distance": 340},
    {"origin": "Casablanca", "destination": "Agadir", "distance": 460},
    {"origin": "Rabat", "destination": "Fes", "distance": 210},
    {"origin": "Oujda", "destination": "Marrakech", "distance": 870}
]

# Create a Folium map centered on Morocco
map_morocco = folium.Map(location=[32.0, -6.0], zoom_start=6)

# Add cities as markers
for city, coords in city_coords.items():
    folium.Marker(coords, popup=city, icon=folium.Icon(color="blue")).add_to(map_morocco)

# Add routes as lines
for route in routes:
    origin_coords = city_coords[route['origin']]
    destination_coords = city_coords[route['destination']]
    folium.PolyLine([origin_coords, destination_coords], color="green", weight=2.5, opacity=1).add_to(map_morocco)

# Save the map to an HTML file
map_morocco.save("templates/map.html")
