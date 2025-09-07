import numpy as np

def generate_1d_keys(q):
    A = np.random.randint(0, q)
    s = np.random.randint(0, q)
    return A, s

def encrypt_bit(A, s, message_bit, q):
    e = np.random.randint(-1, 2)
    ciphertext = (A * s + e + message_bit * (q // 2)) % q
    return ciphertext

def decrypt_bit(s, A, ciphertext, q):
    decryption_value = (ciphertext - (A * s)) % q
    decryption_value = (decryption_value + q) % q
    if decryption_value < q / 4 or decryption_value > 3 * q / 4:
        return 0
    else:
        return 1

if _name_ == "_main_":
    q = 101
    
    A, s = generate_1d_keys(q)
    print("1D Keys generated successfully. 🔑")
    print(f"Public Key (A): {A}")
    print(f"Private Key (s): {s}")
    
    while True:
        binary_string = input("\nEnter the binary number to encrypt (e.g., '1011'): ")
        if all(c in '01' for c in binary_string) and len(binary_string) > 0:
            break
        else:
            print("Invalid input. Please enter a string of only '0's and '1's.")

    encrypted_list = []
    print("\nEncrypting...")
    for bit_char in binary_string:
        message_bit = int(bit_char)
        ciphertext = encrypt_bit(A, s, message_bit, q)
        encrypted_list.append(ciphertext)
        print(f"  - Encrypted bit '{message_bit}': {ciphertext}")

    print(f"\nFull ciphertext: {encrypted_list}")

    decrypted_string = ""
    print("\nDecrypting...")
    for ciphertext in encrypted_list:
        decrypted_bit = decrypt_bit(s, A, ciphertext, q)
        decrypted_string += str(decrypted_bit)
        print(f"  - Decrypted ciphertext '{ciphertext}': {decrypted_bit}")

    print(f"\nOriginal binary number: {binary_string}")
    print(f"Decrypted binary number: {decrypted_string}")
    
    if binary_string == decrypted_string:
        print("\nSuccess: The decrypted binary number matches the original. ✅")
    else:
        print("\nFailure: The decryption failed. ❌")
