emoji = 0
different = 0
emojies = ["❤️", "🧡", "💛", "💚", "💙", "🩵", "💜", "🩷", "🤎", "🖤", "🩶", "🤍"]
print("I love you generator")
print()
name = input("Nome a qui devi dedicare: ")
percentuale = input("Quanto dovra essere grande il numero massimo?: ")
emoji = input("Usare emoji? (si/no): ")
if emoji == "si":
  emoji = 1
  different = input("Emoji differenti? (si/no): ")
if emoji == "no":
  emoji = 0
if different == "si":
  different = 1
if different == "no":
  different = 0
print()
print("---------------------------")
print(name,"...")
for i in range(int(percentuale)):
  if emoji == 1 and different == 1:
    print("I love you",i+1,emojies[i%len(emojies)])
  elif emoji == 0:
    print("I love you", i+1, "%")
  elif emoji == 1 and different == 0:
    print("I love you", i+1, "%")
