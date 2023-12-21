import matplotlib.pyplot as plt
import numpy as np


def lire_image(chemin):
    # Lire l'image avec Matplotlib
    image = plt.imread(chemin)
    print(type(image))
    print(image.shape)
    fig, ax = plt.subplots()
    ax.imshow(image)
    return image


def canaux(image):
    red_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    blue_channel = image[:, :, 2]

    return red_channel, green_channel, blue_channel


def rotation(image, nombre_rotations):
    rotated_image = np.rot90(image, nombre_rotations)
    fig, ax = plt.subplots()
    ax.imshow(rotated_image)
    return rotated_image


def roi(image, x1, x2, y1, y2):
    # Coordonnées des deux points du rectangle
    x_coords = [x1, x1, x2, x2, x1]
    y_coords = [y1, y2, y2, y1, y1]
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.plot(x_coords, y_coords, color='red')


def crop_image(image, x1, x2, y1, y2):
    # Coordonnées des deux points du rectangle
    x_coords = [x1, x1, x2, x2, x1]
    y_coords = [y1, y2, y2, y1, y1]
    crop_image = image[y1:y2, x1:x2, :]
    fig, ax = plt.subplots()
    ax.imshow(crop_image)
    return crop_image

def histogramme(image):
    # Séparez les canaux RGB de l'image
    red_channel = image[:, :, 0].flatten() #la fonction histogramme de matplotlib attend 1 tableau en 1 dimension il faut flatten
    green_channel = image[:, :, 1].flatten()
    blue_channel = image[:, :, 2].flatten()
    
    # Créez une figure avec trois sous-graphiques pour les histogrammes
    fig, ax = plt.subplots(1, 3,figsize = (12,6))

    # Tracez l'histogramme du canal rouge
    ax[0].hist(red_channel, bins=256, range=(0, 255), color='red')
    ax[0].set_title('Red Channel')
    ax[0].set_xlim(0, 255) 
    ax[0].set_ylim(0, 32000) 

    # Tracez l'histogramme du canal vert
    ax[1].hist(green_channel, bins=256, range=(0, 255), color='green')
    ax[1].set_title('Green Channel')
    ax[1].set_xlim(0, 255) 
    ax[1].set_ylim(0, 32000) 
    

    # Tracez l'histogramme du canal bleu
    ax[2].hist(blue_channel, bins=256, range=(0, 255), color='blue')
    ax[2].set_title('Blue Channel')
    ax[2].set_xlim(0, 255) 
    ax[2].set_ylim(0, 32000) 
    
    fig.tight_layout()
    return red_channel, green_channel, blue_channel
 
    
def gris(image,canalR,canalG,canalB):
    
    image_gray = (canalR/3 + canalG/3 + canalB/3) 
    
    fig,ax = plt.subplots(1,2)
    ax[0].imshow(image,cmap='gray')
    ax[0].set_title('Avant')
    ax[1].imshow(image_gray,cmap='gray')#,cmap='gray',vmin = 0, vmax = 255)
    ax[1].set_title('Après')
    return image_gray

def seuil(image_gray,seuil):
    
    image_seuil = np.copy(image_gray)
    condition_fond = (image_gray < seuil)
    condition_objet = (image_gray >= seuil)

    indices_fond= np.where(condition_fond)
    indices_objet= np.where(condition_objet )

    image_seuil[indices_fond] = 0
    image_seuil[indices_objet] = 255
    
    fig,ax = plt.subplots(1,2)
    ax[0].imshow(image_gray,cmap='gray')
    ax[0].set_title('Avant')
    ax[1].imshow(image_seuil,cmap='gray')#,cmap='gray',vmin = 0, vmax = 255)
    ax[1].set_title('Après')

# def couleur(image,canal,delta):
    
    
#     red_channel = image[:, :, 0]
#     green_channel = image[:, :, 1]
#     blue_channel = image[:, :, 2]

    
#     if canal == 'rouge':
#         red_channel  = red_channel + delta
#         red_channel[red_channel<= 0] = 0
#         red_channel[red_channel > 255] = 255
    
#     if canal == 'vert':
#         green_channel  = green_channel + delta
#         green_channel[green_channel<= 0] = 0
#         green_channel[green_channel > 255] = 255
    
    
#     if canal == 'bleu':
#         blue_channel  = blue_channel + delta
#         blue_channel[blue_channel<= 0] = 0
#         blue_channel[blue_channel > 255] = 255

#     image_couleur_modif = np.stack((red_channel, green_channel, blue_channel), axis=-1)
    
#     fig,ax = plt.subplots(1,2)
#     ax[0].imshow(image)
#     ax[1].imshow(image_couleur_modif)
    
#     return image_couleur_modif




# def brillance(image,delta):
#     red_channel = image[:, :, 0]
#     green_channel = image[:, :, 1]
#     blue_channel = image[:, :, 2]

#     # # Ajouter une valeur constante au canal bleu
#     red_channel  = red_channel + delta
#     red_channel[red_channel<= 0] = 0
#     red_channel[red_channel > 255] = 255


#     green_channel  = green_channel + delta
#     green_channel[green_channel<= 0] = 0
#     green_channel[green_channel > 255] = 255

#     blue_channel  = blue_channel + delta
#     blue_channel[blue_channel<= 0] = 0
#     blue_channel[blue_channel > 255] = 255

#     image_brillance_modif = np.stack((red_channel, green_channel, blue_channel), axis=-1)
#     fig,ax = plt.subplots(1,2)
#     ax[0].imshow(image)
#     ax[1].imshow(image_brillance_modif)
    
#     return image_brillance_modif