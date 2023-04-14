print("Hello, World!")
client = SecretClient(vault_url=vault_url, credential=credential)
password = "test"
username = client.get_secret("apikey")
password = client.get_secret("apisecret")
