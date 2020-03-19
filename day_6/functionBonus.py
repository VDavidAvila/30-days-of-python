def my_sum_and_count(my_num_list):
    total, count = 0, 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
            count += 1
    return total, count


def my_avg(my_num_list):
    the_sum, num_of_items = my_sum_and_count(my_num_list)
    return the_sum / (num_of_items * 1.0)  # float


if __name__ == '__main__':
    items = [
        "Mic", "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 134
    ]
    print(my_avg(items))
