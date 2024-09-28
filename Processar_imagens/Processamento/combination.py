# combinação das imagens

import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

# achar a diferençã entre as imagens 
def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Specify 2 images with de same shape." # valida a semelhança
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2) # converte para cinza
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True) # procura o score de 0 à 1 que define a semelhança
    print("Similarity of the images:", score)
    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image)) # normaliza para pode reduzir as diferenças das imagens
    return normalized_difference_image



def transfer_histogram(image1, image2): # chama as duas 
    matched_image = match_histograms(image1, image2, multichannel=True) # função comparativa
    return matched_image


