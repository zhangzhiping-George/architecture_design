'''
singleton pattern and shared status pattern
'''

# class Level Singleton pattern
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

def test_single(cls):
    return cls() == cls()

s1 = Singleton()
s2 = Singleton()
assert s1 == s2

class SingletonA(Singleton):
    pass

assert test_single(SingletonA) is True


# metaclass Level Singleton implement
class MetaSingleton(type):
    def __init__(cls, *args, **kwargs):
        print(cls, 'init called with', *args, **kwargs)
        type.__init__(cls, *args, **kwargs)
        cls.instance = None
   
    # class(metacalss instance) initiation will call metaclass via this
    def __call__(cls, *args, **kwargs): 
        print(cls, 'creating class(metaclass instance) ', *args, **kwargs)
        if not cls.instance: 
            return cls.instance


class Singleton_meta(metaclass=MetaSingleton):
    pass

sm = Singleton_meta()

print('===assert test_single(Singleton_meta) is True===')
assert test_single(Singleton_meta) is True




# shared status pattern
class SharedObjstatus:
    _status = {}
    def __init__(self,  *args, **kwargs):
        self.__class__.__dict__ = _status
        self.args = args
        self.kwargs = kwargs
