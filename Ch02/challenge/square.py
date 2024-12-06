# %%
import matplotlib.pyplot as plt

img = plt.imread('flower.png')
img = img.copy()  # make img writable
plt.imshow(img)

#%%
type(img)
# %%
img.shape

# %%
# Draw a blue square around the flower
# Top-left: 190x350
# Bottom-right: 680x850
# Line width: 5

top_left_x, top_left_y = 350, 190
bottom_right_x, bottom_right_y = 850, 680
width = 5

color = [0, 0, 0xFF] # blue

# Top line
img[top_left_x:top_left_x+width, top_left_y:bottom_right_y] = color
# Bottom line
img[bottom_right_x:bottom_right_x+width, top_left_y:bottom_right_y] = color
# Left line
img[top_left_x:bottom_right_x, top_left_y:top_left_y+width] = color
# Right line
img[top_left_x:bottom_right_x, bottom_right_y-width:bottom_right_y] = color

plt.imshow(img)
# %%
