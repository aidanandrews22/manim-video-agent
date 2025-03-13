from importlib.metadata import version

from .constants import MArrayStyle, MGraphStyle, MStackStyle
from .m_collection.m_array import MArray
from .m_collection.m_stack import MStack
from .m_graph.m_graph import MGraph

__version__ = version(__name__)

__all__ = ["MArray", "MStack", "MGraph", "MArrayStyle", "MStackStyle", "MGraphStyle"]
