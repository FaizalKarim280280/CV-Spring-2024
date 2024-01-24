import cv2 as cv
import os
from tqdm import tqdm

def video_to_images(video_path, output_folder):
    cap = cv.VideoCapture(video_path)
    
    frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Saving each frame as an image in the output folder
        frame_count += 1
        image_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv.imwrite(image_path, frame)

    cap.release()

if __name__ == "__main__":
    input_video_path = './gta6.mp4'

    output_folder_path = "gta6"
    os.makedirs(output_folder_path, exist_ok=True)

    video_to_images(input_video_path, output_folder_path)