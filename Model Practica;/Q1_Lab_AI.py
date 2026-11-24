temp = float(input("Enter temperature: "))

if temp <= 20:
    cold = 1
    warm = 0
    hot = 0
elif temp <= 25:
    cold = (25 - temp) / 5
    warm = (temp - 20) / 5
    hot = 0
elif temp <= 30:
    cold = 0
    warm = (30 - temp) / 5
    hot = (temp - 25) / 5
else:
    cold = 0
    warm = 0
    hot = 1

fan_speed = (cold * 20 + warm * 50 + hot * 100) / (cold + warm + hot)

print("Cold Membership:", round(cold, 2))
print("Warm Membership:", round(warm, 2))
print("Hot Membership:", round(hot, 2))
print("Fan Speed:", round(fan_speed, 2), "%")
