prices: list[int] = [120, 45, 300, 89, 210, 15, 74]
double = [n * 2 for n in prices]
print ("Doubled : ", double)
expensive = [p for p in prices if p > 100]
print ("Expensive : ", expensive)
on_sale = [p-50 for p in expensive]
print   ("On sale : ",on_sale)
labels = ['pricey' if p > 100 else 'cheap' for p in prices]

print("Labels : ",labels)
as_text = [f"{p} NIS" for p in prices]
print("As text : ",as_text)
