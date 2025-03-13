# VDict

Qualified name: `manim.mobject.types.vectorized\_mobject.VDict`

### *class* VDict(mapping_or_iterable={}, show_keys=False, \*\*kwargs)

Bases: [`VMobject`](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)

A VGroup-like class, also offering submobject access by
key, like a python dict

* **Parameters:**
  * **mapping_or_iterable** (*Mapping* *[**Hashable* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*  *|* *Iterable* *[**tuple* *[**Hashable* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *]*) – The parameter specifying the key-value mapping of keys and mobjects.
  * **show_keys** (*bool*) – Whether to also display the key associated with
    the mobject. This might be useful when debugging,
    especially when there are a lot of mobjects in the
    [`VDict`](#manim.mobject.types.vectorized_mobject.VDict). Defaults to False.
  * **kwargs** – Other arguments to be passed to Mobject.

#### show_keys

Whether to also display the key associated with
the mobject. This might be useful when debugging,
especially when there are a lot of mobjects in the
[`VDict`](#manim.mobject.types.vectorized_mobject.VDict). When displayed, the key is towards
the left of the mobject.
Defaults to False.

* **Type:**
  `bool`

#### submob_dict

Is the actual python dictionary that is used to bind
the keys to the mobjects.

* **Type:**
  `dict`

### Examples

<div id="shapeswithvdict" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ShapesWithVDict <a class="headerlink" href="#shapeswithvdict">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./ShapesWithVDict-1.mp4">
</video>
```python
from manim import *

class ShapesWithVDict(Scene):
    def construct(self):
        square = Square().set_color(RED)
        circle = Circle().set_color(YELLOW).next_to(square, UP)

        # create dict from list of tuples each having key-mobject pair
        pairs = [("s", square), ("c", circle)]
        my_dict = VDict(pairs, show_keys=True)

        # display it just like a VGroup
        self.play(Create(my_dict))
        self.wait()

        text = Tex("Some text").set_color(GREEN).next_to(square, DOWN)

        # add a key-value pair by wrapping it in a single-element list of tuple
        # after attrs branch is merged, it will be easier like `.add(t=text)`
        my_dict.add([("t", text)])
        self.wait()

        rect = Rectangle().next_to(text, DOWN)
        # can also do key assignment like a python dict
        my_dict["r"] = rect

        # access submobjects like a python dict
        my_dict["t"].set_color(PURPLE)
        self.play(my_dict["t"].animate.scale(3))
        self.wait()

        # also supports python dict styled reassignment
        my_dict["t"] = Tex("Some other text").set_color(BLUE)
        self.wait()

        # remove submobject by key
        my_dict.remove("t")
        self.wait()

        self.play(Uncreate(my_dict["s"]))
        self.wait()

        self.play(FadeOut(my_dict["c"]))
        self.wait()

        self.play(FadeOut(my_dict["r"], shift=DOWN))
        self.wait()

        # you can also make a VDict from an existing dict of mobjects
        plain_dict = {
            1: Integer(1).shift(DOWN),
            2: Integer(2).shift(2 * DOWN),
            3: Integer(3).shift(3 * DOWN),
        }

        vdict_from_plain_dict = VDict(plain_dict)
        vdict_from_plain_dict.shift(1.5 * (UP + LEFT))
        self.play(Create(vdict_from_plain_dict))

        # you can even use zip
        vdict_using_zip = VDict(zip(["s", "c", "r"], [Square(), Circle(), Rectangle()]))
        vdict_using_zip.shift(1.5 * RIGHT)
        self.play(Create(vdict_using_zip))
        self.wait()
```

<pre data-manim-binder data-manim-classname="ShapesWithVDict">
class ShapesWithVDict(Scene):
    def construct(self):
        square = Square().set_color(RED)
        circle = Circle().set_color(YELLOW).next_to(square, UP)

        # create dict from list of tuples each having key-mobject pair
        pairs = [("s", square), ("c", circle)]
        my_dict = VDict(pairs, show_keys=True)

        # display it just like a VGroup
        self.play(Create(my_dict))
        self.wait()

        text = Tex("Some text").set_color(GREEN).next_to(square, DOWN)

        # add a key-value pair by wrapping it in a single-element list of tuple
        # after attrs branch is merged, it will be easier like \`.add(t=text)\`
        my_dict.add([("t", text)])
        self.wait()

        rect = Rectangle().next_to(text, DOWN)
        # can also do key assignment like a python dict
        my_dict["r"] = rect

        # access submobjects like a python dict
        my_dict["t"].set_color(PURPLE)
        self.play(my_dict["t"].animate.scale(3))
        self.wait()

        # also supports python dict styled reassignment
        my_dict["t"] = Tex("Some other text").set_color(BLUE)
        self.wait()

        # remove submobject by key
        my_dict.remove("t")
        self.wait()

        self.play(Uncreate(my_dict["s"]))
        self.wait()

        self.play(FadeOut(my_dict["c"]))
        self.wait()

        self.play(FadeOut(my_dict["r"], shift=DOWN))
        self.wait()

        # you can also make a VDict from an existing dict of mobjects
        plain_dict = {
            1: Integer(1).shift(DOWN),
            2: Integer(2).shift(2 \* DOWN),
            3: Integer(3).shift(3 \* DOWN),
        }

        vdict_from_plain_dict = VDict(plain_dict)
        vdict_from_plain_dict.shift(1.5 \* (UP + LEFT))
        self.play(Create(vdict_from_plain_dict))

        # you can even use zip
        vdict_using_zip = VDict(zip(["s", "c", "r"], [Square(), Circle(), Rectangle()]))
        vdict_using_zip.shift(1.5 \* RIGHT)
        self.play(Create(vdict_using_zip))
        self.wait()

</pre></div>

### Methods

| [`add`](#manim.mobject.types.vectorized_mobject.VDict.add)                                 | Adds the key-value pairs to the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object.                                                                                                 |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`add_key_value_pair`](#manim.mobject.types.vectorized_mobject.VDict.add_key_value_pair)   | A utility function used by [`add()`](#manim.mobject.types.vectorized_mobject.VDict.add) to add the key-value pair to [`submob_dict`](#manim.mobject.types.vectorized_mobject.VDict.submob_dict). |
| [`get_all_submobjects`](#manim.mobject.types.vectorized_mobject.VDict.get_all_submobjects) | To get all the submobjects associated with a particular [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object                                                                          |
| [`remove`](#manim.mobject.types.vectorized_mobject.VDict.remove)                           | Removes the mobject from the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object having the key key                                                                                  |

### Attributes

| `animate`             | Used to animate the application of any method of `self`.               |
|-----------------------|------------------------------------------------------------------------|
| `animation_overrides` |                                                                        |
| `color`               |                                                                        |
| `depth`               | The depth of the mobject.                                              |
| `fill_color`          | If there are multiple colors (for gradient) this returns the first one |
| `height`              | The height of the mobject.                                             |
| `n_points_per_curve`  |                                                                        |
| `sheen_factor`        |                                                                        |
| `stroke_color`        |                                                                        |
| `width`               | The width of the mobject.                                              |

#### \_original_\_init_\_(mapping_or_iterable={}, show_keys=False, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **mapping_or_iterable** (*Mapping* *[**Hashable* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*  *|* *Iterable* *[**tuple* *[**Hashable* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *]*)
  * **show_keys** (*bool*)
* **Return type:**
  None

#### add(mapping_or_iterable)

Adds the key-value pairs to the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object.

Also, it internally adds the value to the submobjects `list`
of [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject), which is responsible for actual on-screen display.

* **Parameters:**
  **mapping_or_iterable** (*Mapping* *[**Hashable* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]*  *|* *Iterable* *[**tuple* *[**Hashable* *,* [*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject) *]* *]*) – The parameter specifying the key-value mapping of keys and mobjects.
* **Returns:**
  Returns the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object on which this method was called.
* **Return type:**
  [`VDict`](#manim.mobject.types.vectorized_mobject.VDict)

### Examples

Normal usage:

```default
square_obj = Square()
my_dict.add([("s", square_obj)])
```

#### add_key_value_pair(key, value)

A utility function used by [`add()`](#manim.mobject.types.vectorized_mobject.VDict.add) to add the key-value pair
to [`submob_dict`](#manim.mobject.types.vectorized_mobject.VDict.submob_dict). Not really meant to be used externally.

* **Parameters:**
  * **key** (*Hashable*) – The key of the submobject to be added.
  * **value** ([*VMobject*](manim.mobject.types.vectorized_mobject.VMobject.md#manim.mobject.types.vectorized_mobject.VMobject)) – The mobject associated with the key
* **Return type:**
  None
* **Raises:**
  **TypeError** – If the value is not an instance of VMobject

### Examples

Normal usage:

```default
square_obj = Square()
self.add_key_value_pair("s", square_obj)
```

#### get_all_submobjects()

To get all the submobjects associated with a particular [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object

* **Returns:**
  All the submobjects associated with the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object
* **Return type:**
  `dict_values`

### Examples

Normal usage:

```default
for submob in my_dict.get_all_submobjects():
    self.play(Create(submob))
```

#### remove(key)

Removes the mobject from the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object having the key key

Also, it internally removes the mobject from the submobjects `list`
of [`Mobject`](manim.mobject.mobject.Mobject.md#manim.mobject.mobject.Mobject), (which is responsible for removing it from the screen)

* **Parameters:**
  **key** (*Hashable*) – The key of the submoject to be removed.
* **Returns:**
  Returns the [`VDict`](#manim.mobject.types.vectorized_mobject.VDict) object on which this method was called.
* **Return type:**
  [`VDict`](#manim.mobject.types.vectorized_mobject.VDict)

### Examples

Normal usage:

```default
my_dict.remove("square")
```
