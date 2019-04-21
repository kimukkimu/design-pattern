from Iterator import Iterator
from abc import ABCMeta, abstractmethod

# 抽象クラス
class Aggregate(metaclass=ABCMeta):

    @abstractmethod
    def iterator(self) -> Iterator:
        raise NotImplementedError