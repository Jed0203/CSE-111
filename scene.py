import tkinter as tk
import random


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 650
    tree_top = scene_top + 100
    tree_height = 300
    draw_sky(canvas,0,0,800,300)
    draw_ground(canvas, 0, 300, 800, 500)
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    draw_sun(canvas, 50, 50)
    rowgen(canvas, 0, 500, 500, 300)
    #draw_grass(canvas, 0, 1900, 20, 500)
    #draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    text_horizontal_margin = 20
    text_vertical_margin = 20

    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text = f"{i}")

    for i in range (left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text = f"{i}")

def draw_sky(canvas, x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue4")

def draw_ground(canvas, x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill="tan4")

"""def draw_grass(canvas, x1, y1, x2, y2):
    width = x1 / 10
    height =  y1/ 6
    left = x2 - width / 4
    right = y2 - width / 8
    bottom = y2 + height
    canvas.create_rectangle(left, bottom, width, height, fill="green")
    """       
def rowgen(canvas, x1, y1, x2, y2):
    width = x1 / 10
    height =  y1/ 6
    left = x2 - width / 4
    right = y2 - width / 8
    bottom = y2 + height
    for i in range(x1, x1):
        for j in range(y1, y2):
            canvas.create_rectangle(left, bottom, width, height,fill="green")

def draw_sun(canvas, x, y):
    canvas.create_oval(x, y, x + 100, y + 100, fill="yellow", width = False)

def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 5
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()