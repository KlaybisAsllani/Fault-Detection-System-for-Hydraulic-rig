import pandas as pd
import os

def load_data(sensor_files, profile_file):
    # Get the absolute path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Load sensor data
    sensor_data = []
    for sensor_file in sensor_files:
        file_path = os.path.join(current_dir, '..', 'condition+monitoring+of+hydraulic+systems', sensor_file)
        sensor_df = pd.read_csv(file_path, delimiter='\t')
        sensor_data.append(sensor_df)
    
    # Concatenate all sensor data
    sensor_data = pd.concat(sensor_data, axis=1)
    
    # Load profile data
    profile_file_path = os.path.join(current_dir, '..', 'condition+monitoring+of+hydraulic+systems', profile_file)
    profile_data = pd.read_csv(profile_file_path, delimiter='\t')
    
    # Combine sensor data and profile data
    data = pd.concat([sensor_data, profile_data], axis=1)
    return data