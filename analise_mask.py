import cv2
import numpy as np
import os
local="./data/mask"
list_data=os.listdir(local)
soma_mask=0
for nome in list_data:
    img=cv2.imread((local+'/'+nome))
    soma_mask+=np.sum(img/255)
    cv2.imshow("mask",img)
    cv2.waitKey(1)

total_px=len(list_data)*480*848
print("total px: ",total_px)
print("total mask: ",soma_mask)
print("porcent% ",soma_mask/total_px*100)