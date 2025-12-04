# Check file encoding and content
with open('data/expenses.csv', 'rb') as f:
    content = f.read()
    print("File content (bytes):")
    print(content)
    print("\nFile content (hex):")
    print(content.hex())
    
    # Try to decode as UTF-8
    try:
        text = content.decode('utf-8')
        print("\nDecoded as UTF-8:")
        print(repr(text))
    except UnicodeDecodeError as e:
        print(f"\nUTF-8 decode error: {e}")
        
    # Try to decode as latin-1
    try:
        text = content.decode('latin-1')
        print("\nDecoded as latin-1:")
        print(repr(text))
    except UnicodeDecodeError as e:
        print(f"\nLatin-1 decode error: {e}")