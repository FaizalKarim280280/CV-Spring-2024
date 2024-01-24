import cv2
import os

def main(image_path):
    counter = 0
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('w'):
            filename = os.path.join(image_path, f'{counter}.png')
            counter += 1
            cv2.imwrite(filename, frame)
            print(f"Image saved as {filename}")
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    image_path = './webcam'
    os.makedirs(image_path, exist_ok=True)
    main(image_path)