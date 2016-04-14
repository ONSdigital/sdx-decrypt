from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, PublicFormat, BestAvailableEncryption
import os

f4 = 65537

os.environ['EQ_PUBLIC_KEY'] = './jwt-test-keys/sr-public.pem'
os.environ['EQ_PRIVATE_KEY'] = './jwt-test-keys/sr-private.pem'

os.environ['PUBLIC_KEY'] = './jwt-test-keys/sdx-public.pem'
os.environ['PRIVATE_KEY'] = './jwt-test-keys/sdx-private.pem'
os.environ['PRIVATE_KEY_PASSWORD'] = "digitaleq"

backend = default_backend()

eq_private_key = rsa.generate_private_key(
   public_exponent=f4,
   key_size=3072,
   backend=default_backend()
)

eq_private_bytes = eq_private_key.private_bytes(
    encoding=Encoding.PEM,
    format=PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=BestAvailableEncryption(b'digitaleq')
)

eq_public_key = eq_private_key.public_key().public_bytes(
    encoding=Encoding.PEM,
    format=PublicFormat.SubjectPublicKeyInfo
)

if not os.path.exists('./jwt-test-keys'):
    os.mkdir('./jwt-test-keys')

f = open('./jwt-test-keys/sr-public.pem', 'w')
f.write(eq_public_key.decode('UTF8'))
f.close()

f = open('./jwt-test-keys/sr-private.pem', 'w')
f.write(eq_private_bytes.decode('UTF8'))
f.close()

sde_private_key = rsa.generate_private_key(
   public_exponent=f4,
   key_size=3072,
   backend=default_backend()
)

sde_private_bytes = sde_private_key.private_bytes(
    encoding=Encoding.PEM,
    format=PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=BestAvailableEncryption(b'digitaleq')
)

sde_public_key = sde_private_key.public_key().public_bytes(
    encoding=Encoding.PEM,
    format=PublicFormat.SubjectPublicKeyInfo
)

f = open('./jwt-test-keys/sdx-public.pem', 'w')
f.write(sde_public_key.decode('UTF8'))
f.close()

f = open('./jwt-test-keys/sdx-private.pem', 'w')
f.write(sde_private_bytes.decode('UTF8'))
f.close()