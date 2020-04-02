import random as rand
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = list(s.split())
ans = [word[0]+ ''.join(rand.sample(word[1:-1], len(word)-2)) +word[-1] if len(word)>4 else word for word in words]
print(*ans)
