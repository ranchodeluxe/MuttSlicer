
class Base(object):

    def combine(self,update_dict):
        raise NotImplemented('you must implement combine')

    def flatten(self):
        raise NotImplemented('you must implement flatten')

    def merge(self,update_dict):
        raise NotImplemented('you must implement merges')

class Foo(Base):

    def __init__(self,data_dict):
        self.data_dict = data_dict

    def __str__(self):
        return "{}{}".format(
            type(self).__name__,
            self.data_dict
        )

    def __repr__(self):
        return "{}{}".format(
            type(self).__name__,
            self.data_dict
        )

    def combine(self,update_dict):
        self.data_dict['combine'] = list(zip(self.data_dict.keys(),update_dict.values()))  # python3 compatibility

    def flatten(self):
        self.data_dict['flatten'] = self.data_dict.items()

    def merge(self,update_dict):
        self.data_dict.update(**update_dict)

class Bar(Base):

    def __init__(self,data_list):
        self.data_list = data_list

    def __str__(self):
        return "{}{}".format(
            type(self).__name__,
            self.data_list
        )

    def __repr__(self):
        return "{}{}".format(
            type(self).__name__,
            self.data_list
        )

    def combine(self,update_dict):
        self.data_list.append(
            list(zip(self.data_list,update_dict.keys())) # python3 compatibility
        )

    def flatten(self):
        pass

    def merge(self,update_dict):
        self.data_list.extend(update_dict.keys())
        self.data_list.extend(update_dict.values())
