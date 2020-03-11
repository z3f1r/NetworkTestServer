# Generate priv & pub keys
openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem

# Review created cert
openssl x509 -text -noout -in certificate.pem

# Combine key and cert to pkcs12 bundle (pass: 123456)
openssl pkcs12 -inkey key.pem -in certificate.pem -export -out certificate.p12

# Validate pkcs12 file
`openssl pkcs12 -in certificate.p12 -noout -info

# Get hash for ssl pinning
```
➜  config$  openssl x509 -noout -fingerprint -sha256 -inform pem -in certificate.pem 
SHA256 Fingerprint=DC:C9:D2:3E:61:03:85:BB:84:0C:68:A2:51:E8:34:A0:CC:34:9B:DD:92:28:85:6F:A7:C0:2B:BA:1C:78:37:43
➜  config$  python
Python 2.7.16 (v2.7.16:413a49145e, Mar  2 2019, 14:32:10) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> "DC:C9:D2:3E:61:03:85:BB:84:0C:68:A2:51:E8:34:A0:CC:34:9B:DD:92:28:85:6F:A7:C0:2B:BA:1C:78:37:43".replace(':', '')
'DCC9D23E610385BB840C68A251E834A0CC349BDD9228856FA7C02BBA1C783743'
>>> from binascii import unhexlify
>>> from base64 import b64encode
>>> unhexlify('DCC9D23E610385BB840C68A251E834A0CC349BDD9228856FA7C02BBA1C783743')
'\xdc\xc9\xd2>a\x03\x85\xbb\x84\x0ch\xa2Q\xe84\xa0\xcc4\x9b\xdd\x92(\x85o\xa7\xc0+\xba\x1cx7C'
>>> b64encode(unhexlify('DCC9D23E610385BB840C68A251E834A0CC349BDD9228856FA7C02BBA1C783743'))
'3MnSPmEDhbuEDGiiUeg0oMw0m92SKIVvp8Aruhx4N0M='
>>> 

```