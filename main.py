import os
from dataclasses import dataclass
from run import run_cdm

@dataclass
class Data:
    image_location: str
    output_name: str
    optional_parameters: bool = False
    latitude: str = ''
    longitude: str = ''
    image_res: float = 0.0
    image_dim: str = ''
    planet_radius: float = 0.0

def main():
    data_directory = '/Users/princekumar/Machine Learning/Moon_crater_detection/Data/Images'  # path to your data directory
    output_directory = '/Users/princekumar/Machine Learning/Moon_crater_detection/Data/Output'  # path to your desired output directory
    
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    data = Data(
        image_location=data_directory,
        output_name=output_directory,
        optional_parameters=False  # Set to True if you want to use latitude and longitude
    )

    images, detections = run_cdm(data)
    
    print("Processed Images:", images)
    print("Generated Detections:", detections)

if __name__ == "__main__":
    main()
