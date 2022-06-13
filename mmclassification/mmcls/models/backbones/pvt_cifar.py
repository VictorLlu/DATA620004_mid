import torch
from ..builder import BACKBONES
from mmdet.models import PyramidVisionTransformer

@BACKBONES.register_module()
class PyramidVisionTransformerCifar(PyramidVisionTransformer):
    def __init__(self, **args):
        super().__init__(**args)