from .transformData import TransformData


class TransformContext:
    def __init__(self, strategy: TransformData):
        self._strategy = strategy

    @property
    def strategy(self) -> TransformData:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: TransformData):
        self._strategy = strategy

    def execute(self, data: dict()):
        return self._strategy.convertDict(data)
