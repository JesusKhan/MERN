import math

p = 3
q = 7
n = p*q
e = 2
phi = (p-1)*(q-1)

while (e < phi):
	if(math.gcd(e, phi) == 1):
		break
	else:
		e+=1

k = 2
d = (1 + (k*phi))/e

msg = 12.0
print("Message data = ", msg)

c = math.fmod(pow(msg, e), n)
print("Encrypted data = ", c)

m = math.fmod(pow(c, d), n)
print("Original Message Sent = ", m)
