def change(money):
    # write your code here  
    num_coins = 0

    while money > 0:
        if money >= 10:
            money -= 10
            num_coins += 1
        elif money >= 5:
            money -= 5
            num_coins += 1
        else:
            num_coins += money
            money = 0 

    return num_coins


if __name__ == '__main__':
    m = int(input())
    print(change(m))
