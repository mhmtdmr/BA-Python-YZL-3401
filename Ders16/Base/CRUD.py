from abc import *
class CRUD:
    def __init__(self) -> None:
        pass

    @abstractstaticmethod
    def Create(obj):
        pass

    @abstractstaticmethod
    def Read(obj):
        pass

    @abstractstaticmethod
    def Update(obj):
        pass

    @abstractstaticmethod
    def Delete(obj):
        pass


