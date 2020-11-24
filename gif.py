from PIL import Image
import glob

# Create the frames
frames = []
imgs = list(glob.glob("*.png"))
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
    #print(new_frame)
    print(imgs)

# Save into a GIF file that loops forever
frames[1].save('png_to_gif.gif', format='GIF',
               append_images=frames[0:1],
               save_all=True,
               duration=300, loop=0)
