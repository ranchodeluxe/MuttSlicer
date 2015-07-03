import inspect
import collections

class Slicer(collections.MutableSequence):

    def __init__(self, class_type, init_list):
        self.class_type = class_type
        self.items = []
        for item in init_list:
            self.append(item)
        self._rebind_and_wrap()

    def __str__(self):
        return "{} {}".format(type(self).__name__,self.items)

    def __repr__(self):
        return "{} {}".format(type(self).__name__,self.items)

    def _assert_type(self, item):
        if not isinstance(item, self.class_type):
            raise TypeError(
                'collection items must be subclasses of "{}"'.format(self.class_type)
            )

    def __len__(self):
        return len(self.items)

    def __getitem__(self, indx):
        return self.items[indx]

    def __delitem__(self, indx):
        del self.items[indx]

    def __setitem__(self, indx, item):
        self._assert_type(item)
        self.items[indx] = item

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.items == other.items

    def __ne__(self, other):
        return not self.__eq__(other)

    def insert(self, indx, item):
        self._assert_type(item)
        self.items.insert(indx, item)

    def append(self, item):
        self._assert_type(item)
        self.items.append(item)

    def __getitem__(self, key):
        if isinstance(key, slice):
            #
            #  in certain cases, like when __getslice__
            #  forwards calls to __getitem__
            #  the default key.stop value might be large
            #
            if key.stop > len(self.items):
                key = slice(key.start,len(self.items),key.step)
            #
            #  handles slices with start, stop, step
            #
            return self.__class__(
                self.class_type,
                self.items[key.start:key.stop:key.step]
            )
        #
        #  handles single index lookups
        #
        return self.__class__(
            self.class_type,
            [self.items[key],]
        )

    def __getslice__(self, start, stop):
        return self.__getitem__(slice(start,stop,1))


    def _rebind_and_wrap(self):
        for name, func in inspect.getmembers( self.class_type ):
            if not inspect.ismethod( func ):
                continue

            if name.startswith( '__' ) or name.endswith( '__' ):
                continue

            #
            #  rebind the func.__name__ to Slicer instance
            #  and dynamically decorate the original function
            #  so we can handle different calling signatures
            #  when the func is invoked on Slicer
            #
            setattr( self, name, self._create_wrapper(func.im_func) )

    def _create_wrapper(self,func):
        def decorate(*args,**kwargs):
            for item in self.items:
                getattr(item,func.__name__)(*args,**kwargs)
            return self
        return decorate
