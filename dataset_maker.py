"""
用于抠图
"""

import os

import cv2
import numpy as np

# original file path
original_path = 'CV/dataset_original'
# new file path
new_path = 'CV/dataset'
annotation_path = 'CV/dataset/annotation.txt'
# 图片旋转阈值
rot_threshold = 15

f = open(annotation_path, 'w')
for filepath,dirnames,filenames in os.walk(original_path):
    for filename in filenames:
        if filename.endswith('jpg'):
            # print(filename,filepath)
            img = cv2.imread(filepath + '\\'+ filename)
            img = np.array(img)
            f_annot = open(filepath + '\\'+ filename[:-4] + '-annot' + '.txt', 'r')
            annots = f_annot.readlines()
            f_annot.close()
            cnt = 0
            for annot in annots:
                annot = annot.split()
                rot = float(annot[4])
                rot += 90
                if (rot > rot_threshold and rot < 90 - rot_threshold) or (rot > 90 + rot_threshold and rot < 180 - rot_threshold) or (rot > 180 + rot_threshold and rot < 270 - rot_threshold) or (rot > 270 + rot_threshold and rot < 360 - rot_threshold):
                    continue

                central_x = float(annot[0])
                central_y = float(annot[1])
                width = float(annot[2])
                height = float(annot[3])
                x1 = int(central_x - width/2)
                y1 = int(central_y - height/2)
                x2 = int(central_x + width/2)
                y2 = int(central_y + height/2)

                img_crop = img[y1:y2, x1:x2]
                new_file_path = new_path + '\\' + filepath.split('\\')[-2] + filepath.split('\\')[-1] + '_' + filename[:-4] + '_' + str(cnt) + '_' + annot[4] + '.jpg'
                cv2.imwrite(new_file_path, img_crop)
                f.write('ICs;' + new_file_path + '\n')
                cnt += 1
f.close()