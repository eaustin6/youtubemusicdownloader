from ytmusicapi import YTMusic

ytmusic = YTMusic('headers_auth.json')
search = input("insira oq tu quer\n")
result = ytmusic.search(search, filter = 'albums')
print("escolha um resultado:\n")
print("1:")
print("nome do album: " + result[0]["title"])
print("nome do artista: " + result[0]["artists"][0]["name"])
print("\n2:")
print("nome do album: " + result[1]["title"])
print("nome do artista: " + result[1]["artists"][0]["name"])
print("\n3:")
print("nome do album: " + result[2]["title"])
print("nome do artista: " + result[2]["artists"][0]["name"])
