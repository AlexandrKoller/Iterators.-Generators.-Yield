import types


def flat_generator(list_of_list):
    stop_index = False
    while stop_index is False:
        stop_index = True
        for seq in list_of_list:
            if isinstance(seq, list) is True:
                stop_index = False
        value = list_of_list.pop(0)
        if isinstance(value, list) is True:
            list_of_list.extend(value)
        else:
            list_of_list.append(value)
    list_of_list.insert(0, list_of_list.pop())
    for i in list_of_list:
        yield i


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
