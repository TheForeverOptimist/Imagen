import imgaug.augmenters as iaa
import cv2
import glob


# 1.) Load Dataset
images = []
images_path = glob.glob("images/*.jpeg")
for img_path in images_path:
    img = cv2.imread(img_path)
    images.append(img)

#2.) Image Augmentation

augmentation = iaa.Sequential([
    #1. Rotate
    # iaa.Rotate((-30, 30))
    #2. Flip
    iaa.Fliplr(0.5),
    iaa.Flipud(0.5),

    #3. Affine
    iaa.Affine(translate_percent={"x": (-0.5, 0.5), "y": (-0.5, 0.5)},
               rotate=(-30, 30),
               scale=(0.5, 1.5),
               ),
    #4. Multiply -- which makes the image brighter or darker
    iaa.Multiply((0.8, 1.2)),

    #5 Linear Contrast
    iaa.LinearContrast((0.6, 1.4)),

    #Perform the below messages only sometime
    iaa.Sometimes(0.5, 
        #6. gaussian blur
        iaa.GaussianBlur((0.0, 3.0)),
                  
                  )


    

])

#3.) show images
while True:
    augmented_images = augmentation(images=images)
    for img in augmented_images:
        cv2.imshow("Image", img)
        cv2.waitKey(0)