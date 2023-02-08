import pyzipper


def try_extract(subset: list, path_from: str, path_to: str) -> None:
    possible_password: str = ''.join(subset)

    try:
        with pyzipper.AESZipFile(path_from, 'r', compression=pyzipper.ZIP_DEFLATED,
                                 encryption=pyzipper.WZ_AES) as extracted_zip:
            extracted_zip.extractall(path=path_to, pwd=str.encode(possible_password))
        print('Success', subset)

        with open('password.txt', 'wr') as f:
            f.write(possible_password)

    except Exception as e:
        print(e, '\n')
