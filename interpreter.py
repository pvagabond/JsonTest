import json

file = "D:/DataVault/orderHistory.txt"
file_obj = open(file)
json_obj = json.load(file_obj)
items = json_obj['items']
# items = filter(lambda x: x['orderId'] == "0002ead5-a0ae-406b-bf1b-63e6debba597", items)
items.sort(key=lambda x: x['createdTime'])
for item in items:
    if len(item['orderLineItems']) > 1:
        raise ValueError("There are more than one line items")
    timeStamp = item['createdTime']
    lineItem = item['orderLineItems'][0]
    billState = lineItem['billingState']
    orderState = item['orderState']
    print("{}: the billing state is {} while the order state is {}".format(timeStamp, billState, orderState))


def exp(x, precision):
    constant = 1
    numerator, denominator, step = x, 1, 1
    total = constant + numerator / denominator
    for _ in range(precision):
        step += 1
        denominator = denominator * step
        numerator = numerator * x
        total += numerator / denominator
    return total


