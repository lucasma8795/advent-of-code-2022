def parse_snafu(s):
	out = 0
	for char in s:
		out *= 5
		if char.isdigit(): out += int(char)
		elif char == "-": out -= 1
		elif char == "=": out -= 2
	return out

total = 0
with open("./data.txt", "r") as fo:
	for line in fo.readlines():
		total += parse_snafu(line.strip())

ans = ""
while total != 0:
	rem = total % 5
	if rem == 0 or rem == 1 or rem == 2:
		total -= rem
		ans += str(rem)
	elif rem == 3:
		total += 2
		ans += str("=")
	elif rem == 4:
		total += 1
		ans += str("-")
	total //= 5
ans = ans[::-1]
print(ans)