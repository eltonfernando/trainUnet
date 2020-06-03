import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('./via_export_csv60.csv')
path_img='./data/'
##filename,file_size,file_attributes,region_count,region_id,region_shape_attributes,region_attributes

for idx,row in df.iterrows():
    img_name = df["filename"][idx].split(".")
    img_name=img_name[0]+"."+img_name[-1]
    print(img_name)
    img = cv2.imread(path_img +"img/"+ img_name)
    points=eval(df['region_shape_attributes'][idx])
    x=np.array(points['all_points_x'])
    y=np.array(points['all_points_y'])
    point =[]
    for i in range(len(x)):
        point.append([x[i],y[i]])
    mask=np.zeros(img.shape)
    point=np.array(point).reshape(-1,1,2)
    cv2.drawContours(mask,([point]),-1,(255,0,0),cv2.FILLED)
    cv2.imshow("nome",img)
    cv2.imshow("mask", mask)
    cv2.imwrite(path_img+"mask/"+img_name,mask)
    cv2.waitKey(1)
