import base64

# The original string
original_string = "Hello$World"

# Convert the string to bytes, as Base64 works with binary data
bytes_to_encode = original_string.encode('utf-8')

# Encode the bytes into Base64
base64_bytes = base64.b64encode(bytes_to_encode)

# Convert the Base64 bytes back to a string for display
base64_string = base64_bytes.decode('utf-8')

print(f"Original String: {original_string}")
print(f"Base64 Encoded: {base64_string}")