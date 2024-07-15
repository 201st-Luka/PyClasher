"""
``Replay`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class Replay(Model):
    replay_data: dict
    replay_tag: str
