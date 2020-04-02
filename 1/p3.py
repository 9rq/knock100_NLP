s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = list(s.split())

ans = [len(word.strip(',').strip('.')) for word in words]
print(ans)
