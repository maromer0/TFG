phrase = input("Introduce a phrase: ")
word = input("Introduce a word: ")
count = 0
for i in phrase:
    if word == i:
    	count += 1
print(count)