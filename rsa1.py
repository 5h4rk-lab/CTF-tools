from Crypto.Util.number import inverse
n = int(input("enter value of n: "))
p = int(input("enter value of p: "))
q = int(input("enter value of q: "))
e = int(input("enter value of e: "))
c = int(input("enter cipher text: "))


phi = (p-1)*(q-1)
d = inverse(e,phi)
m = pow(c,d,n)
print hex(m)[2:-1].decode('hex')
