def exchange():

    change = ((1, 160.86, 1.07, 0.87), (0.0062, 1, 0.0066, 0.0054), (0.94, 150.67, 1, 0,82), (1.15, 184.76, 1.23, 1))
    types = ('euro', 'yen', 'dollar', 'sterling pound')
    amount = float(input("Please enter an amount of money: "))

    while amount < 0:
        amount = float(input("Please enter a valid amount of money"))
    currency = input("Enter the currency: ")

    for i in range(len(types)):
        if types[i] == currency:
            to_change = float(input("Enter an amount to change: "))
            while to_change > amount:
                to_change = float(input(f"Please enter a valid amount to change. You have {amount} {currency}"))
            target_currency = input("Enter the target currency: ")
            for i in range(len(types)):
                if currency == types[0]:
                    if target_currency == types[0]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[0][0]} {target_currency}")
                        return result
                    elif target_currency == types[1]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[0][1]} {target_currency}")
                        return result
                    elif target_currency == types[2]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[0][2]} {target_currency}")
                        return result
                    elif target_currency == types[3]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[0][3]} {target_currency}")
                        return result
                elif currency == types[1]:
                    if target_currency == types[0]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[1][0]} {target_currency}")
                        return result
                    elif target_currency == types[1]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[1][1]} {target_currency}")
                        return result
                    elif target_currency == types[2]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[1][2]} {target_currency}")
                        return result
                    elif target_currency == types[3]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[1][3]} {target_currency}")
                        return result
                elif currency == types[2]:
                    if target_currency == types[0]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[2][0]} {target_currency}")
                        return result
                    elif target_currency == types[1]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[2][1]} {target_currency}")
                        return result
                    elif target_currency == types[2]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[2][2]} {target_currency}")
                        return result
                    elif target_currency == types[3]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[2][3]} {target_currency}")
                        return result
                elif currency == types[3]:
                    if target_currency == types[0]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[3][0]} {target_currency}")
                        return result
                    elif target_currency == types[1]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[3][1]} {target_currency}")
                        return result
                    elif target_currency == types[2]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[3][2]} {target_currency}")
                        return result
                    elif target_currency == types[3]:
                        result = (f"You changed {to_change} {currency} to {to_change * change[3][3]} {target_currency}")
                        return result
                    
print(exchange())