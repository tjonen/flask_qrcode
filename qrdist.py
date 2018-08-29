from flask import Blueprint

# QRコード保存用に新しい静的ディレクトリを追加する。
app = Blueprint('qrdist', __name__, static_url_path='/qrdist', static_folder='./qrdist')
