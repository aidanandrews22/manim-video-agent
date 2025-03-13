# MarkupText

Qualified name: `manim.mobject.text.text\_mobject.MarkupText`

### *class* MarkupText(text, fill_opacity=1, stroke_width=0, color=None, font_size=48, line_spacing=-1, font='', slant='NORMAL', weight='NORMAL', justify=False, gradient=None, tab_width=4, height=None, width=None, should_center=True, disable_ligatures=False, warn_missing_font=True, \*\*kwargs)

Bases: [`SVGMobject`](manim.mobject.svg.svg_mobject.SVGMobject.md#manim.mobject.svg.svg_mobject.SVGMobject)

Display (non-LaTeX) text rendered using [Pango](https://pango.gnome.org/).

Text objects behave like a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)-like iterable of all characters
in the given text. In particular, slicing is possible.

**What is PangoMarkup?**

PangoMarkup is a small markup language like html and it helps you avoid using
“range of characters” while coloring or styling a piece a Text. You can use
this language with [`MarkupText`](#manim.mobject.text.text_mobject.MarkupText).

A simple example of a marked-up string might be:

```default
<span foreground="blue" size="x-large">Blue text</span> is <i>cool</i>!"
```

and it can be used with [`MarkupText`](#manim.mobject.text.text_mobject.MarkupText) as

<div id="markupexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MarkupExample <a class="headerlink" href="#markupexample">¶</a></p>![image](media/images/MarkupExample-1.png)
```python
from manim import *

class MarkupExample(Scene):
    def construct(self):
        text = MarkupText('<span foreground="blue" size="x-large">Blue text</span> is <i>cool</i>!"')
        self.add(text)
```

<pre data-manim-binder data-manim-classname="MarkupExample">
class MarkupExample(Scene):
    def construct(self):
        text = MarkupText('<span foreground="blue" size="x-large">Blue text</span> is <i>cool</i>!"')
        self.add(text)

</pre></div>

A more elaborate example would be:

<div id="markupelaborateexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MarkupElaborateExample <a class="headerlink" href="#markupelaborateexample">¶</a></p>![image](media/images/MarkupElaborateExample-1.png)
```python
from manim import *

class MarkupElaborateExample(Scene):
    def construct(self):
        text = MarkupText(
            '<span foreground="purple">ا</span><span foreground="red">َ</span>'
            'ل<span foreground="blue">ْ</span>ع<span foreground="red">َ</span>ر'
            '<span foreground="red">َ</span>ب<span foreground="red">ِ</span>ي'
            '<span foreground="green">ّ</span><span foreground="red">َ</span>ة'
            '<span foreground="blue">ُ</span>'
        )
        self.add(text)
```

<pre data-manim-binder data-manim-classname="MarkupElaborateExample">
class MarkupElaborateExample(Scene):
    def construct(self):
        text = MarkupText(
            '<span foreground="purple">ا</span><span foreground="red">َ</span>'
            'ل<span foreground="blue">ْ</span>ع<span foreground="red">َ</span>ر'
            '<span foreground="red">َ</span>ب<span foreground="red">ِ</span>ي'
            '<span foreground="green">ّ</span><span foreground="red">َ</span>ة'
            '<span foreground="blue">ُ</span>'
        )
        self.add(text)

</pre></div>

PangoMarkup can also contain XML features such as numeric character
entities such as `&#169;` for © can be used too.

The most general markup tag is `<span>`, then there are some
convenience tags.

Here is a list of supported tags:

- `<b>bold</b>`, `<i>italic</i>` and `<b><i>bold+italic</i></b>`
- `<u>underline</u>` and `<s>strike through</s>`
- `<tt>typewriter font</tt>`
- `<big>bigger font</big>` and `<small>smaller font</small>`
- `<sup>superscript</sup>` and `<sub>subscript</sub>`
- `<span underline="double" underline_color="green">double underline</span>`
- `<span underline="error">error underline</span>`
- `<span overline="single" overline_color="green">overline</span>`
- `<span strikethrough="true" strikethrough_color="red">strikethrough</span>`
- `<span font_family="sans">temporary change of font</span>`
- `<span foreground="red">temporary change of color</span>`
- `<span fgcolor="red">temporary change of color</span>`
- `<gradient from="YELLOW" to="RED">temporary gradient</gradient>`

For `<span>` markup, colors can be specified either as
hex triples like `#aabbcc` or as named CSS colors like
`AliceBlue`.
The `<gradient>` tag is handled by Manim rather than
Pango, and supports hex triplets or Manim constants like
`RED` or `RED_A`.
If you want to use Manim constants like `RED_A` together
with `<span>`, you will need to use Python’s f-String
syntax as follows:

```default
MarkupText(f'<span foreground="{RED_A}">here you go</span>')
```

If your text contains ligatures, the [`MarkupText`](#manim.mobject.text.text_mobject.MarkupText) class may
incorrectly determine the first and last letter when creating the
gradient. This is due to the fact that `fl` are two separate characters,
but might be set as one single glyph - a ligature. If your language
does not depend on ligatures, consider setting `disable_ligatures`
to `True`. If you must use ligatures, the `gradient` tag supports an optional
attribute `offset` which can be used to compensate for that error.

For example:

- `<gradient from="RED" to="YELLOW" offset="1">example</gradient>` to *start* the gradient one letter earlier
- `<gradient from="RED" to="YELLOW" offset=",1">example</gradient>` to *end* the gradient one letter earlier
- `<gradient from="RED" to="YELLOW" offset="2,1">example</gradient>` to *start* the gradient two letters earlier and *end* it one letter earlier

Specifying a second offset may be necessary if the text to be colored does
itself contain ligatures. The same can happen when using HTML entities for
special chars.

When using `underline`, `overline` or `strikethrough` together with
`<gradient>` tags, you will also need to use the offset, because
underlines are additional paths in the final `SVGMobject`.
Check out the following example.

Escaping of special characters: `>` **should** be written as `&gt;`
whereas `<` and `&` *must* be written as `&lt;` and
`&amp;`.

You can find more information about Pango markup formatting at the
corresponding documentation page:
[Pango Markup](https://docs.gtk.org/Pango/pango_markup.html).
Please be aware that not all features are supported by this class and that
the `<gradient>` tag mentioned above is not supported by Pango.

* **Parameters:**
  * **text** (*str*) – The text that needs to be created as mobject.
  * **fill_opacity** (*float*) – The fill opacity, with 1 meaning opaque and 0 meaning transparent.
  * **stroke_width** (*float*) – Stroke width.
  * **font_size** (*float*) – Font size.
  * **line_spacing** (*int*) – Line spacing.
  * **font** (*str*) – Global font setting for the entire text. Local overrides are possible.
  * **slant** (*str*) – Global slant setting, e.g. NORMAL or ITALIC. Local overrides are possible.
  * **weight** (*str*) – Global weight setting, e.g. NORMAL or BOLD. Local overrides are possible.
  * **gradient** (*tuple*) – Global gradient setting. Local overrides are possible.
  * **warn_missing_font** (*bool*) – If True (default), Manim will issue a warning if the font does not exist in the
    (case-sensitive) list of fonts returned from manimpango.list_fonts().
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **justify** (*bool*)
  * **tab_width** (*int*)
  * **height** (*int*)
  * **width** (*int*)
  * **should_center** (*bool*)
  * **disable_ligatures** (*bool*)
* **Returns:**
  The text displayed in form of a [`VGroup`](manim.mobject.types.vectorized_mobject.VGroup.md#manim.mobject.types.vectorized_mobject.VGroup)-like mobject.
* **Return type:**
  [`MarkupText`](#manim.mobject.text.text_mobject.MarkupText)

### Examples

<div id="basicmarkupexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: BasicMarkupExample <a class="headerlink" href="#basicmarkupexample">¶</a></p>![image](media/images/BasicMarkupExample-1.png)
```python
from manim import *

class BasicMarkupExample(Scene):
    def construct(self):
        text1 = MarkupText("<b>foo</b> <i>bar</i> <b><i>foobar</i></b>")
        text2 = MarkupText("<s>foo</s> <u>bar</u> <big>big</big> <small>small</small>")
        text3 = MarkupText("H<sub>2</sub>O and H<sub>3</sub>O<sup>+</sup>")
        text4 = MarkupText("type <tt>help</tt> for help")
        text5 = MarkupText(
            '<span underline="double">foo</span> <span underline="error">bar</span>'
        )
        group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        self.add(group)
```

<pre data-manim-binder data-manim-classname="BasicMarkupExample">
class BasicMarkupExample(Scene):
    def construct(self):
        text1 = MarkupText("<b>foo</b> <i>bar</i> <b><i>foobar</i></b>")
        text2 = MarkupText("<s>foo</s> <u>bar</u> <big>big</big> <small>small</small>")
        text3 = MarkupText("H<sub>2</sub>O and H<sub>3</sub>O<sup>+</sup>")
        text4 = MarkupText("type <tt>help</tt> for help")
        text5 = MarkupText(
            '<span underline="double">foo</span> <span underline="error">bar</span>'
        )
        group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        self.add(group)

</pre></div><div id="colorexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: ColorExample <a class="headerlink" href="#colorexample">¶</a></p>![image](media/images/ColorExample-1.png)
```python
from manim import *

class ColorExample(Scene):
    def construct(self):
        text1 = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        )
        text2 = MarkupText("nice gradient", gradient=(BLUE, GREEN))
        text3 = MarkupText(
            'nice <gradient from="RED" to="YELLOW">intermediate</gradient> gradient',
            gradient=(BLUE, GREEN),
        )
        text4 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW">causing trouble</gradient> here'
        )
        text5 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1">defeated</gradient> with offset'
        )
        text6 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1">floating</gradient> inside'
        )
        text7 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1,1">floating</gradient> inside'
        )
        group = VGroup(text1, text2, text3, text4, text5, text6, text7).arrange(DOWN)
        self.add(group)
```

<pre data-manim-binder data-manim-classname="ColorExample">
class ColorExample(Scene):
    def construct(self):
        text1 = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        )
        text2 = MarkupText("nice gradient", gradient=(BLUE, GREEN))
        text3 = MarkupText(
            'nice <gradient from="RED" to="YELLOW">intermediate</gradient> gradient',
            gradient=(BLUE, GREEN),
        )
        text4 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW">causing trouble</gradient> here'
        )
        text5 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1">defeated</gradient> with offset'
        )
        text6 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1">floating</gradient> inside'
        )
        text7 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1,1">floating</gradient> inside'
        )
        group = VGroup(text1, text2, text3, text4, text5, text6, text7).arrange(DOWN)
        self.add(group)

</pre></div><div id="underlineexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: UnderlineExample <a class="headerlink" href="#underlineexample">¶</a></p>![image](media/images/UnderlineExample-1.png)
```python
from manim import *

class UnderlineExample(Scene):
    def construct(self):
        text1 = MarkupText(
            '<span underline="double" underline_color="green">bla</span>'
        )
        text2 = MarkupText(
            '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
        )
        text3 = MarkupText(
            '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-1">aabb</gradient>y'
        )
        text4 = MarkupText(
            '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
        )
        text5 = MarkupText(
            '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-2">aabb</gradient>y'
        )
        group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        self.add(group)
```

<pre data-manim-binder data-manim-classname="UnderlineExample">
class UnderlineExample(Scene):
    def construct(self):
        text1 = MarkupText(
            '<span underline="double" underline_color="green">bla</span>'
        )
        text2 = MarkupText(
            '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
        )
        text3 = MarkupText(
            '<span underline="single" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-1">aabb</gradient>y'
        )
        text4 = MarkupText(
            '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED">aabb</gradient>y'
        )
        text5 = MarkupText(
            '<span underline="double" underline_color="green">xxx</span><gradient from="#ffff00" to="RED" offset="-2">aabb</gradient>y'
        )
        group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        self.add(group)

</pre></div><div id="fontexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: FontExample <a class="headerlink" href="#fontexample">¶</a></p>![image](media/images/FontExample-1.png)
```python
from manim import *

class FontExample(Scene):
    def construct(self):
        text1 = MarkupText(
            'all in sans <span font_family="serif">except this</span>', font="sans"
        )
        text2 = MarkupText(
            '<span font_family="serif">mixing</span> <span font_family="sans">fonts</span> <span font_family="monospace">is ugly</span>'
        )
        text3 = MarkupText("special char > or &gt;")
        text4 = MarkupText("special char &lt; and &amp;")
        group = VGroup(text1, text2, text3, text4).arrange(DOWN)
        self.add(group)
```

<pre data-manim-binder data-manim-classname="FontExample">
class FontExample(Scene):
    def construct(self):
        text1 = MarkupText(
            'all in sans <span font_family="serif">except this</span>', font="sans"
        )
        text2 = MarkupText(
            '<span font_family="serif">mixing</span> <span font_family="sans">fonts</span> <span font_family="monospace">is ugly</span>'
        )
        text3 = MarkupText("special char > or &gt;")
        text4 = MarkupText("special char &lt; and &amp;")
        group = VGroup(text1, text2, text3, text4).arrange(DOWN)
        self.add(group)

</pre></div><div id="newlineexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: NewlineExample <a class="headerlink" href="#newlineexample">¶</a></p>![image](media/images/NewlineExample-1.png)
```python
from manim import *

class NewlineExample(Scene):
    def construct(self):
        text = MarkupText('foooo<span foreground="red">oo\nbaa</span>aar')
        self.add(text)
```

<pre data-manim-binder data-manim-classname="NewlineExample">
class NewlineExample(Scene):
    def construct(self):
        text = MarkupText('foooo<span foreground="red">oo\\nbaa</span>aar')
        self.add(text)

</pre></div><div id="noligaturesexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: NoLigaturesExample <a class="headerlink" href="#noligaturesexample">¶</a></p>![image](media/images/NoLigaturesExample-1.png)
```python
from manim import *

class NoLigaturesExample(Scene):
    def construct(self):
        text1 = MarkupText('fl<gradient from="RED" to="GREEN">oat</gradient>ing')
        text2 = MarkupText('fl<gradient from="RED" to="GREEN">oat</gradient>ing', disable_ligatures=True)
        group = VGroup(text1, text2).arrange(DOWN)
        self.add(group)
```

<pre data-manim-binder data-manim-classname="NoLigaturesExample">
class NoLigaturesExample(Scene):
    def construct(self):
        text1 = MarkupText('fl<gradient from="RED" to="GREEN">oat</gradient>ing')
        text2 = MarkupText('fl<gradient from="RED" to="GREEN">oat</gradient>ing', disable_ligatures=True)
        group = VGroup(text1, text2).arrange(DOWN)
        self.add(group)

</pre></div>

As [`MarkupText`](#manim.mobject.text.text_mobject.MarkupText) uses Pango to render text, rendering non-English
characters is easily possible:

<div id="multilanguage" class="admonition admonition-manim-example">
<p class="admonition-title">Example: MultiLanguage <a class="headerlink" href="#multilanguage">¶</a></p>![image](media/images/MultiLanguage-1.png)
```python
from manim import *

class MultiLanguage(Scene):
    def construct(self):
        morning = MarkupText("வணக்கம்", font="sans-serif")
        japanese = MarkupText(
            '<span fgcolor="blue">日本</span>へようこそ'
        )  # works as in ``Text``.
        mess = MarkupText("Multi-Language", weight=BOLD)
        russ = MarkupText("Здравствуйте मस नम म ", font="sans-serif")
        hin = MarkupText("नमस्ते", font="sans-serif")
        chinese = MarkupText("臂猿「黛比」帶著孩子", font="sans-serif")
        group = VGroup(morning, japanese, mess, russ, hin, chinese).arrange(DOWN)
        self.add(group)
```

<pre data-manim-binder data-manim-classname="MultiLanguage">
class MultiLanguage(Scene):
    def construct(self):
        morning = MarkupText("வணக்கம்", font="sans-serif")
        japanese = MarkupText(
            '<span fgcolor="blue">日本</span>へようこそ'
        )  # works as in \`\`Text\`\`.
        mess = MarkupText("Multi-Language", weight=BOLD)
        russ = MarkupText("Здравствуйте मस नम म ", font="sans-serif")
        hin = MarkupText("नमस्ते", font="sans-serif")
        chinese = MarkupText("臂猿「黛比」帶著孩子", font="sans-serif")
        group = VGroup(morning, japanese, mess, russ, hin, chinese).arrange(DOWN)
        self.add(group)

</pre></div>

You can justify the text by passing `justify` parameter.

<div id="justifytext" class="admonition admonition-manim-example">
<p class="admonition-title">Example: JustifyText <a class="headerlink" href="#justifytext">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./JustifyText-1.mp4">
</video>
```python
from manim import *

class JustifyText(Scene):
    def construct(self):
        ipsum_text = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            "Praesent feugiat metus sit amet iaculis pulvinar. Nulla posuere "
            "quam a ex aliquam, eleifend consectetur tellus viverra. Aliquam "
            "fermentum interdum justo, nec rutrum elit pretium ac. Nam quis "
            "leo pulvinar, dignissim est at, venenatis nisi."
        )
        justified_text = MarkupText(ipsum_text, justify=True).scale(0.4)
        not_justified_text = MarkupText(ipsum_text, justify=False).scale(0.4)
        just_title = Title("Justified")
        njust_title = Title("Not Justified")
        self.add(njust_title, not_justified_text)
        self.play(
            FadeOut(not_justified_text),
            FadeIn(justified_text),
            FadeOut(njust_title),
            FadeIn(just_title),
        )
        self.wait(1)
```

<pre data-manim-binder data-manim-classname="JustifyText">
class JustifyText(Scene):
    def construct(self):
        ipsum_text = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            "Praesent feugiat metus sit amet iaculis pulvinar. Nulla posuere "
            "quam a ex aliquam, eleifend consectetur tellus viverra. Aliquam "
            "fermentum interdum justo, nec rutrum elit pretium ac. Nam quis "
            "leo pulvinar, dignissim est at, venenatis nisi."
        )
        justified_text = MarkupText(ipsum_text, justify=True).scale(0.4)
        not_justified_text = MarkupText(ipsum_text, justify=False).scale(0.4)
        just_title = Title("Justified")
        njust_title = Title("Not Justified")
        self.add(njust_title, not_justified_text)
        self.play(
            FadeOut(not_justified_text),
            FadeIn(justified_text),
            FadeOut(njust_title),
            FadeIn(just_title),
        )
        self.wait(1)

</pre></div>

### Tests

Check that the creation of [`MarkupText`](#manim.mobject.text.text_mobject.MarkupText) works:

```default
>>> MarkupText('The horse does not eat cucumber salad.')
MarkupText('The horse does not eat cucumber salad.')
```

### Methods

| `font_list`   |    |
|---------------|----|

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

#### \_count_real_chars(s)

Counts characters that will be displayed.

This is needed for partial coloring or gradients, because space
counts to the text’s len, but has no corresponding character.

#### \_extract_color_tags()

Used to determine which parts (if any) of the string should be formatted
with a custom color.

Removes the `<color>` tag, as it is not part of Pango’s markup and would cause an error.

Note: Using the `<color>` tags is deprecated. As soon as the legacy syntax is gone, this function
will be removed.

#### \_extract_gradient_tags()

Used to determine which parts (if any) of the string should be formatted
with a gradient.

Removes the `<gradient>` tag, as it is not part of Pango’s markup and would cause an error.

#### \_original_\_init_\_(text, fill_opacity=1, stroke_width=0, color=None, font_size=48, line_spacing=-1, font='', slant='NORMAL', weight='NORMAL', justify=False, gradient=None, tab_width=4, height=None, width=None, should_center=True, disable_ligatures=False, warn_missing_font=True, \*\*kwargs)

Initialize self.  See help(type(self)) for accurate signature.

* **Parameters:**
  * **text** (*str*)
  * **fill_opacity** (*float*)
  * **stroke_width** (*float*)
  * **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
  * **font_size** (*float*)
  * **line_spacing** (*int*)
  * **font** (*str*)
  * **slant** (*str*)
  * **weight** (*str*)
  * **justify** (*bool*)
  * **gradient** (*tuple*)
  * **tab_width** (*int*)
  * **height** (*int*)
  * **width** (*int*)
  * **should_center** (*bool*)
  * **disable_ligatures** (*bool*)
  * **warn_missing_font** (*bool*)
* **Return type:**
  None

#### \_parse_color(col)

Parse color given in `<color>` or `<gradient>` tags.

#### \_text2hash(color)

Generates `sha256` hash for file name.

* **Parameters:**
  **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor))

#### \_text2svg(color)

Convert the text to SVG using Pango.

* **Parameters:**
  **color** ([*ParsableManimColor*](manim.utils.color.core.md#manim.utils.color.core.ParsableManimColor) *|* *None*)
