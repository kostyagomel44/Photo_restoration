# from image_compres import image_compressor
# Image comressor get img_path, save_path. Max_weight and max_hight defined by deafault as 200 and 150
# Image compressor compress image by saving proportion

from PIL import Image

def image_compresser(img_path, save_path, max_weight=350, max_hight=350):

    img = Image.open(img_path)
    img_weight=img.size[0]
    img_hight=img.size[1]

    if img_weight * img_hight > max_weight * max_hight:

        if img_weight >= max_weight:
            new_img_weight = max_weight
            new_img_hight = int(new_img_weight * (img_hight/img_weight))

        elif img_hight >= max_hight:
            new_img_hight = max_hight
            new_img_weight = int(new_img_hight * (img_weight/img_hight))

    else:
        print('IMAGE DOESNT NEED TO BE COMPREESED')
        return
    
    new_image = img.resize((new_img_weight, new_img_hight),Image.ANTIALIAS)
    new_image.save(save_path)