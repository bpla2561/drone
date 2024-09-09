import re
import numpy as np
import pandas as pd
from math import radians, cos, sin, sqrt, atan2

class DronePath:
    def __init__(self, coordinates_str):
        self.coordinates_str = coordinates_str
        self._radius = 6371  # км
        self.total_distance = 0
    
    def _parse_coordinates(self):
        pairs = re.findall(r"\s*(-?\d+\.\d+),\s*(-?\d+\.\d+)\s*", self.coordinates_str)
        coordinates = []
        for pair in pairs:
            longitude, latitude = pair
            coordinates.append((float(longitude), float(latitude)))
        return np.array(coordinates)
    
    def _distance_between(self, lat1, lon1, lat2, lon2):
        # Переводим градусы в радианы
        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)
        
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return self._radius * c
    
    def calculate_total_distance(self):
        coordinates = self._parse_coordinates()
        df = pd.DataFrame(coordinates, columns=['Latitude', 'Longitude'])
        self._df = df
        for i in range(len(df)):
            for j in range(i+1, len(df)):
                self.total_distance += self._distance_between(df.iloc[i]['Latitude'], df.iloc[i]['Longitude'], df.iloc[j]['Latitude'], df.iloc[j]['Longitude'])
        return self.total_distance
    
    def print_results(self):
        if hasattr(self, 'total_distance'):
            print("Общее расстояние: {:.2f} км".format(self.total_distance))
        else:
            raise AttributeError('Необходимо сначала вычислить общую дистанцию')

    
# if __name__ == "__main__":
#     coordinates = np.array([[40.7128, -74.0060], [40.7129, -74.0059], [40.7127, -74.0061], [40.7126, -74.0062], [40.7125, -74.0063]])
#     drone_path = DronePath(coordinates)
#     drone_path.calculate_total_distance()
    