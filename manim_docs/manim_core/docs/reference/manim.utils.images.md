# images

Image manipulation utilities.

### Functions

### change_to_rgba_array(image, dtype='uint8')

Converts an RGB array into RGBA with the alpha value opacity maxed.

* **Parameters:**
  * **image** ([*RGBPixelArray*](manim.typing.md#manim.typing.RGBPixelArray))
  * **dtype** (*str*)
* **Return type:**
  [*RGBPixelArray*](manim.typing.md#manim.typing.RGBPixelArray)

### drag_pixels(frames)

* **Parameters:**
  **frames** (*list* *[**array* *]*)
* **Return type:**
  list[*array*]

### get_full_raster_image_path(image_file_name)

* **Parameters:**
  **image_file_name** (*str* *|* *PurePath*)
* **Return type:**
  *Path*

### get_full_vector_image_path(image_file_name)

* **Parameters:**
  **image_file_name** (*str* *|* *PurePath*)
* **Return type:**
  *Path*

### invert_image(image)

* **Parameters:**
  **image** (*array*)
* **Return type:**
  <module ‘PIL.Image’ from ‘/opt/anaconda3/envs/edu_video_generation/lib/python3.11/site-packages/PIL/Image.py’>
