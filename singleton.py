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




# shared states pattern
class SharedStatesCls:
    # shared states container created
    # for instances states sharing
    # in __dict__ of every instance
    __shared_states = {}
    def __init__(self):
        # how does it work: self(instance) accesses class attribute(__shared_states)
        # but instance attribute deny class access
        # self.__dict__ = self.__class__.__shared_states
        # self.__dict__ = self._SharedStatesCls__shared_states 
        self.__dict__ = self.__shared_states 

class Singleton_sharedStates(SharedStatesCls):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.initstate = 'shared_initstate' 
        self.args = args
        self.kwargs = kwargs

ci1 = Singleton_sharedStates()
# ci2 = Singleton_sharedStates(2, b='b')
ci2 = Singleton_sharedStates() 

ci2.dynamicattr1 = 'running'

print('vars(ci1): ', vars(ci1))
print('vars(ci2): ', vars(ci2))
#assert ci1 is ci2
#assert ci1 == ci2
