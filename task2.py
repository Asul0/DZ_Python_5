def sumnumbers(a, b):
   if b == 0:
      return a
   else: return 1 + sumnumbers(a, b - 1)

print(sumnumbers(3, 5))