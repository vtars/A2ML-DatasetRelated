import SimpleITK as sitk
import numpy as np
import os
import cv2


def save_nii_slice(filepath):
    img_dir = os.path.join(os.path.dirname(filepath), '{}_img'.format(os.path.abspath(filepath)))
    print(img_dir)
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    filenames = os.listdir(filepath)

    for f in filenames:
        img_path = os.path.join(filepath, f)
        img = sitk.ReadImage(img_path)
        img = sitk.Cast(sitk.RescaleIntensity(img), sitk.sitkUInt8)
        img = sitk.GetArrayFromImage(img)
        z_length = np.shape(img)[0]
        slice_img = img[int(z_length/2), ::-1, ::-1]
        fname = f.replace('.nii.gz', '')
        cv2.imwrite('{}\\{}.png'.format(img_dir, fname), slice_img)
        print(fname, 'is sliced ')


main_path = 'E:\\work\\data\\Task02_Heart'
dirs = os.listdir(main_path)
for dirname in dirs:
    abs_dirname = os.path.join(main_path, dirname)
    if os.path.isdir(abs_dirname):
        print(abs_dirname)
        save_nii_slice(abs_dirname)
