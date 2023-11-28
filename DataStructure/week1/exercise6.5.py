text = "X-DSPM-Confidence:      0.8475"

colon_position = text.find(":")

numeric_part = text[colon_position + 1:].strip()

confidence_value = float(numeric_part)

print(confidence_value)