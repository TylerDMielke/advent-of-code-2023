import std/httpclient

var client = newHttpClient()

try
    echo client.getContent("http://google.com")
finally:
    client.close()