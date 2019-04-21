from abc import ABCMeta, abstractmethod

# 抽象クラス
class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def hasNext(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def next(self) -> object:
        raise NotImplementedError