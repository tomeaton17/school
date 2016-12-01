def maya(i):
    firstQuotient = i // 10
    firstRemainder = i % 10
    secondQuotient = firstQuotient // 10
    secondRemainder = firstQuotient % 10
    final = secondQuotient * 10
    final += firstRemainder
    final = final * 10
    final = final + secondRemainder
    return final

print(123456, maya(123456))