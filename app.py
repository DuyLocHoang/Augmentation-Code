import os
import pandas as pd
import glob
import shutil

class FHSimulator:
    def __init__(self,img_path,csv_file,save_path):
        self.img_path = img_path
        self.csv_file = csv_file
        self.save_path = save_path

        self.data = pd.read_csv(self.csv_file)
        self.data = self.data.iloc[:,1:]

        self.img_file = []

        for file in os.listdir(img_path):
            self.img_file.append(file)
        
    def check_file(self):
        if self.data[self.data.columns[0]].count() != len(self.img_file):
            print("CSV file is not correct")
            return 0
        print("CHECK CSV FILES")
    
    def split(self):
        for i in range(self.data.shape[1]):
            k = 0
            folder_name = self.data.columns[i].replace(" ",'')
            if not os.path.exists(os.path.join(self.save_path,folder_name)):
                os.mkdir(os.path.join(self.save_path,folder_name))
            else:
                for file_path in os.listdir(os.path.join(self.save_path,folder_name)):
                    os.remove(os.path.join(self.save_path,folder_name,file_path))
            
            for index,j in enumerate(self.data.iloc[:,i]):
                if int(j) == -1 :
                    k += 1
                    shutil.copy(os.path.join(self.img_path,self.img_file[index]),os.path.join(self.save_path,folder_name,self.img_file[index]))
            print("NG {} {}".format(folder_name,k))
        print("DONE")

img_path = input("IMG FOLDER: ")
img_path = img_path.replace("\\","\\\\")
csv_file = input("CSV FILE: ")
csv_file = csv_file.replace("\\","\\\\")
save_path = input("SAVE FOLDER: ")
save_path = save_path.replace("\\","\\\\")
duyloc = FHSimulator(img_path,csv_file,save_path)
duyloc.check_file()
duyloc.split()
