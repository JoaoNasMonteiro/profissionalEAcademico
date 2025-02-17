


file = open('challengefile', mode  = 'rb')

data = file.read()

ba = bytearray(data)
ba.reverse()

#print(f"type = {type(data)}, data = {data}")

with open('reversed', 'wb') as out:
	out.write(ba)


file.close()
