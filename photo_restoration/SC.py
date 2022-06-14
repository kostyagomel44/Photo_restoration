import os
import subprocess


# input_folder = "test_images/old_w_scratch"
# output_folder = "output_w_scratch"
# basepath = os.getcwd()
# input_path = os.path.join(basepath, input_folder)
# output_path = os.path.join(basepath, output_folder)
# os.mkdir(output_path)



# def scratching():
#     command = f'python run.py --input_folder /home/konstantin/Projects/Diploma/photo_restoration/test_images/old_w_scratch  --output_folder /home/konstantin/Projects/Diploma/photo_restoration/output_w_scratch --GPU 0 --with_scratch'
#     os.chdir('/home/konstantin/Projects/Diploma/photo_restoration/')
#     os.system(command)


def scratching(user_id):
    command_copy = f'cp /home/konstantin/Projects/Diploma/input_{user_id}.jpg /home/konstantin/Projects/Diploma/photo_restoration/test_images/old_w_scratch'
    os.system(command_copy)
    command = f'python run.py --input_folder /home/konstantin/Projects/Diploma/photo_restoration/test_images/old_w_scratch  --output_folder /home/konstantin/Projects/Diploma/photo_restoration/output_w_scratch --GPU 0 --with_scratch'
    os.chdir('/home/konstantin/Projects/Diploma/photo_restoration/')
    os.system(command)


