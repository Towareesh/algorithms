from random import randint, choice
from string import ascii_uppercase as ascii_up
# from os import listdir


def generate_tracklist(tracklist=None, len_tracklist=500):
    ''' Create and write to file tracklist
        Return {track: random number of auditions}
    '''
    if tracklist == None:
        name_track = lambda :''.join([choice(ascii_up) for i in range(7)])
        tracklist = {name_track(): randint(1, 250) for i in range(len_tracklist)}

    with open('tracklist.txt', 'w', encoding='utf-8') as file:
        for line in tracklist:
            file.writelines(f'{line} {tracklist.get(line)}\n')  
    return tracklist


class Sort:
    ''' Return a new sorted collection
    '''
    def __init__(self, collection=None):
        self.collection = collection
        self.condition  = '<'

    def __repr__(self):
        try:
            args = ', '.join([f'{key}: {self.collection.get(key)}'for key in self.collection])
        except AttributeError:
            args = ', '.join([repr(x) for x in self.collection])
        return f'{type(self).__name__}({args})'

    def sort(self): # for simplification of call
        if isinstance(self.collection, list):
            return self._sortlist()
        if isinstance(self.collection, dict):
            return self._sortdict()

    def revers_sort(self):
        self.condition = '>'
        return self.sort()

    def _sortlist(self):
        newlist = []
        if type(self.collection) is list:
            for i in range(len(self.collection)):
                smallset = self.__find_list_small(self.collection)
                newlist.append(self.collection.pop(smallset))
        return newlist

    def _sortdict(self):
        newdict = {}
        if type(self.collection) is dict:
            for i in range(len(self.collection)):
                smallset = self.__find_dict_small(self.collection)
                newdict.update({smallset: self.collection.pop(smallset)})
            return newdict

    def __find_list_small(self, collection):
        now_item = collection[0]
        index = 0
        for now_index, val in enumerate(collection):
            if eval(f'val {self.condition} now_item'):
                now_item = val
                index = now_index
        return index

    def __find_dict_small(self, collection):
        key  = [i for i in collection][0]
        for now_key in collection.keys():
            if eval(f'now_key {self.condition} key'):
                key = now_key
        return key

class QuickSort(Sort):
    # def __init__(self):
    #     pass

    def quicksort(self, collection):
        if len(collection) <= 1:
            return collection
        support_elem = collection[0]
        left   = list(filter(lambda x: x < support_elem, collection))
        center = [i for i in collection if i == support_elem]
        right  = list(filter(lambda x: x > support_elem, collection))
        return self.quicksort(left) + center + self.quicksort(right)