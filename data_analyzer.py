import tenseal
from utils import *

def main():
    context = load_context()

    male_salary_proto = read_data("encrypted_male_data")
    male_salary_encrypted = tenseal.lazy_ckks_vector_from(male_salary_proto)
    male_salary_encrypted.link_context(context)

    x = male_salary_encrypted.sum()
    print('Encrypted sum:', round(x.decrypt()[0], 2))
    
""" 
    # Serialize the encrypted vector to a file
    with open("encrypted_data", "wb") as file:
        file.write(enc.serialize())

    # Deserialize the encrypted vector from the file
    with open("encrypted_data", "rb") as file:
        enc_proto = file.read()

    # Create a lazy CKKS vector from the serialized data
    enc = tenseal.lazy_ckks_vector_from(enc_proto)
    enc.link_context(context)

    # Decrypt and print the result
    print('Decrypted:', enc.decrypt())
 """

if __name__ == "__main__":
    main()