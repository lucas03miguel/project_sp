import tenseal

def encrypt(dataset, filename):

    pass

    
def decrypt():
    pass


if __name__ == "__main__":
    # Test the encrypt and decrypt functions
    test_string = ["Hello, World!"]
    encrypted_string = encrypt(test_string, "values_encrypted.txt")
    decrypted_string = decrypt(encrypted_string)
    
    assert test_string == decrypted_string, "Test failed!"
    print("Test passed!")