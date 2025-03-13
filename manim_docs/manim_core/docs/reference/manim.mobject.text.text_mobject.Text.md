# Text

Qualified name: `manim.mobject.text.text\_mobject.Text`

### *class* Text(text, fill_opacity=1.0, stroke_width=0, \*, color=ManimColor('#FFFFFF'), font_size=48, line_spacing=-1, font='', slant='NORMAL', weight='NORMAL', t2c=None, t2f=None, t2g=None, t2s=None, t2w=None, gradient=None, tab_width=4, warn_missing_font=True, height=None, width=None, should_center=True, disable_ligatures=False, use_svg_cache=False, \*\*kwargs)

Bases: [`SVGMobject`](manim.mobject.svg.svg_mobject.SVGMobject.md#manim.mobject.svg.svg_mobject.SVGMobject)

Display (non-LaTeX) text rendered using [Pango](https://pango.gnome.org/).

Text objects behave like a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)-like iterable of all characters
in the given text. In particular, slicing is possible.

* **Parameters:**
  * **text** (*str*) – The text that needs to be created as a mobject.
  * **font** (*str*) – The font family to be used to render the text. This is either a system font or
    one loaded with register_font(). Note that font family names may be different
    across operating systems.
  * **warn_missing_font** (*bool*) – If True (default), Manim will issue a warning if the font does not exist in the
    (case-sensitive) list of fonts returned from manimpango.list_fonts().
  * **fill_opacity** (*float*)
  * **stroke_width** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **font_size** (*float*)
  * **line_spacing** (*float*)
  * **slant** (*str*)
  * **weight** (*str*)
  * **t2c** (*dict* *[**str* *,* *str* *]*)
  * **t2f** (*dict* *[**str* *,* *str* *]*)
  * **t2g** (*dict* *[**str* *,* *tuple* *]*)
  * **t2s** (*dict* *[**str* *,* *str* *]*)
  * **t2w** (*dict* *[**str* *,* *str* *]*)
  * **gradient** (*tuple*)
  * **tab_width** (*int*)
  * **height** (*float*)
  * **width** (*float*)
  * **should_center** (*bool*)
  * **disable_ligatures** (*bool*)
  * **use_svg_cache** (*bool*)
* **Returns:**
  The mobject-like [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup).
* **Return type:**
  [`Text`](#manim.mobject.text.text_mobject.Text)

### Examples

<div id="example1text" class="admonition admonition-manim-example">
<p class="admonition-title">Example: Example1Text <a class="headerlink" href="#example1text">¶</a></p>![image](media/images/Example1Text-1.png)
```python
from manim import *

class Example1Text(Scene):
    def construct(self):
        text = Text('Hello world').scale(3)
        self.add(text)
```

<pre data-manim-binder data-manim-classname="Example1Text">
class Example1Text(Scene):
    def construct(self):
        text = Text('Hello world').scale(3)
        self.add(text)

</pre></div><div id="textcolorexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: TextColorExample <a class="headerlink" href="#textcolorexample">¶</a></p>![image](media/images/TextColorExample-1.png)
```python
from manim import *

class TextColorExample(Scene):
    def construct(self):
        text1 = Text('Hello world', color=BLUE).scale(3)
        text2 = Text('Hello world', gradient=(BLUE, GREEN)).scale(3).next_to(text1, DOWN)
        self.add(text1, text2)
```

<pre data-manim-binder data-manim-classname="TextColorExample">
class TextColorExample(Scene):
    def construct(self):
        text1 = Text('Hello world', color=BLUE).scale(3)
        text2 = Text('Hello world', gradient=(BLUE, GREEN)).scale(3).next_to(text1, DOWN)
        self.add(text1, text2)

</pre></div><div id="textitalicandboldexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: TextItalicAndBoldExample <a class="headerlink" href="#textitalicandboldexample">¶</a></p>![image](media/images/TextItalicAndBoldExample-1.png)
```python
from manim import *

class TextItalicAndBoldExample(Scene):
    def construct(self):
        text1 = Text("Hello world", slant=ITALIC)
        text2 = Text("Hello world", t2s={'world':ITALIC})
        text3 = Text("Hello world", weight=BOLD)
        text4 = Text("Hello world", t2w={'world':BOLD})
        text5 = Text("Hello world", t2c={'o':YELLOW}, disable_ligatures=True)
        text6 = Text(
            "Visit us at docs.manim.community",
            t2c={"docs.manim.community": YELLOW},
            disable_ligatures=True,
       )
        text6.scale(1.3).shift(DOWN)
        self.add(text1, text2, text3, text4, text5 , text6)
        Group(*self.mobjects).arrange(DOWN, buff=.8).set(height=config.frame_height-LARGE_BUFF)
```

<pre data-manim-binder data-manim-classname="TextItalicAndBoldExample">
class TextItalicAndBoldExample(Scene):
    def construct(self):
        text1 = Text("Hello world", slant=ITALIC)
        text2 = Text("Hello world", t2s={'world':ITALIC})
        text3 = Text("Hello world", weight=BOLD)
        text4 = Text("Hello world", t2w={'world':BOLD})
        text5 = Text("Hello world", t2c={'o':YELLOW}, disable_ligatures=True)
        text6 = Text(
            "Visit us at docs.manim.community",
            t2c={"docs.manim.community": YELLOW},
            disable_ligatures=True,
       )
        text6.scale(1.3).shift(DOWN)
        self.add(text1, text2, text3, text4, text5 , text6)
        Group(\*self.mobjects).arrange(DOWN, buff=.8).set(height=config.frame_height-LARGE_BUFF)

</pre></div><div id="textmorecustomization" class="admonition admonition-manim-example">
<p class="admonition-title">Example: TextMoreCustomization <a class="headerlink" href="#textmorecustomization">¶</a></p>![image](media/images/TextMoreCustomization-1.png)
```python
from manim import *

class TextMoreCustomization(Scene):
    def construct(self):
        text1 = Text(
            'Google',
            t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
                 '[2:3]': '#fbb003', '[3:4]': '#3174f0',
                 '[4:5]': '#269a43', '[5:]': '#e53125'}, font_size=58).scale(3)
        self.add(text1)
```

<pre data-manim-binder data-manim-classname="TextMoreCustomization">
class TextMoreCustomization(Scene):
    def construct(self):
        text1 = Text(
            'Google',
            t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
                 '[2:3]': '#fbb003', '[3:4]': '#3174f0',
                 '[4:5]': '#269a43', '[5:]': '#e53125'}, font_size=58).scale(3)
        self.add(text1)

</pre></div>

As [`Text`](#manim.mobject.text.text_mobject.Text) uses Pango to render text, rendering non-English
characters is easily possible:

<div id="multiplefonts" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MultipleFonts <a class="headerlink" href="#multiplefonts">¶</a></p>![image](media/images/MultipleFonts-1.png)
```python
from manim import *

class MultipleFonts(Scene):
    def construct(self):
        morning = Text("வணக்கம்", font="sans-serif")
        japanese = Text(
            "日本へようこそ", t2c={"日本": BLUE}
        )  # works same as ``Text``.
        mess = Text("Multi-Language", weight=BOLD)
        russ = Text("Здравствуйте मस नम म ", font="sans-serif")
        hin = Text("नमस्ते", font="sans-serif")
        arb = Text(
            "صباح الخير \n تشرفت بمقابلتك", font="sans-serif"
        )  # don't mix RTL and LTR languages nothing shows up then ;-)
        chinese = Text("臂猿「黛比」帶著孩子", font="sans-serif")
        self.add(morning, japanese, mess, russ, hin, arb, chinese)
        for i,mobj in enumerate(self.mobjects):
            mobj.shift(DOWN*(i-3))
```

<pre data-manim-binder data-manim-classname="MultipleFonts">
class MultipleFonts(Scene):
    def construct(self):
        morning = Text("வணக்கம்", font="sans-serif")
        japanese = Text(
            "日本へようこそ", t2c={"日本": BLUE}
        )  # works same as \`\`Text\`\`.
        mess = Text("Multi-Language", weight=BOLD)
        russ = Text("Здравствуйте मस नम म ", font="sans-serif")
        hin = Text("नमस्ते", font="sans-serif")
        arb = Text(
            "صباح الخير \\n تشرفت بمقابلتك", font="sans-serif"
        )  # don't mix RTL and LTR languages nothing shows up then ;-)
        chinese = Text("臂猿「黛比」帶著孩子", font="sans-serif")
        self.add(morning, japanese, mess, russ, hin, arb, chinese)
        for i,mobj in enumerate(self.mobjects):
            mobj.shift(DOWN\*(i-3))

</pre></div><div id="pangorender" class="admonition admonition-manim-example">
<p class="admonition-title">Example: PangoRender <a class="headerlink" href="#pangorender">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./PangoRender-1.mp4">
</video>
```python
from manim import *

class PangoRender(Scene):
    def construct(self):
        morning = Text("வணக்கம்", font="sans-serif")
        self.play(Write(morning))
        self.wait(2)
```

<pre data-manim-binder data-manim-classname="PangoRender">
class PangoRender(Scene):
    def construct(self):
        morning = Text("வணக்கம்", font="sans-serif")
        self.play(Write(morning))
        self.wait(2)

</pre></div>

### Tests

Check that the creation of [`Text`](#manim.mobject.text.text_mobject.Text) works:

```default
>>> Text('The horse does not eat cucumber salad.')
Text('The horse does not eat cucumber salad.')
```

### Methods

| `font_list`                                                        |                         |
|--------------------------------------------------------------------|-------------------------|
| [`init_colors`](#manim.mobject.text.text_mobject.Text.init_colors) | Initializes the colors. |

### Attributes

| `animate`             | Used to animate the application of any method of `self`.               |
|-----------------------|------------------------------------------------------------------------|
| `animation_overrides` |                                                                        |
| `color`               |                                                                        |
| `depth`               | The depth of the mobject.                                              |
| `fill_color`          | If there are multiple colors (for gradient) this returns the first one |
| `font_size`           |                                                                        |
| `hash_seed`           | A unique hash representing the result of the generated mobject points. |
| `height`              | The height of the mobject.                                             |
| `n_points_per_curve`  |                                                                        |
| `sheen_factor`        |                                                                        |
| `stroke_color`        |                                                                        |
| `width`               | The width of the mobject.                                              |

#### \_find_indexes(word, text)

Finds the indexes of `text` in `word`.

* **Parameters:**
  * **word** (*str*)
  * **text** (*str*)

#### \_original_\_init_\_(text, fill_opacity=1.0, stroke_width=0, color=None, font_size=48, line_spacing=-1, font='', slant='NORMAL', weight='NORMAL', t2c=None, t2f=None, t2g=None, t2s=None, t2w=None, gradient=None, tab_width=4, warn_missing_font=True, height=None, width=None, should_center=True, disable_ligatures=False, use_svg_cache=False, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **text** (*str*)
  * **fill_opacity** (*float*)
  * **stroke_width** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **font_size** (*float*)
  * **line_spacing** (*float*)
  * **font** (*str*)
  * **slant** (*str*)
  * **weight** (*str*)
  * **t2c** (*dict* *[**str* *,* *str* *]*)
  * **t2f** (*dict* *[**str* *,* *str* *]*)
  * **t2g** (*dict* *[**str* *,* *tuple* *]*)
  * **t2s** (*dict* *[**str* *,* *str* *]*)
  * **t2w** (*dict* *[**str* *,* *str* *]*)
  * **gradient** (*tuple*)
  * **tab_width** (*int*)
  * **warn_missing_font** (*bool*)
  * **height** (*float*)
  * **width** (*float*)
  * **should_center** (*bool*)
  * **disable_ligatures** (*bool*)
  * **use_svg_cache** (*bool*)
* **Return type:**
  None

#### \_set_color_by_t2c(t2c=None)

Sets color for specified strings.

#### ATTENTION
Deprecated
The method Text._set_color_by_t2c has been deprecated since v0.14.0 and is expected to be removed after v0.15.0. This was internal function, you shouldn’t be using it anyway.

#### \_set_color_by_t2g(t2g=None)

Sets gradient colors for specified
: strings. Behaves similarly to `set_color_by_t2c`.

#### ATTENTION
Deprecated
The method Text._set_color_by_t2g has been deprecated since v0.14.0 and is expected to be removed after v0.15.0. This was internal function, you shouldn’t be using it anyway.

#### \_text2hash(color)

Generates `sha256` hash for file name.

* **Parameters:**
  **color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor))

#### \_text2settings(color)

Converts the texts and styles to a setting for parsing.

* **Parameters:**
  **color** (*str*)

#### \_text2svg(color)

Convert the text to SVG using Pango.

* **Parameters:**
  **color** ([*ManimColor*](manim.utils.color.core.ManimColor.md#manim.utils.color.core.ManimColor))

#### init_colors(propagate_colors=True)

Initializes the colors.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.
