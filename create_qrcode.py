import pyqrcode
from pyqrcode import QRCode
s = "https://www.youtube.com/watch?v=QXeEoD0pB3E&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"
url = pyqrcode.create(s)
url.svg("qr.svg",scale=8)