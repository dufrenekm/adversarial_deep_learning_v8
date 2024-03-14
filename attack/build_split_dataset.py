import os

os.chdir("../coco126/images")
split = "watermelon"


# Grab 1/2 images randomly from clean, 1/2 from adversarial
image_files = os.listdir('train_clean_2017')
images = [img.split('.')[0] for img in image_files] # Strip file type

new_dir = "split_"+split
os.mkdir(new_dir)

for i in range(63):
    image = images.pop()
    os.system(f'cp train_clean_2017/{image}.jpg {new_dir}/')
    
for i in range(63):
    image = images.pop()
    os.system(f'cp {split}/{image}.jpg {new_dir}/')