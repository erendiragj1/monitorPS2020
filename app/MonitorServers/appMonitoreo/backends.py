import hashlib
from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

class LoginBackend(BaseBackend):
    # MML se crea nuestro propio back-end de authenticacion, 
    # se redefinen los metodos predefinidos de Django
    def authenticate(self, request, username=None, password=None,  **kwargs):
        try:
            user = User.objects.get(username=username)
        except Exception:
            return None
        pwd_sin_mac_b64_binario = base64.b64decode(password[44:].encode('utf-8'))
        llave_aes_b64 = password[:44]
        llave_aes = base64.b64decode(llave_aes_b64.encode('utf-8'))
        mac = 'utKTZxUrAkf7liJeEhC3pw=='
        llave_mac = base64.b64decode(mac.encode('utf-8'))
        pwdBD = user.password
        pwd_descifrada = decifrar_mensaje(pwd_sin_mac_b64_binario, llave_aes, llave_mac)
        pwd_valida = check_password(pwd_descifrada.decode('utf-8'), pwdBD)
        if pwd_valida:
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(usr=user_id)
        except User.DoesNotExist:
            return print("NADA")


def decifrar_mensaje(mensaje_cifrado, llave, vector):
    # Fuinción que regresa el mensaje descifrado
    aesCipher = Cipher(algorithms.AES(llave),
                       modes.CTR(vector),
                       backend=default_backend())
    decifrador = aesCipher.decryptor()
    mensaje_decifrado = decifrador.update(mensaje_cifrado)
    mensaje_decifrado += decifrador.finalize()
    return mensaje_decifrado