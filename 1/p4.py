s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
index = [1, 5, 6, 7, 8, 9, 15, 16, 19]

symbol = list(s.split())
symbol = {symbol[i][:1] if i+1 in index else symbol[i][:2] : i+1 for i in range(len(symbol))}
print(symbol)
