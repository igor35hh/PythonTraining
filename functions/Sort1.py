
#items = ["Microphone",  "Phone", 5502.22, "Camera", 312.33, "Cliff Bars", 423.00, "Climbing Shoes", 132, "Laptop", "Rope"]

str_items = []

int_items = []

str_items.sort(key=str.lower)

print(str_items)

str_items.sort(key=str.lower, reverse=True)

print(str_items)

new_list = sorted(str_items, reverse=True)

numbers = [13, 123, 333, 423, 2341]

total = sum(numbers)
average = total/len(numbers)
average_abs = total/(len(numbers) * 1.0)
average_abs_2 = sum(numbers)/float(len(numbers))



