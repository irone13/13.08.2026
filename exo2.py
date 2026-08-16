battery: list[int] = [78, 92, 45, 61, 88, 30]

#1
print("All above 20: ",all(b > 20 for b in battery))


#2
print("Any below 40:",any(b < 40 for b in battery))

#3
print("All full :",all(b == 100 for b in battery))

#4
ordered = sorted(battery)
print("ordered:", ordered)
print("Original: ", battery)

#5
battery.sort(reverse=True)
print("Sorted desc: ", battery)

#6
print("Top three: ",battery[:3])