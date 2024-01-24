import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def get_mask(img, lower:list, upper:list, normalize_mask=True):
    lower = np.array(lower)
    upper = np.array(upper)
    img_masked = img.copy()
    
    mask = cv2.inRange(img, lower, upper)
    img_masked[mask > 0, 0] = 255
    img_masked[mask > 0, 1] = 0
    img_masked[mask > 0, 2] = 0
    
    mask = mask/255 if normalize_mask else mask
    
    return mask, img_masked

def images_to_video(imgs, output_path, frame_rate):
    height, width, _ = imgs[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, frame_rate, (width, height))
    
    for img in tqdm(imgs):
        video_writer.write(cv2.cvtColor((img * 255).astype(np.uint8), cv2.COLOR_BGR2RGB))
        
    video_writer.release()
    

def main():
    foreground = [plt.imread(os.path.join('./cat/', i)) for i in sorted(os.listdir('./cat'))]
    
    background = [plt.imread(os.path.join('./gta6/', i)) for i in sorted(os.listdir('./gta6'))]
    
    print(f"{len(foreground)} images in foreground")
    print(f"{len(background)} images in background")

    result = []
    
    for fore, back in tqdm(zip(foreground, background), total=len(foreground)):
        mask, _ = get_mask(fore, [0, 200.0, 0], [100.0, 255.0, 100.0])
        fore, back = fore/255.0, back/255.0
        back_mask = mask[:, :, None] * back
        only_fore = fore * np.logical_not(mask)[:, :, None]
        result.append(back_mask + only_fore)

    
    images_to_video(result, 'cat_gta6.mp4', 30)


if __name__ == "__main__":
    main()