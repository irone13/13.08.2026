words = ["HELLO", "WORLD", "PYTHON", "CODE", "DEVELOPER", "AI"]

#1
print("All upercase : ",all(w.isupper() for w in words))

#2
print("Has a long word : ",any(len(w) > 5 for w in words))

#3
print(sorted(words, key=len))
