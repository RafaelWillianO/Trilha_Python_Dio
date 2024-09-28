# vai transforma para uma imagem

from skimage.transform import resize

def resize_image(image, proportion): # parametros da imagem com proporção de 0 à 1
    assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1." #  passa mensagem se estiver errado
    height = round(image.shape[0] * proportion)
    width = round(image.shape[1] * proportion)
    image_resized = resize(image, (height, width), anti_aliasing=True) # correção para valor inteiro
    return image_resized