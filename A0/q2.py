import cv2 as cv
import os

def images_to_video(image_folder, output_video_path, frame_rate):
    image_files = [f for f in os.listdir(image_folder) if f.endswith(".jpg")]
    
    image_files.sort()

    # Reading the first image to get dimensions
    first_image_path = os.path.join(image_folder, image_files[0])
    first_image = cv.imread(first_image_path)
    height, width, _ = first_image.shape

    # Defining the codec and creating a VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    video_writer = cv.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))

    # Writing each image to the video
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = cv.imread(image_path)
        video_writer.write(img)

    # Releasing the video writer object
    video_writer.release()
    
    
def main():
    input_images_folder = "oreo_frames"
    output_video_path = "oreo_output.mp4"
    
    frame_rate = 10

    images_to_video(input_images_folder, output_video_path, frame_rate)

if __name__ == "__main__":
    main()