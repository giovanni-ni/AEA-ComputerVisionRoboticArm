import cv2
import os

DATASET_DIR = "../../Dataset/ternary_mnist/"
IMAGES_DIR = DATASET_DIR+""
DATASET_FILENAME = "ternary_mnist.csv"

data_file = open(DATASET_DIR+DATASET_FILENAME,"w")

print("Lettura di tutte le immagini da %s" % IMAGES_DIR)
print("Scrittura sul file %s" % DATASET_FILENAME)

counter = {"0":0, "1":0, "2":0, "total":0}

for i in range(3):
    current_dir = IMAGES_DIR+str(i)
    for f in os.listdir(current_dir):

        if(not ".jpg" in f):
            continue

        img = cv2.imread(current_dir+"/"+f, (cv2.IMREAD_GRAYSCALE))
        arr = img.flatten()
        for j, k in enumerate(arr):
            arr[j] = 255 - k
        data_file.write(",".join(arr.astype(str)))
        data_file.write(","+str(i))
        data_file.write("\n")

        counter[str(i)]+=1
        counter["total"]+=1

data_file.close()

print("Immagini scritte: %s" % counter)