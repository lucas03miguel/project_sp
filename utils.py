import base64

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