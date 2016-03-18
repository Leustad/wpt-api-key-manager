This is a very simple API built upon http://bottlepy.org/docs/dev/index.html.

Getting started
```
pip install -r requirements.txt
python server.py
```

`GET /key-stats` returns all API keys and how many times they've been used.
`GET /use-key/<key>?count=#` records uses of an API key.  Count is optional, and defaults to 1.
'GET /find-key' returns an API with available uses.