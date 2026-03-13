from pycipher import Caesar, Vigenere, Rot13

from pycipher import Caesar, Vigenere, Rot13

encrypt_caesar = lambda key, text: Caesar(key).encipher(text)
encrypt_vigenere = lambda password, text: Vigenere(password).encipher(text)
encrypt_rot13 = lambda text: Rot13().encipher(text)

decrypt_caesar = lambda key, cypher: Caesar(key).decipher(cypher)
decrypt_vigenere = lambda password, cypher: Vigenere(password).decipher(cypher)
decrypt_rot13 = lambda cypher: Rot13().decipher(cypher)


test_data = "ILOVEBUBLAS"

c_key = 3

c_enc = encrypt_caesar(c_key, test_data)
c_dec = decrypt_caesar(c_key, c_enc)
print(f"Caesar: {test_data} -> {c_enc} -> {c_dec}")

v_key = "KLIC"

v_enc = encrypt_vigenere(v_key, test_data)
v_dec = decrypt_vigenere(v_key, v_enc)
print(f"Vigenere: {test_data} -> {v_enc} -> {v_dec}")

r_enc = encrypt_rot13(test_data)
r_dec = decrypt_rot13(r_enc)
print(f"Rot13: {test_data} -> {r_enc} -> {r_dec}")