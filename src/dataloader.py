import os
import numpy as np
from PIL import Image
from torchvision.transforms import ToTensor
from torch.utils.data import Dataset

class DatasetLoader(Dataset):
  def __init__(self,dir_gt,dir_in):
    super().__init__()
    self.dir_gt = dir_gt
    self.dir_in = dir_in
    self.paths_gt = [dir_gt+f for f in listdir(dir_gt) if isfile(join(dir_gt, f))]
    self.paths_in = [dir_in+f for f in listdir(dir_in) if isfile(join(dir_in, f))]
  
  def __len__(self):
    return len(self.paths_gt)
  
  def __getitem__(self,idx):
    image_gt = np.array(Image.open(self.paths_gt[idx])).astype('uint8')
    image_in = np.array(Image.open(self.paths_in[idx])).astype('uint8')
    return(ToTensor()(image_in),ToTensor()(image_gt))
