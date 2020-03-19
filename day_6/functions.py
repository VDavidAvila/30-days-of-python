items = [
    "Microphone", "Phone", 5502.22, "Camera",
    312.33, "Cliff Bars", 423.00, "Climbing Shoes", 132, "Laptop", "Rope", "Age"]

str_items = []
int_items = []

for item in items:
    if isinstance(item, int) or isinstance(item, float):
        int_items.append(item)
    elif isinstance(item, str):
        str_items.append(item)
    else:
        pass


#  str_items.sort(key=str.lower)  # order cad
str_items.sort(key=str.lower, reverse=True)  # order cad reverse
print(str_items)

#  order numbers
int_items.sort(reverse=True)
print(int_items)

#  To not modify the current list, use "sorted"
new_list = sorted(str_items, reverse=True)
print(new_list)

numbers = [13, 123, 333, 423, 2341]

total = sum(numbers)
average = total//len(numbers)  # rounded int
average_abs = total/(len(numbers)*1.0)  # float
average_abs_2 = sum(numbers)/float(len(numbers))

print("total => ", total)
print("average => ", average)
print("average_abs => ", average_abs)
print("average_abs_2 => ", average_abs_2)
