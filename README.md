# Photo_Restoration
## Сервис по восстановлению старых фотографий
![My Remote Image](https://i.ibb.co/rpYZfXd/123-Ie-Q03.png)


### Stack:
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://python.org)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
[![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white)](https://www.tensorflow.com)
![OpenCV](https://img.shields.io/static/v1?style=for-the-badge&message=OpenCV&color=5C3EE8&logo=OpenCV&logoColor=FFFFFF&label=)

## Алгоритм работы:

### 1. Удаление повреждений
#### Сначала на поврежденной фотографии определяются зоны с повреждениями. Построенная маска накладывается на фото и нейросеть заполняет области пустоты
![My Remote Image](https://i.ibb.co/fXY9DJZ/Fit-Predict.png)


#### Так же отдельная нейросеть определяет зоны лиц и проводит повышения разрешения конкретно этих зон
![My Remote Image](https://i.ibb.co/2gDWL5K/Fit-Predict1.png)


### 2. Колоризация
#### Колоризацию проводит отдельная нейросеть обученная на старых цветных фотографиях (так что колоризация любой фотографии получается слегка в винтажном стиле)
![My Remote Image](https://i.ibb.co/SPYhzhT/Fit-Predict2.png)

### 3. Повышение разрешения.
#### Операция повышения разрешения происходит на стороннем сервисе через API запрос. На выхое получаете картинку разрешением х8.
https://deepai.org/machine-learning-model/torch-srgan

![My Remote Image](https://i.ibb.co/5MGjY2k/Fit-Predict7.png)

### 4. Обрезка фотографии
#### Предположим вы просто сфотографировали фотографию на столе и не хотите ее обрезать вручную. Для этого случае встроена функция обрезки.
![My Remote Image](https://i.ibb.co/2yLFpxV/Fit-Predict5.png)

### Пример работ

![My Remote Image](https://i.ibb.co/0yzqG7X/Fit-Predict6.png)

#### Веса моделей
#### /photo_restoration/Face_Enhancement/checkpoints (https://drive.google.com/drive/folders/1MXpcVzNmWY3lxiTcsq6JrUqB-XDd_kDD?usp=sharing)
#### /photo_restoration/Global/checkpoints (https://drive.google.com/drive/folders/1mzzz0ExKpO11srrxZtcvzmR21DxUnrPE?usp=sharing)
