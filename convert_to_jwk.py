from jwcrypto import jwk

# Load existing PEM
with open("lti_keys/public.pem", "rb") as f:
    key = jwk.JWK.from_pem(f.read())

# Export as JWK (public only)
jwk_public = key.export_public()

print(jwk_public)
