from data import Data_processing

import os
import shutil # Standard Python library for high-level file operations.
import Moon_model as Moon_model
import pandas as pd
from data_finder import clean_directory,transfer_files


# path: Directory path where the input images and labels are located.
# output_directory: Directory where the output files (annotated images and CSVs) will be saved.
# model: The machine learning model used for predictions.

def main_processing(path, output_directory, model):

    #Copies the images directory from the specified path to the current working directory 
    try:
        shutil.copytree(path + '/images', os.getcwd()+'/images')
    # if the image directory is already present in CWD, then 
    except FileExistsError:
        shutil.rmtree(os.getcwd()+'/images') # Remove the image directory
        shutil.copytree(path + '/images', os.getcwd() + '/images') # add the image directory

    # Also copies the images directory to static/prediction_original_images.
    shutil.copytree(path + '/images', 'static/prediction_original_images')


    # if there is a labels directory in the specified path.
    if 'labels' in os.listdir(path):
        # If it exists, copies it to the CWD.
        try:
            shutil.copytree(path + '/labels', os.getcwd() + '/labels')
        except FileExistsError:
            shutil.rmtree(os.getcwd() + '/labels')
            shutil.copytree(path + '/labels', os.getcwd() + '/labels')

        # object of Data_processing class
        processor = Data_processing('images','labels')
        processor.convert_to_txt() # convert labels into .txt file





    # Run Model Predictions:
    if os.path.exists('runs'):
        shutil.rmtree('runs') #Removes any existing runs directory.
    model.predict(source='images', hide_labels=True, line_thickness=2, save=True, save_txt=True)




    #Create output directories
    try:
        os.mkdir(output_directory + '/images')
    except FileExistsError: # if already exists remove directory anf recreate
        shutil.rmtree(output_directory + '/images')
        os.mkdir(output_directory + '/images')

    try:
        os.mkdir(output_directory + '/detections')
    except FileExistsError: # if already exists remove directory anf recreate
        shutil.rmtree(output_directory + '/detections')
        os.mkdir(output_directory + '/detections')




    for item in os.listdir('runs/detect/predict'):
        if item != 'labels':
            name = item.split('.')[0]
            label = [name,'txt']
            label_name = '.'.join(label)
            if label_name in os.listdir('runs/detect/predict/labels'):
                shutil.copy('runs/detect/predict/'+item, output_directory + '/images')
                shutil.copy('runs/detect/predict/'+item, 'static/prediction_old_names')
            for item in os.listdir('runs/detect/predict/'+ 'labels'):
                name = item.split('.')[0]
                label = [name, 'csv']
                label_name = '.'.join(label)
                read_file = pd.read_csv('runs/detect/predict/'+'labels'+'/'+item)
                read_file_2 = pd.read_csv('runs/detect/predict/'+'labels'+'/'+item)
                read_file.to_csv(output_directory+'/detections/'+label_name)
                read_file_2.to_csv('static/prediction_original_labels')

    #Cleans up temporary files and directories used during processing.                  
    clean_directory()
    return transfer_files() # Transfers the final files to the desired locations 


main_processing('/Users/princekumar/Machine Learning/Moon_crater_detection/Data/Images', '/Users/princekumar/Machine Learning/Moon_crater_detection/Data/Output', Moon_model.model_moon)
