import os
import numpy as np
from PIL import Image
from torchvision.transforms import ToTensor
from torch.utils.data import Dataset

class DatasetLoader(Dataset):
  def __init__(self,dir_rgb,dir_tf):
    super().__init__()
    self.dir_rgb = dir_rgb
    self.dir_tf = dir_tf
    self.paths_rgb = [dir_rgb+f for f in listdir(dir_rgb) if isfile(join(dir_rgb, f))]
    self.paths_tf = [dir_tf+f for f in listdir(dir_tf) if isfile(join(dir_tf, f))]
  
  def __len__(self):
    return len(self.paths_rgb)
  
  def __getitem__(self,idx):
    image_rgb = np.array(Image.open(self.paths_rgb[idx])).astype('uint8')
    image_tf = np.array(Image.open(self.paths_tf[idx])).astype('uint8')
    return(ToTensor()(image_tf),ToTensor()(image_rgb))
