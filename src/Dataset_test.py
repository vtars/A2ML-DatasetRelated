import torch
# model=resnext101_32x48d_wsl(progress=True) # example with the ResNeXt-101 32x48d

pretrained_dict = torch.load('./ResNet_no_adaptation.pth', map_location='cpu')['model']
print(pretrained_dict)
# model_dict = model.state_dict()
# for k in model_dict.keys():
#     if(('module.'+k) in pretrained_dict.keys()):
#         model_dict[k]=pretrained_dict.get(('module.'+k))
# model.load_state_dict(model_dict)
