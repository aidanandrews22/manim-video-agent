# lenses

Lenses for refracting Rays.

### Classes

| [`Lens`](manim_physics.optics.lenses.Lens.md#manim_physics.optics.lenses.Lens)   | A lens.   |
|----------------------------------------------------------------------------------|-----------|

### Functions

### antisnell(r_ang, n)

accepts radians, returns radians

* **Parameters:**
  * **r_ang** (*float*)
  * **n** (*float*)
* **Return type:**
  float

### intersection(vmob1, vmob2)

intersection points of 2 curves

* **Parameters:**
  * **vmob1** (*VMobject*)
  * **vmob2** (*VMobject*)
* **Return type:**
  *Iterable*[*Iterable*[float]]

### snell(i_ang, n)

accepts radians, returns radians

* **Parameters:**
  * **i_ang** (*float*)
  * **n** (*float*)
* **Return type:**
  float
