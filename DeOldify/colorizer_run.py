from DeOldify.deoldify.visualize import get_image_colorizer
from DeOldify.deoldify import device
from DeOldify.deoldify.device_id import DeviceId
device.set(device=DeviceId.GPU0)




colorizer_model = get_image_colorizer(artistic=True)


def colorizer(source_path, user_id, model=colorizer_model, render_factor=25):
    # source_path = '/home/alexandr/instauration_bot/input.jpg'
    res = model.get_transformed_image(source_path)
    # res.save("/home/konstantin/Projects/Diploma/DeOldify/result_images/result.jpg")
    res.save(f"/home/konstantin/Projects/Diploma/input_{user_id}.jpg")
    return res
