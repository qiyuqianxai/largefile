import torch


state_dict = torch.load('outdoor_0625.pth', map_location="cpu")
torch.save(state_dict, 'detr_outdoor.pth', _use_new_zipfile_serialization=False)