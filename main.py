from http.server import BaseHTTPRequestHandler
import json
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            eth = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
            eth_price = eth.json()['ethereum']['usd']
            burna_price = round(eth_price * 0.0000075, 5)
            result = {
                "eth_price": eth_price,
                "burna_price": burna_price
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({ "error": str(e) }).encode())
