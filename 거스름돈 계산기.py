def calculate_change(payment, cost):
    change = payment - cost
    fifty_thounsand_count = int(change / 50000)
    print("50000원 지폐: %d장" % fifty_thounsand_count)

    change = change % 50000
    ten_thousand_count = int(change / 10000)
    print("10000원 지폐: %d장" % ten_thousand_count)

    change = change % 10000
    five_thousand_count = int(change / 5000)
    print("5000원 지폐: %d장" % five_thousand_count)

    change = change % 5000
    one_thousand_count = int(change / 1000)
    print("1000원 지폐: %d장" % one_thousand_count)

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

print()

print("="*20)

#2
def calculate_change(payment, cost):
    change = payment - cost
    fifty_thousand = change/50000
    ten_thousand = (change%50000) / 10000
    five_thousand = ((change%50000)%10000) / 5000
    one_thousand= (((change%50000)%10000) % 5000) / 1000

    print("50000원 지폐: %d장" % (fifty_thousand))
    print("10000원 지폐: %d장" % (ten_thousand))
    print("5000원 지폐: %d장" % (five_thousand))
    print("1000원 지폐: %d장" % (one_thousand))


calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

print()


print("="*20)


#3
def calculate_change(payment, cost):
    # 코드를 작성하세요.
    change = payment - cost

    fifty_thousand = change // 50000
    change -= fifty_thousand * 50000

    ten_thousand= change // 10000
    change -= ten_thousand * 10000

    five_thousand = change // 5000
    change -= five_thousand * 5000

    one_thousand = change // 1000

    print("50000원 지폐: %d장" % (fifty_thousand))
    print("10000원 지폐: %d장" % (ten_thousand))
    print("5000원 지폐: %d장" % (five_thousand))
    print("1000원 지폐: %d장" % (one_thousand))

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)