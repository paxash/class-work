str = 'X-DSPAM-Confidence: 0.8475'
start = str.find(':')
num = float(str[start+1:])
print(num)
