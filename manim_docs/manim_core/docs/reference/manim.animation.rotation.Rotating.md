# Rotating

Qualified name: `manim.animation.rotation.Rotating`

### *class* Rotating(mobject=None, \*args, use_override=True, \*\*kwargs)

Bases: [`Animation`](manim.animation.animation.Animation.md#manim.animation.animation.Animation)

### Methods

| [`interpolate_mobject`](#manim.animation.rotation.Rotating.interpolate_mobject)   | Interpolates the mobject of the `Animation` based on alpha value.   |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------|

### Attributes

| `run_time`   |    |
|--------------|----|
* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **axis** (*np.ndarray*)
  * **radians** (*np.ndarray*)
  * **about_point** (*np.ndarray* *|* *None*)
  * **about_edge** (*np.ndarray* *|* *None*)
  * **run_time** (*float*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)

#### \_original_\_init_\_(mobject, axis=array([0., 0., 1.]), radians=6.283185307179586, about_point=None, about_edge=None, run_time=5, rate_func=<function linear>, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mobject** ([*Mobject*](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject))
  * **axis** (*np.ndarray*)
  * **radians** (*np.ndarray*)
  * **about_point** (*np.ndarray* *|* *None*)
  * **about_edge** (*np.ndarray* *|* *None*)
  * **run_time** (*float*)
  * **rate_func** (*Callable* *[* *[**float* *]* *,* *float* *]*)
* **Return type:**
  None

#### interpolate_mobject(alpha)

Interpolates the mobject of the `Animation` based on alpha value.

* **Parameters:**
  **alpha** (*float*) – A float between 0 and 1 expressing the ratio to which the animation
  is completed. For example, alpha-values of 0, 0.5, and 1 correspond
  to the animation being completed 0%, 50%, and 100%, respectively.
* **Return type:**
  None
