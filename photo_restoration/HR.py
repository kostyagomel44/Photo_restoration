import os
import subprocess


input_folder = "test_images/old"
output_folder = "output"
basepath = os.getcwd()
input_path = os.path.join(basepath, input_folder)
output_path = os.path.join(basepath, output_folder)
#os.mkdir(output_path)

command = f'python run.py --input_folder /home/konstantin/Projects/Diploma/photo_restoration/test_images/old/ --output_folder /home/konstantin/Projects/Diploma/photo_restoration/output/ --GPU 0'

os.chdir('/home/konstantin/Projects/Diploma/photo_restoration/')
os.system(command)

