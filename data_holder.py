import tenseal
import pandas as pd
from utils import *


def encrypt(dataset, filename):
    context = load_context()
    encrypted_data = tenseal.ckks_vector(context, dataset)
    write_data(encrypted_data.serialize(), filename)


def decrypt(filename):
    context = load_context()
    enc_proto = read_data(filename)
    enc = tenseal.lazy_ckks_vector_from(enc_proto)
    enc.link_context(context)
    
    print('Decrypted:', enc.decrypt())


def excel_to_salary_lists(filename):
    df = pd.read_excel(filename)

    male   = df.loc[df['Gender'] == 'M', 'Base Salary/Year ($)'].astype(float).tolist()
    female = df.loc[df['Gender'] == 'F', 'Base Salary/Year ($)'].astype(float).tolist()

    return male, female


if __name__ == "__main__":
    male, female = excel_to_salary_lists("dataset.xlsx")

    encrypt(male, "encrypted_male_data")
    encrypt(female, "encrypted_female_data")

    decrypt("calculations")
    #decrypt("encrypted_female_data")

    #dataset = excel_to_salary_lists("dataset.xlsx")
    #print(dataset)
    #encrypt(dataset, "encrypted_data")

    #decrypt("encrypted_data")