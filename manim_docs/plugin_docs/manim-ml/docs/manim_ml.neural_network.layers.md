# manim_ml.neural_network.layers package

## Submodules

## manim_ml.neural_network.layers.convolutional module

## manim_ml.neural_network.layers.convolutional_to_convolutional module

## manim_ml.neural_network.layers.embedding module

### *class* manim_ml.neural_network.layers.embedding.EmbeddingLayer(point_radius=0.02, mean=array([0, 0]), covariance=array([[1., 0.], [0., 1.]]), dist_theme='gaussian', paired_query_mode=False, \*\*kwargs)

Bases: [`VGroupNeuralNetworkLayer`](#manim_ml.neural_network.layers.parent_layers.VGroupNeuralNetworkLayer)

NeuralNetwork embedding object that can show probability distributions

#### add_gaussian_distribution(gaussian_distribution)

Adds given GaussianDistribution to the list

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function EmbeddingLayer._create_override>}*

#### construct_gaussian_point_cloud(mean, covariance, point_color=ManimColor('#FFFFFF'), num_points=400)

Plots points sampled from a Gaussian with the given mean and covariance

#### construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Constructs the layer at network construction time

* **Parameters:**
  * **input_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – preceding layer
  * **output_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – following layer

#### get_distribution_location()

Returns mean of latent distribution in axes frame

#### make_forward_pass_animation(layer_args={}, \*\*kwargs)

Forward pass animation

#### remove_gaussian_distribution(gaussian_distribution)

Removes the given gaussian distribution from the embedding

#### sample_point_location_from_distribution()

Samples from the current latent distribution

### *class* manim_ml.neural_network.layers.embedding.NeuralNetworkEmbeddingTestScene(renderer=None, camera_class=<class 'manim.camera.camera.Camera'>, always_update_mobjects=False, random_seed=None, skip_animations=False)

Bases: `Scene`

#### construct()

Add content to the Scene.

From within `Scene.construct()`, display mobjects on screen by calling
`Scene.add()` and remove them from screen by calling `Scene.remove()`.
All mobjects currently on screen are kept in `Scene.mobjects`.  Play
animations by calling `Scene.play()`.

### Notes

Initialization code should go in `Scene.setup()`.  Termination code should
go in `Scene.tear_down()`.

### Examples

A typical manim script includes a class derived from `Scene` with an
overridden `Scene.construct()` method:

```python
class MyScene(Scene):
    def construct(self):
        self.play(Write(Text("Hello World!")))
```

#### SEE ALSO
`Scene.setup()`, `Scene.render()`, `Scene.tear_down()`

## manim_ml.neural_network.layers.embedding_to_feed_forward module

### *class* manim_ml.neural_network.layers.embedding_to_feed_forward.EmbeddingToFeedForward(input_layer, output_layer, animation_dot_color=ManimColor('#FC6255'), dot_radius=0.03, \*\*kwargs)

Bases: [`ConnectiveLayer`](#manim_ml.neural_network.layers.parent_layers.ConnectiveLayer)

Feed Forward to Embedding Layer

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function EmbeddingToFeedForward._create_override>}*

#### construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Constructs the layer at network construction time

* **Parameters:**
  * **input_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – preceding layer
  * **output_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – following layer

#### input_class

alias of [`EmbeddingLayer`](#manim_ml.neural_network.layers.embedding.EmbeddingLayer)

#### make_forward_pass_animation(layer_args={}, run_time=1.5, \*\*kwargs)

Makes dots diverge from the given location and move the decoder

#### output_class

alias of [`FeedForwardLayer`](#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer)

## manim_ml.neural_network.layers.feed_forward module

### *class* manim_ml.neural_network.layers.feed_forward.FeedForwardLayer(num_nodes, layer_buffer=0.05, node_radius=0.08, node_color=ManimColor('#58C4DD'), node_outline_color=ManimColor('#FFFFFF'), rectangle_color=ManimColor('#FFFFFF'), node_spacing=0.3, rectangle_fill_color=ManimColor('#000000'), node_stroke_width=2.0, rectangle_stroke_width=2.0, animation_dot_color=ManimColor('#FF862F'), activation_function=None, \*\*kwargs)

Bases: [`VGroupNeuralNetworkLayer`](#manim_ml.neural_network.layers.parent_layers.VGroupNeuralNetworkLayer)

Handles rendering a layer for a neural network

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function FeedForwardLayer._create_override>}*

#### construct_activation_function()

Construct the activation function

#### construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Creates the neural network layer

#### get_center()

Get center Point3Ds

#### get_height()

#### get_left()

Get left Point3Ds of a box bounding the `Mobject`

#### get_right()

Get right Point3Ds of a box bounding the `Mobject`

#### make_dropout_forward_pass_animation(layer_args, \*\*kwargs)

Makes a forward pass animation with dropout

#### make_forward_pass_animation(layer_args={}, \*\*kwargs)

#### move_to(mobject_or_point)

Moves the center of the layer to the given mobject or point

## manim_ml.neural_network.layers.feed_forward_to_embedding module

### *class* manim_ml.neural_network.layers.feed_forward_to_embedding.FeedForwardToEmbedding(input_layer, output_layer, animation_dot_color=ManimColor('#FC6255'), dot_radius=0.03, \*\*kwargs)

Bases: [`ConnectiveLayer`](#manim_ml.neural_network.layers.parent_layers.ConnectiveLayer)

Feed Forward to Embedding Layer

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function FeedForwardToEmbedding._create_override>}*

#### construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Constructs the layer at network construction time

* **Parameters:**
  * **input_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – preceding layer
  * **output_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – following layer

#### input_class

alias of [`FeedForwardLayer`](#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer)

#### make_forward_pass_animation(layer_args={}, run_time=1.5, \*\*kwargs)

Makes dots converge on a specific location

#### output_class

alias of [`EmbeddingLayer`](#manim_ml.neural_network.layers.embedding.EmbeddingLayer)

## manim_ml.neural_network.layers.feed_forward_to_feed_forward module

### *class* manim_ml.neural_network.layers.feed_forward_to_feed_forward.FeedForwardToFeedForward(input_layer, output_layer, passing_flash=True, dot_radius=0.05, animation_dot_color=ManimColor('#FF862F'), edge_color=ManimColor('#FFFFFF'), edge_width=1.5, camera=None, \*\*kwargs)

Bases: [`ConnectiveLayer`](#manim_ml.neural_network.layers.parent_layers.ConnectiveLayer)

Layer for connecting FeedForward layer to FeedForwardLayer

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function FeedForwardToFeedForward._create_override>, <class 'manim.animation.fading.FadeOut'>: <function FeedForwardToFeedForward._fadeout_animation>}*

#### construct_edges()

#### construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Constructs the layer at network construction time

* **Parameters:**
  * **input_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – preceding layer
  * **output_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – following layer

#### input_class

alias of [`FeedForwardLayer`](#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer)

#### make_forward_pass_animation(layer_args={}, run_time=1, feed_forward_dropout=0.0, \*\*kwargs)

Animation for passing information from one FeedForwardLayer to the next

#### modify_edge_colors(colors=None, magnitudes=None, color_scheme='inferno')

Changes the colors of edges

#### modify_edge_stroke_widths(widths)

Changes the widths of the edges

#### output_class

alias of [`FeedForwardLayer`](#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer)

## manim_ml.neural_network.layers.feed_forward_to_image module

### *class* manim_ml.neural_network.layers.feed_forward_to_image.FeedForwardToImage(input_layer, output_layer, animation_dot_color=ManimColor('#FC6255'), dot_radius=0.05, \*\*kwargs)

Bases: [`ConnectiveLayer`](#manim_ml.neural_network.layers.parent_layers.ConnectiveLayer)

Image Layer to FeedForward layer

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function FeedForwardToImage._create_override>}*

#### construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Constructs the layer at network construction time

* **Parameters:**
  * **input_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – preceding layer
  * **output_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – following layer

#### input_class

alias of [`FeedForwardLayer`](#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer)

#### make_forward_pass_animation(layer_args={}, \*\*kwargs)

Makes dots diverge from the given location and move to the feed forward nodes decoder

#### output_class

alias of [`ImageLayer`](#manim_ml.neural_network.layers.image.ImageLayer)

## manim_ml.neural_network.layers.feed_forward_to_vector module

### *class* manim_ml.neural_network.layers.feed_forward_to_vector.FeedForwardToVector(input_layer, output_layer, animation_dot_color=ManimColor('#FC6255'), dot_radius=0.05, \*\*kwargs)

Bases: [`ConnectiveLayer`](#manim_ml.neural_network.layers.parent_layers.ConnectiveLayer)

Image Layer to FeedForward layer

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function FeedForwardToVector._create_override>}*

#### construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Constructs the layer at network construction time

* **Parameters:**
  * **input_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – preceding layer
  * **output_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – following layer

#### input_class

alias of [`FeedForwardLayer`](#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer)

#### make_forward_pass_animation(layer_args={}, \*\*kwargs)

Makes dots diverge from the given location and move to the feed forward nodes decoder

#### output_class

alias of [`VectorLayer`](#manim_ml.neural_network.layers.vector.VectorLayer)

## manim_ml.neural_network.layers.image module

### *class* manim_ml.neural_network.layers.image.ImageLayer(numpy_image, height=1.5, show_image_on_create=True, \*\*kwargs)

Bases: [`NeuralNetworkLayer`](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)

Single Image Layer for Neural Network

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function ImageLayer._create_override>}*

#### construct_layer(input_layer, output_layer, \*\*kwargs)

Construct layer method

* **Parameters:**
  * **input_layer** – Input layer
  * **output_layer** – Output layer

#### *classmethod* from_path(image_path, grayscale=True, \*\*kwargs)

Creates a query using the paths

#### get_right()

Override get right

#### *property* height

The height of the mobject.

* **Return type:**
  `float`

### Examples

<div id="heightexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: HeightExample <a class="headerlink" href="#heightexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./HeightExample-1.mp4">
</video>
```python
from manim import *

class HeightExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.height))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(height=5))
        self.wait()
```

<pre data-manim-binder data-manim-classname="HeightExample">
class HeightExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.height))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(height=5))
        self.wait()

</pre></div>

#### SEE ALSO
`length_over_dim()`

#### make_forward_pass_animation(layer_args={}, \*\*kwargs)

#### scale(scale_factor, \*\*kwargs)

Scales the image mobject

#### *property* width

The width of the mobject.

* **Return type:**
  `float`

### Examples

<div id="widthexample" class="admonition admonition-manim-example">
<p class="admonition-title">Example: WidthExample <a class="headerlink" href="#widthexample">¶</a></p><video
    class="manim-video"
    controls
    loop
    autoplay
    src="./WidthExample-1.mp4">
</video>
```python
from manim import *

class WidthExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.width))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(width=7))
        self.wait()
```

<pre data-manim-binder data-manim-classname="WidthExample">
class WidthExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.width))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(width=7))
        self.wait()

</pre></div>

#### SEE ALSO
`length_over_dim()`

## manim_ml.neural_network.layers.image_to_feed_forward module

### *class* manim_ml.neural_network.layers.image_to_feed_forward.ImageToFeedForward(input_layer, output_layer, animation_dot_color=ManimColor('#FC6255'), dot_radius=0.05, \*\*kwargs)

Bases: [`ConnectiveLayer`](#manim_ml.neural_network.layers.parent_layers.ConnectiveLayer)

Image Layer to FeedForward layer

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function ImageToFeedForward._create_override>}*

#### construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Constructs the layer at network construction time

* **Parameters:**
  * **input_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – preceding layer
  * **output_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – following layer

#### input_class

alias of [`ImageLayer`](#manim_ml.neural_network.layers.image.ImageLayer)

#### make_forward_pass_animation(layer_args={}, \*\*kwargs)

Makes dots diverge from the given location and move to the feed forward nodes decoder

#### output_class

alias of [`FeedForwardLayer`](#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer)

## manim_ml.neural_network.layers.paired_query module

### *class* manim_ml.neural_network.layers.paired_query.PairedQueryLayer(positive, negative, stroke_width=5, font_size=18, spacing=0.5, \*\*kwargs)

Bases: [`NeuralNetworkLayer`](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)

Paired Query Layer

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function PairedQueryLayer._create_override>}*

#### construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Constructs the layer at network construction time

* **Parameters:**
  * **input_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – preceding layer
  * **output_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – following layer

#### *classmethod* from_paths(positive_path, negative_path, grayscale=True, \*\*kwargs)

Creates a query using the paths

#### make_assets()

Constructs the assets needed for a query layer

#### make_forward_pass_animation(layer_args={}, \*\*kwargs)

Forward pass for query

## manim_ml.neural_network.layers.paired_query_to_feed_forward module

### *class* manim_ml.neural_network.layers.paired_query_to_feed_forward.PairedQueryToFeedForward(input_layer, output_layer, animation_dot_color=ManimColor('#FC6255'), dot_radius=0.02, \*\*kwargs)

Bases: [`ConnectiveLayer`](#manim_ml.neural_network.layers.parent_layers.ConnectiveLayer)

PairedQuery layer to FeedForward layer

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function PairedQueryToFeedForward._create_override>}*

#### construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Constructs the layer at network construction time

* **Parameters:**
  * **input_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – preceding layer
  * **output_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – following layer

#### input_class

alias of [`PairedQueryLayer`](#manim_ml.neural_network.layers.paired_query.PairedQueryLayer)

#### make_forward_pass_animation(layer_args={}, \*\*kwargs)

Makes dots diverge from the given location and move to the feed forward nodes decoder

#### output_class

alias of [`FeedForwardLayer`](#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer)

## manim_ml.neural_network.layers.parent_layers module

### *class* manim_ml.neural_network.layers.parent_layers.BlankConnective(input_layer, output_layer, \*\*kwargs)

Bases: [`ConnectiveLayer`](#manim_ml.neural_network.layers.parent_layers.ConnectiveLayer)

Connective layer to be used when the given pair of layers is undefined

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function BlankConnective._create_override>}*

#### make_forward_pass_animation(run_time=1.5, layer_args={}, \*\*kwargs)

### *class* manim_ml.neural_network.layers.parent_layers.ConnectiveLayer(input_layer, output_layer, \*\*kwargs)

Bases: [`VGroupNeuralNetworkLayer`](#manim_ml.neural_network.layers.parent_layers.VGroupNeuralNetworkLayer)

Forward pass animation for a given pair of layers

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function ConnectiveLayer._create_override>}*

#### *abstract* make_forward_pass_animation(run_time=2.0, layer_args={}, \*\*kwargs)

### *class* manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer(text=None, \*args, \*\*kwargs)

Bases: `ABC`, `Group`

Abstract Neural Network Layer class

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function NeuralNetworkLayer._create_override>}*

#### *abstract* construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Constructs the layer at network construction time

* **Parameters:**
  * **input_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – preceding layer
  * **output_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – following layer

#### *abstract* make_forward_pass_animation(layer_args={}, \*\*kwargs)

### *class* manim_ml.neural_network.layers.parent_layers.ThreeDLayer

Bases: `ABC`

Abstract class for 3D layers

### *class* manim_ml.neural_network.layers.parent_layers.VGroupNeuralNetworkLayer(\*args, \*\*kwargs)

Bases: [`NeuralNetworkLayer`](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function VGroupNeuralNetworkLayer._create_override>}*

#### *abstract* make_forward_pass_animation(\*\*kwargs)

## manim_ml.neural_network.layers.triplet module

### *class* manim_ml.neural_network.layers.triplet.TripletLayer(anchor, positive, negative, stroke_width=5, font_size=22, buff=0.2, \*\*kwargs)

Bases: [`NeuralNetworkLayer`](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)

Shows triplet images

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function TripletLayer._create_override>}*

#### construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Constructs the layer at network construction time

* **Parameters:**
  * **input_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – preceding layer
  * **output_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – following layer

#### *classmethod* from_paths(anchor_path, positive_path, negative_path, grayscale=True, font_size=22, buff=0.2)

Creates a triplet using the anchor paths

#### make_assets()

Constructs the assets needed for a triplet layer

#### make_forward_pass_animation(layer_args={}, \*\*kwargs)

Forward pass for triplet

## manim_ml.neural_network.layers.triplet_to_feed_forward module

### *class* manim_ml.neural_network.layers.triplet_to_feed_forward.TripletToFeedForward(input_layer, output_layer, animation_dot_color=ManimColor('#FC6255'), dot_radius=0.02, \*\*kwargs)

Bases: [`ConnectiveLayer`](#manim_ml.neural_network.layers.parent_layers.ConnectiveLayer)

TripletLayer to FeedForward layer

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function TripletToFeedForward._create_override>}*

#### construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Constructs the layer at network construction time

* **Parameters:**
  * **input_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – preceding layer
  * **output_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – following layer

#### input_class

alias of [`TripletLayer`](#manim_ml.neural_network.layers.triplet.TripletLayer)

#### make_forward_pass_animation(layer_args={}, \*\*kwargs)

Makes dots diverge from the given location and move to the feed forward nodes decoder

#### output_class

alias of [`FeedForwardLayer`](#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer)

## manim_ml.neural_network.layers.util module

### manim_ml.neural_network.layers.util.get_connective_layer(input_layer, output_layer)

Deduces the relevant connective layer

## manim_ml.neural_network.layers.vector module

### *class* manim_ml.neural_network.layers.vector.VectorLayer(num_values, value_func=<function VectorLayer.<lambda>>, \*\*kwargs)

Bases: [`VGroupNeuralNetworkLayer`](#manim_ml.neural_network.layers.parent_layers.VGroupNeuralNetworkLayer)

Shows a vector

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function VectorLayer._create_override>}*

#### construct_layer(input_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), output_layer: [NeuralNetworkLayer](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer), \*\*kwargs)

Constructs the layer at network construction time

* **Parameters:**
  * **input_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – preceding layer
  * **output_layer** ([*NeuralNetworkLayer*](#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)) – following layer

#### make_forward_pass_animation(layer_args={}, \*\*kwargs)

#### make_vector()

Makes the vector

## Module contents
