```javascript
              _   _   __ _ _               
  /\/\  _   _| |_| |_/ _\ (_) ___ ___ _ __ 
 /    \| | | | __| __\ \| | |/ __/ _ \ '__|
/ /\/\ \ |_| | |_| |__\ \ | | (_|  __/ |   
\/    \/\__,_|\__|\__\__/_|_|\___\___|_|   
                                           
```

# MuttSlicer
A list-like object that can apply child methods across a slice

```python
>>> from muttslicer import Slicer
>>> x = Slicer( FooClass, [FooClass(),FooClass(),...] )
>>> x[1:100].foo_instance_func()
```

### Example
Given this:

```python
class Base(object):
    def merge(self,update_dict):
        pass

class Foo(Base):
    def __init__(self,init_dict):
        self.data = init_dict

    def merge(self,update_dict):
        self.data.update(**update_dict)

class Bar(Base):
    def __init__(self,init_list):
        self.data = init_list

    def merge(self,update_dict):
        self.data = update_dict.keys()
```

Do stuff like this:
```python
>>> from muttslicer import Slicer
>>> x = Slicer( Base, [Foo({'a':1}),Bar(['b',2]),Foo({'c':3}),Bar(['d',4])] )
>>> new_slicer = x[2:4].merge({'x':100})
```

# Installation
0. Checkout the repsitory

0. Run `python setup.py develop`. Requires `setuptools` to be installed

0. Look at the tests

