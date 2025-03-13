# manim_ml.neural_network package

## Subpackages

* [manim_ml.neural_network.layers package](manim_ml.neural_network.layers.md)
  * [Submodules](manim_ml.neural_network.layers.md#submodules)
  * [manim_ml.neural_network.layers.convolutional module](manim_ml.neural_network.layers.md#manim-ml-neural-network-layers-convolutional-module)
  * [manim_ml.neural_network.layers.convolutional_to_convolutional module](manim_ml.neural_network.layers.md#manim-ml-neural-network-layers-convolutional-to-convolutional-module)
  * [manim_ml.neural_network.layers.embedding module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.embedding)
    * [`EmbeddingLayer`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding.EmbeddingLayer)
      * [`EmbeddingLayer.add_gaussian_distribution()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding.EmbeddingLayer.add_gaussian_distribution)
      * [`EmbeddingLayer.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding.EmbeddingLayer.animation_overrides)
      * [`EmbeddingLayer.construct_gaussian_point_cloud()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding.EmbeddingLayer.construct_gaussian_point_cloud)
      * [`EmbeddingLayer.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding.EmbeddingLayer.construct_layer)
      * [`EmbeddingLayer.get_distribution_location()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding.EmbeddingLayer.get_distribution_location)
      * [`EmbeddingLayer.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding.EmbeddingLayer.make_forward_pass_animation)
      * [`EmbeddingLayer.remove_gaussian_distribution()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding.EmbeddingLayer.remove_gaussian_distribution)
      * [`EmbeddingLayer.sample_point_location_from_distribution()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding.EmbeddingLayer.sample_point_location_from_distribution)
    * [`NeuralNetworkEmbeddingTestScene`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding.NeuralNetworkEmbeddingTestScene)
      * [`NeuralNetworkEmbeddingTestScene.construct()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding.NeuralNetworkEmbeddingTestScene.construct)
  * [manim_ml.neural_network.layers.embedding_to_feed_forward module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.embedding_to_feed_forward)
    * [`EmbeddingToFeedForward`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding_to_feed_forward.EmbeddingToFeedForward)
      * [`EmbeddingToFeedForward.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding_to_feed_forward.EmbeddingToFeedForward.animation_overrides)
      * [`EmbeddingToFeedForward.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding_to_feed_forward.EmbeddingToFeedForward.construct_layer)
      * [`EmbeddingToFeedForward.input_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding_to_feed_forward.EmbeddingToFeedForward.input_class)
      * [`EmbeddingToFeedForward.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding_to_feed_forward.EmbeddingToFeedForward.make_forward_pass_animation)
      * [`EmbeddingToFeedForward.output_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.embedding_to_feed_forward.EmbeddingToFeedForward.output_class)
  * [manim_ml.neural_network.layers.feed_forward module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.feed_forward)
    * [`FeedForwardLayer`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer)
      * [`FeedForwardLayer.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer.animation_overrides)
      * [`FeedForwardLayer.construct_activation_function()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer.construct_activation_function)
      * [`FeedForwardLayer.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer.construct_layer)
      * [`FeedForwardLayer.get_center()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer.get_center)
      * [`FeedForwardLayer.get_height()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer.get_height)
      * [`FeedForwardLayer.get_left()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer.get_left)
      * [`FeedForwardLayer.get_right()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer.get_right)
      * [`FeedForwardLayer.make_dropout_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer.make_dropout_forward_pass_animation)
      * [`FeedForwardLayer.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer.make_forward_pass_animation)
      * [`FeedForwardLayer.move_to()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward.FeedForwardLayer.move_to)
  * [manim_ml.neural_network.layers.feed_forward_to_embedding module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.feed_forward_to_embedding)
    * [`FeedForwardToEmbedding`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_embedding.FeedForwardToEmbedding)
      * [`FeedForwardToEmbedding.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_embedding.FeedForwardToEmbedding.animation_overrides)
      * [`FeedForwardToEmbedding.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_embedding.FeedForwardToEmbedding.construct_layer)
      * [`FeedForwardToEmbedding.input_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_embedding.FeedForwardToEmbedding.input_class)
      * [`FeedForwardToEmbedding.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_embedding.FeedForwardToEmbedding.make_forward_pass_animation)
      * [`FeedForwardToEmbedding.output_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_embedding.FeedForwardToEmbedding.output_class)
  * [manim_ml.neural_network.layers.feed_forward_to_feed_forward module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.feed_forward_to_feed_forward)
    * [`FeedForwardToFeedForward`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_feed_forward.FeedForwardToFeedForward)
      * [`FeedForwardToFeedForward.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_feed_forward.FeedForwardToFeedForward.animation_overrides)
      * [`FeedForwardToFeedForward.construct_edges()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_feed_forward.FeedForwardToFeedForward.construct_edges)
      * [`FeedForwardToFeedForward.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_feed_forward.FeedForwardToFeedForward.construct_layer)
      * [`FeedForwardToFeedForward.input_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_feed_forward.FeedForwardToFeedForward.input_class)
      * [`FeedForwardToFeedForward.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_feed_forward.FeedForwardToFeedForward.make_forward_pass_animation)
      * [`FeedForwardToFeedForward.modify_edge_colors()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_feed_forward.FeedForwardToFeedForward.modify_edge_colors)
      * [`FeedForwardToFeedForward.modify_edge_stroke_widths()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_feed_forward.FeedForwardToFeedForward.modify_edge_stroke_widths)
      * [`FeedForwardToFeedForward.output_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_feed_forward.FeedForwardToFeedForward.output_class)
  * [manim_ml.neural_network.layers.feed_forward_to_image module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.feed_forward_to_image)
    * [`FeedForwardToImage`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_image.FeedForwardToImage)
      * [`FeedForwardToImage.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_image.FeedForwardToImage.animation_overrides)
      * [`FeedForwardToImage.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_image.FeedForwardToImage.construct_layer)
      * [`FeedForwardToImage.input_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_image.FeedForwardToImage.input_class)
      * [`FeedForwardToImage.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_image.FeedForwardToImage.make_forward_pass_animation)
      * [`FeedForwardToImage.output_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_image.FeedForwardToImage.output_class)
  * [manim_ml.neural_network.layers.feed_forward_to_vector module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.feed_forward_to_vector)
    * [`FeedForwardToVector`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_vector.FeedForwardToVector)
      * [`FeedForwardToVector.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_vector.FeedForwardToVector.animation_overrides)
      * [`FeedForwardToVector.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_vector.FeedForwardToVector.construct_layer)
      * [`FeedForwardToVector.input_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_vector.FeedForwardToVector.input_class)
      * [`FeedForwardToVector.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_vector.FeedForwardToVector.make_forward_pass_animation)
      * [`FeedForwardToVector.output_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.feed_forward_to_vector.FeedForwardToVector.output_class)
  * [manim_ml.neural_network.layers.image module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.image)
    * [`ImageLayer`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image.ImageLayer)
      * [`ImageLayer.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image.ImageLayer.animation_overrides)
      * [`ImageLayer.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image.ImageLayer.construct_layer)
      * [`ImageLayer.from_path()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image.ImageLayer.from_path)
      * [`ImageLayer.get_right()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image.ImageLayer.get_right)
      * [`ImageLayer.height`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image.ImageLayer.height)
      * [`ImageLayer.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image.ImageLayer.make_forward_pass_animation)
      * [`ImageLayer.scale()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image.ImageLayer.scale)
      * [`ImageLayer.width`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image.ImageLayer.width)
  * [manim_ml.neural_network.layers.image_to_feed_forward module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.image_to_feed_forward)
    * [`ImageToFeedForward`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image_to_feed_forward.ImageToFeedForward)
      * [`ImageToFeedForward.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image_to_feed_forward.ImageToFeedForward.animation_overrides)
      * [`ImageToFeedForward.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image_to_feed_forward.ImageToFeedForward.construct_layer)
      * [`ImageToFeedForward.input_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image_to_feed_forward.ImageToFeedForward.input_class)
      * [`ImageToFeedForward.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image_to_feed_forward.ImageToFeedForward.make_forward_pass_animation)
      * [`ImageToFeedForward.output_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.image_to_feed_forward.ImageToFeedForward.output_class)
  * [manim_ml.neural_network.layers.paired_query module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.paired_query)
    * [`PairedQueryLayer`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.paired_query.PairedQueryLayer)
      * [`PairedQueryLayer.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.paired_query.PairedQueryLayer.animation_overrides)
      * [`PairedQueryLayer.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.paired_query.PairedQueryLayer.construct_layer)
      * [`PairedQueryLayer.from_paths()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.paired_query.PairedQueryLayer.from_paths)
      * [`PairedQueryLayer.make_assets()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.paired_query.PairedQueryLayer.make_assets)
      * [`PairedQueryLayer.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.paired_query.PairedQueryLayer.make_forward_pass_animation)
  * [manim_ml.neural_network.layers.paired_query_to_feed_forward module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.paired_query_to_feed_forward)
    * [`PairedQueryToFeedForward`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.paired_query_to_feed_forward.PairedQueryToFeedForward)
      * [`PairedQueryToFeedForward.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.paired_query_to_feed_forward.PairedQueryToFeedForward.animation_overrides)
      * [`PairedQueryToFeedForward.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.paired_query_to_feed_forward.PairedQueryToFeedForward.construct_layer)
      * [`PairedQueryToFeedForward.input_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.paired_query_to_feed_forward.PairedQueryToFeedForward.input_class)
      * [`PairedQueryToFeedForward.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.paired_query_to_feed_forward.PairedQueryToFeedForward.make_forward_pass_animation)
      * [`PairedQueryToFeedForward.output_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.paired_query_to_feed_forward.PairedQueryToFeedForward.output_class)
  * [manim_ml.neural_network.layers.parent_layers module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.parent_layers)
    * [`BlankConnective`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.BlankConnective)
      * [`BlankConnective.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.BlankConnective.animation_overrides)
      * [`BlankConnective.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.BlankConnective.make_forward_pass_animation)
    * [`ConnectiveLayer`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.ConnectiveLayer)
      * [`ConnectiveLayer.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.ConnectiveLayer.animation_overrides)
      * [`ConnectiveLayer.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.ConnectiveLayer.make_forward_pass_animation)
    * [`NeuralNetworkLayer`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer)
      * [`NeuralNetworkLayer.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer.animation_overrides)
      * [`NeuralNetworkLayer.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer.construct_layer)
      * [`NeuralNetworkLayer.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.NeuralNetworkLayer.make_forward_pass_animation)
    * [`ThreeDLayer`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.ThreeDLayer)
    * [`VGroupNeuralNetworkLayer`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.VGroupNeuralNetworkLayer)
      * [`VGroupNeuralNetworkLayer.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.VGroupNeuralNetworkLayer.animation_overrides)
      * [`VGroupNeuralNetworkLayer.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.parent_layers.VGroupNeuralNetworkLayer.make_forward_pass_animation)
  * [manim_ml.neural_network.layers.triplet module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.triplet)
    * [`TripletLayer`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.triplet.TripletLayer)
      * [`TripletLayer.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.triplet.TripletLayer.animation_overrides)
      * [`TripletLayer.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.triplet.TripletLayer.construct_layer)
      * [`TripletLayer.from_paths()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.triplet.TripletLayer.from_paths)
      * [`TripletLayer.make_assets()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.triplet.TripletLayer.make_assets)
      * [`TripletLayer.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.triplet.TripletLayer.make_forward_pass_animation)
  * [manim_ml.neural_network.layers.triplet_to_feed_forward module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.triplet_to_feed_forward)
    * [`TripletToFeedForward`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.triplet_to_feed_forward.TripletToFeedForward)
      * [`TripletToFeedForward.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.triplet_to_feed_forward.TripletToFeedForward.animation_overrides)
      * [`TripletToFeedForward.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.triplet_to_feed_forward.TripletToFeedForward.construct_layer)
      * [`TripletToFeedForward.input_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.triplet_to_feed_forward.TripletToFeedForward.input_class)
      * [`TripletToFeedForward.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.triplet_to_feed_forward.TripletToFeedForward.make_forward_pass_animation)
      * [`TripletToFeedForward.output_class`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.triplet_to_feed_forward.TripletToFeedForward.output_class)
  * [manim_ml.neural_network.layers.util module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.util)
    * [`get_connective_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.util.get_connective_layer)
  * [manim_ml.neural_network.layers.vector module](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers.vector)
    * [`VectorLayer`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.vector.VectorLayer)
      * [`VectorLayer.animation_overrides`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.vector.VectorLayer.animation_overrides)
      * [`VectorLayer.construct_layer()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.vector.VectorLayer.construct_layer)
      * [`VectorLayer.make_forward_pass_animation()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.vector.VectorLayer.make_forward_pass_animation)
      * [`VectorLayer.make_vector()`](manim_ml.neural_network.layers.md#manim_ml.neural_network.layers.vector.VectorLayer.make_vector)
  * [Module contents](manim_ml.neural_network.layers.md#module-manim_ml.neural_network.layers)

## Submodules

## manim_ml.neural_network.neural_network module

Neural Network Manim Visualization

This module is responsible for generating a neural network visualization with
manim, specifically a fully connected neural network diagram.

### Example

# Specify how many nodes are in each node layer
layer_node_count = [5, 3, 5]
# Create the object with default style settings
NeuralNetwork(layer_node_count)

### *class* manim_ml.neural_network.neural_network.NeuralNetwork(input_layers, layer_spacing=0.2, animation_dot_color=ManimColor('#FF862F'), edge_width=2.5, dot_radius=0.03, title=' ', layout='linear', layout_direction='left_to_right', debug_mode=False)

Bases: `Group`

Neural Network Visualization Container Class

#### add_connection(start_mobject_or_name, end_mobject_or_name, connection_style='default', connection_position='bottom', arc_direction='down')

Add connection from start layer to end layer

#### animation_overrides *= {<class 'manim.animation.creation.Create'>: <function NeuralNetwork._create_override>}*

#### filter_layers(function)

Filters layers of the network given function

#### insert_layer(layer, insert_index)

Inserts a layer at the given index

#### make_forward_pass_animation(run_time=None, passing_flash=True, layer_args={}, per_layer_animations=False, \*\*kwargs)

Generates an animation for feed forward propagation

#### make_input_layers_dict(input_layers)

Make dictionary of input layers

#### remove_layer(layer)

Removes layer object if it exists

#### replace_layer(old_layer, new_layer)

Replaces given layer object

#### scale(scale_factor, \*\*kwargs)

Overriden scale

#### set_z_index(z_index_value: float, family=False)

Overriden set_z_index

## manim_ml.neural_network.neural_network_transformations module

## manim_ml.neural_network.variational_autoencoder module

## Module contents
