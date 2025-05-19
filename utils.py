import base64
import os
import tenseal

PRIVATE_KEY_FILENAME = "private_key"


def write_data(data: bytes, filename: str):
    data = base64.b64encode(data)

    filepath = "files/" + filename
    with open(filepath, "wb") as file:
        file.write(data)


def read_data(filename: str) -> bytes:
    filepath = "files/" + filename
    with open(filepath, "rb") as file:
        data = file.read()

    return base64.b64decode(data)


def load_context():
    return tenseal.context_from(read_data(PRIVATE_KEY_FILENAME))


def main():
    private_key_filename = "private_key"
    public_key_filename = "public_key"

    if os.path.exists("files/" + private_key_filename) and os.path.exists("files/" + public_key_filename):
        print("Private and public keys already exist.")
    
    else:
        print("Generating keys...")

        context = tenseal.context(
            tenseal.SCHEME_TYPE.CKKS,
            poly_modulus_degree=16384,
            coeff_mod_bit_sizes=[60, 40, 40, 60]
        )

        context.generate_galois_keys()
        context.global_scale = 2**40
        
        secret_context = context.serialize(save_secret_key=True)
        write_data(secret_context, private_key_filename)
        
        context.make_context_public()
        public_context = context.serialize()
        write_data(public_context, public_key_filename)


if __name__ == "__main__":
    main()