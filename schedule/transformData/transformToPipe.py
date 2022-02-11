from .transformData import TransformData
from functools import reduce


class TransformToPipe(TransformData):
    def convertDict(self, data: dict()):
        dataTransformed = reduce(
            lambda a, b: f'{a}{b[0]}: {b[1]} |',  list(data.items()), '')
        return dataTransformed
