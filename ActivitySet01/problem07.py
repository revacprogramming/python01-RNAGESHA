# Strings
text = "X-DSPAM-Confidence:    0.8475"
nag=text.find(':')
#print(nag)
gsd=text[nag+5:]
pavan=float(gsd)
print(gsd)
