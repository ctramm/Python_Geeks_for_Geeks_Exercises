import base64


p = "45678@Test"
print(base64.b64encode(p.encode()))
e = base64.b64decode("NDU2NzhAVGVzdA==")
print(e.decode())
