"""
 -------------------
| h | e | l | l | o |
 -------------------
1   2   3   4   5  6 position of list python
-6 -5  -4  -3  -2 -1 position of list reverse
"""
my_list = [item for item in "hello"]
print(my_list[-3:3])



def day(items=[]):
    if len(items) > 0:
        print(items.__class__)
        print(items[-2].__class__)

        str_items = []  # list str empty
        num_items = []  # list num empty

        for item in items:
            if isinstance(item, float) or isinstance(item, int):
                num_items.append(item)
            elif isinstance(item, str):
                str_items.append(item)
            else:
                pass

        print("str_items_list ==> ", str_items)
        print("num_items_list ==> ", num_items)
    else:
        print("method day() empty")


if __name__ == '__main__':
    # list of think
    items = ["Mic", "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 134]
    # call method day(list:None)
    day()
    day(items)
