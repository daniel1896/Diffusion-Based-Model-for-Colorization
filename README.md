[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/daniel1896/Diffusion-Based-Model-for-Inpainting/blob/main/inpainting.ipynb)


# WORK IN PROGRESS
forked from [LouisRouss](https://github.com/LouisRouss/Diffusion-Based-Model-for-Colorization) and modified for inpainting

# How to train the model
Modify the conf.yml file, set the 'mode' option to 1. Then run the main.py file specifying the path to the config file  (absolute or relative)
Example : python main.py --config conf.yml

# Reference
Palette Image_to_Image Diffusion Models https://arxiv.org/pdf/2111.05826v1.pdf

Diffusion Models Beat GANs on Image Synthesis https://arxiv.org/pdf/2105.05233.pdf 

The Unet Network script directly comes from the repo of this last : https://github.com/openai/guided-diffusion (with small modifications according to the Palette paper)

A colorization Dataset : https://www.kaggle.com/shravankumar9892/image-colorization ( Palette paper's researchers uses ImageNet )
