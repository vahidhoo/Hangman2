coin = int(input())

remain_coin = coin

if remain_coin >= 6769:
    result = remain_coin // 6769
    print(str(result) + ' sheep')
elif remain_coin >= 3848:
    result = remain_coin // 3848
    print(str(result) + " cows" if result > 1 else ' 1 cow')
elif remain_coin >= 1296:
    result = remain_coin // 1296
    print(str(result) + " pigs" if result > 1 else ' 1 pig')
elif remain_coin >= 678:
    result = remain_coin // 678
    print(str(result) + " goats" if result > 1 else ' 1 goat')
elif remain_coin >= 23:
    result = remain_coin // 23
    print(str(result) + " chickens" if result > 1 else ' 1 chicken')
else:
    print('None')
