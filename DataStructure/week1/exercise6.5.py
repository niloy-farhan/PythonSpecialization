text = "X-DSPM-Confidence: 0.8475"

colon_position = text.find(":")
print(colon_position)
piece = text[colon_position+2:]
print(piece)
value = float(piece)
print(value)
