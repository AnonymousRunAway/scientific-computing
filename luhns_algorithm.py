def luhn(query, verify=False):
    digits = [int(x) for x in str(query)]
    clip = -1 if verify else len(digits)
    check = 10 - (sum([x if i % 2 == 0 else x * 2 if x < 5 else (x * 2) % 10 + (x * 2) // 10 for i, x in enumerate(reversed(digits[:clip]))])) % 10
    return check == digits[-1] if verify else check

number = input("Enter a number: ")
print(luhn(number))