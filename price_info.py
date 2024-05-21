
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


def total_cost_shopping():
    total_cost = 0
    for key in price_list.keys():
        if key in quantity_list: #if fruit in price_list also appear in quantity_list
            # complete the implementation below:
            times_list = quantity_list[key]*price_list[key]
            #print(times_list)
            total_cost = total_cost + times_list
            print("cost of" + key + " =", total_cost)

    print("total cost = ", total_cost)
    return total_cost


def cost_of_fruits(fruit, quantity):
    for key in price_list.keys():
        if key == fruit:
            cost = quantity*price_list[key]
            break

    print("cost of ", quantity, fruit, "=", cost)
    return cost


def main():

    fcost = cost_of_fruits('apple', 10)
    tcost = total_cost_shopping()


if __name__ == "__main__":
    main()