# Copyright IRT Antoine de Saint Exupéry et Université Paul Sabatier Toulouse III - All
# rights reserved. DEEL is a research program operated by IVADO, IRT Saint Exupéry,
# CRIAQ and ANITI - https://www.deel.ai/
# =====================================================================================

from os import path

with open(path.join(path.dirname(__file__), "VERSION")) as f:
    __version__ = f.read().strip()

from . import activations
from . import callbacks
from . import constraints
from . import initializers
from . import layers
from . import losses
from . import metrics
from .model import Sequential, Model, vanillaModel
from . import normalizers
from . import regularizers
from . import utils
