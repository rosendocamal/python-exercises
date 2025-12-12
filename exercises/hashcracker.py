import hashlib

target_hash = "5040c11cf85edf87fc5b0812a2ad7a27df4ad12f9e899b94221fb4d9c8ddbca9"


wordlist = "projects\hash_cracker\wordlist.txt"

with open(wordlist, 'r', encoding="utf-8", errors='ignore') as file:
    password_dictionary = [line.strip() for line in file]

    for password in password_dictionary:
        calculated_hash = hashlib.sha256(password.encode()).hexdigest()
        if calculated_hash == target_hash:
            print(f"La contraseña original es: {password}")
            break
        else:
            print("La contraseña no se encuentra en el diccionario")