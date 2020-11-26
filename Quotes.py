from PIL import Image
import glob

# Create the frames
frames = []
imgs = list(glob.glob("*.png"))
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
    #print(new_frame)
    #print(imgs)

# Save into a GIF file that loops forever
frames[0].save('Quotes.gif', format='GIF',
               append_images=frames[0:13],
               save_all=True,
               duration=300, loop=0)

