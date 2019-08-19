import urllib.request

def test_localhost_loads():
    urlOpened = urllib.request.urlopen("http://localhost:5000/")
    assert urlOpened