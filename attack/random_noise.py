import os
import cv2
import pandas as pd


# add some random noise to bounding boxes of all of the images

name='test1'
copy = True
# Go into the dataset directory
os.chdir("../coco128")
# Check if directory already exists
current_files = os.listdir('images')

if copy:
    if name in current_files:
        print("Directory already exists!!")
        exit()

    # Copy clean data
    os.mkdir('images/'+name)
    os.system(f'cp -r images/train_clean_2017/* images/{name}/')

# Get all images
image_files = os.listdir(f'images/{name}')
images = [img.split('.')[0] for img in image_files] # Strip file type
print(images)

label_files = os.listdir(f'labels/train2017')
labels = [img.split('.')[0] for img in label_files] # Strip file type
# print(labels)

# result = [a == b for a, b in zip(images, labels)]
# print(result)
# print(images)
# import csv
# new_lab = list(labels).sort()
# print("here")
# print(new_lab)
# new_img = list(images).sort()
# with open('tesy.csv', 'w', newline='') as csvfile:
#     for i in range(128):
#         writer = csv.writer(csvfile)
#         writer.writerow([new_img[i], new_lab[i]])\
# def find_differences(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
    
#     # Differences in list1 but not in list2
#     in_list1_not_in_list2 = set1 - set2
    
#     # Differences in list2 but not in list1
#     in_list2_not_in_list1 = set2 - set1
    
#     return in_list1_not_in_list2, in_list2_not_in_list1



# differences1, differences2 = find_differences(images, labels)

# print("Differences in list1 but not in list2:", differences1)
# print("Differences in list2 but not in list1:", differences2)

        
# print(all(result))

# print(len(set(labels)))
# print(len(set(images)))

for img in images:
    # Get the label
    data = pd.read_csv(f'labels/train2017/{img}.txt', header = None)
    print(data)
    