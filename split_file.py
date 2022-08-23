import os
from re import I


root = "D:\\AI\\Datasets\\Traffic Signs Data\\A11"
save_file = "D:\\AI\\Datasets\\Traffic Signs Data\\A11-split"
cam = ["CAM_1","CAM_2"]
for i in cam:
    root_file = os.path.join(root,i)
    for root,path,file in os.walk(root_file):
        print(root,path,file)
        if file != []:
            for img in file:
                os.replace(os.path.join(root,img),os.path.join(save_file,img))