import os
import Moon_model as Moon_model

from data_processing import main_processing
from Moon_model import model_moon


def run_cdm(data):
    if (data.optional_parameters and data.latitude != '' and data.longitude != ''):
        image_location = data.image_location
        latitude = data.latitude
        longitude = data.longitude

        image_res = float(data.image_res)  # Converts the image resolution to a float.

        image_dim = data.image_dim.upper().split('X')  # Split the dimension at X

        # Map of width and height of the image
        image_dim = {'W': float(image_dim[0]),
                     'H': float(image_dim[-1])}

        # Converts the planet's radius to a float.
        planet_radius = float(data.planet_radius)

        # Model selection: Always using the Moon model
        model = Moon_model.model_moon

        # main_processing(path, output_directory, model)
        images, csvs = main_processing(data.output_name, image_location, model)

        # Create a list of images
        images = [image for image in images if '.png' in image]
        images = sorted(images)

        # Crater detection model
        cdm_data = [images, csvs]

    else:
        image_location = data.image_location

        # Always using the Moon model
        model = Moon_model.model_moon
        images, csvs = main_processing(data.output_name, image_location, model)
        images = [image for image in images if '.png' in image]
        images = sorted(images)
        cdm_data = [images, csvs]

    return cdm_data
