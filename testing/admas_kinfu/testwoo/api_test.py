from woocommerce import API

wcapi = API(
    url="http://localhost:11002/",
    consumer_key="ck_f42ab89419a8669b1c8272005920479bf975ea5d",
    consumer_secret="cs_adb4dfb8117d1cc46f397990596c859641c15787",
    version="wc/v3"
)

r = wcapi.get("products")

import pprint
pprint.pprint(r.json())