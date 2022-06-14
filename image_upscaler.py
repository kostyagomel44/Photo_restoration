from PIL import Image
import requests


def upscaler(img_path, img_save_path, max_weight=600, max_hight=600):

    with open('/home/konstantin/Projects/Diploma/API_key.txt') as f:
        API_key = f.readlines()
        
    r = requests.post(
    "https://api.deepai.org/api/torch-srgan",
    files={
        'image': open(img_path, 'rb'),
    },
    headers={'api-key': API_key[0][:-1]})

    img = Image.open(requests.get(r.json()['output_url'], stream=True).raw)
        
    img_weight=img.size[0]
    img_hight=img.size[1]

    if img_weight * img_hight > max_weight * max_hight:

        if img_weight >= max_weight:
            new_img_weight = max_weight
            new_img_hight = int(new_img_weight * (img_hight/img_weight))

        elif img_hight >= max_hight:
            new_img_hight = max_hight
            new_img_weight = int(new_img_hight * (img_weight/img_hight))
  
    new_image = img.resize((new_img_weight, new_img_hight),Image.ANTIALIAS)
    new_image.save(img_save_path)      