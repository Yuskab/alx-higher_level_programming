#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)

=================================
2-uniq_add.py

#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i

    return (num)

=================================
3-common_elements.py

#!/usr/bin/python3
def common_elements(set_1, set_2):
    return (set_1 & set_2)

=================================
4-only_diff_elements.py

#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return (set_1 ^ set_2)

=================================
5-number_keys.py

#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        num += 1

    return (num)
