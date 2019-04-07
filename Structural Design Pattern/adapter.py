class Korean:
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "Anyeong"

class British:
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello"

class Adapter:
    """ Changes the generic method name to inidividualized method name """
    def __init__(self, object, **adapted_method):
        self._object = object

        self.__dict__.update(adapted_method)

    def __getattr__(self,attr):
        return getattr(self._object, attr)

objects = []

korean = Korean()
british = British()

objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says {}\n".format(obj.name, obj.speak()))