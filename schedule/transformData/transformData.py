from abc import ABC, abstractmethod

class TransformData(ABC):
    @abstractmethod
    def convertDict(self,data: dict()):
        pass