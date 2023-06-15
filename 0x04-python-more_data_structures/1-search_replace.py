#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None and search is not None and replace is not None:
        new_list = []
        for i in my_list:
            if i == search:
                i = replace
            new_list.append(i)

        return new_list
