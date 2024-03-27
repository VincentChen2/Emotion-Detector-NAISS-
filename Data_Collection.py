import cv2
import os

cam = cv2.VideoCapture(1) #Sets up camera capture using front-facing camera !!!FOR MAC!!! (change if using other device)
cam.set(3, 100) #Sets Width
cam.set(4, 100) #Sets Height

# Check if the camera opened successfully
if not cam.isOpened():
    print("Error: Camera could not be accessed.")
    exit()

number_of_images, current_images = int(input('Input Number of Images: ')), 0
folder_path = input('Input Folder Path: ')

if not os.path.exists(folder_path): #Creates directory if directory does not exist
    os.makedirs(folder_path)

while current_images < number_of_images: #Creates number of images, interrupts with 'q'
    _, frame = cam.read(0)
    cv2.imshow('Image', frame)
    cv2.imwrite(f'{folder_path}/IMG_{current_images}.jpg', frame)

    if cv2.waitKey(20) == ord('q'):
        break
    current_images += 1

cam.release()
cv2.destroyAllWindows()

print(f'Created {current_images + 1} images at {folder_path}')
