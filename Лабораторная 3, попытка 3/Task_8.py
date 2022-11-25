money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while True:
    delta = spend - salary
    if delta > money_capital:
        break

    month += 1
    money_capital -= delta
    spend *= 1 + increase

print(month)  # 8
