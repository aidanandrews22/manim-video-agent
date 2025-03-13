# MappingCamera

Qualified name: `manim.camera.mapping\_camera.MappingCamera`

### *class* MappingCamera(mapping_func=<function MappingCamera.<lambda>>, min_num_curves=50, allow_object_intrusion=False, \*\*kwargs)

Bases: [`Camera`](manim.camera.camera.Camera.md#manim.camera.camera.Camera)

Camera object that allows mapping
between objects.

### Methods

| [`capture_mobjects`](#manim.camera.mapping_camera.MappingCamera.capture_mobjects)   | Capture mobjects by printing them on `pixel_array`.   |
|-------------------------------------------------------------------------------------|-------------------------------------------------------|
| `points_to_pixel_coords`                                                            |                                                       |

### Attributes

| `background_color`   |    |
|----------------------|----|
| `background_opacity` |    |

#### capture_mobjects(mobjects, \*\*kwargs)

Capture mobjects by printing them on `pixel_array`.

This is the essential function that converts the contents of a Scene
into an array, which is then converted to an image or video.

* **Parameters:**
  * **mobjects** – Mobjects to capture.
  * **kwargs** – Keyword arguments to be passed to `get_mobjects_to_display()`.

### Notes

For a list of classes that can currently be rendered, see `display_funcs()`.
