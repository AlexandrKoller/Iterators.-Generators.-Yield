class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        stop_index = False
        while stop_index is False:
            stop_index = True
            for seq in self.list_of_list:
                if isinstance(seq, list) is True:
                    stop_index = False
            self.value = self.list_of_list.pop(0)
            if isinstance(self.value, list) is True:
                self.list_of_list.extend(self.value)
            else:
                self.list_of_list.append(self.value)
        self.list_of_list.insert(0, self.list_of_list.pop())
        self.max_index = len(self.list_of_list)
        self.min_index = 0
        return self

    def __next__(self):
        if self.max_index > self.min_index:
            item = self.list_of_list[self.min_index]
            self.min_index += 1
        else:
            raise StopIteration
        return item


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()