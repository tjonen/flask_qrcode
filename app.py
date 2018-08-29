from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import hashlib
import qrcode
import qrdist

app = Flask(__name__)
app.config['DEBUG'] = False
app.secret_key = 'this is secret'
app.register_blueprint(qrdist.app)
csrf = CSRFProtect(app)

@app.route("/")
@app.route("/make_qrcode", methods = ['POST'])
def make_qrcode():
    if (request.method == 'POST'):
        qr_value = request.form['qr_value']
        if (qr_value != ""):
            # 値のMD5値をファイル名とする。
            qr_path = hashlib.md5(qr_value.encode('utf-8')).hexdigest() + ".png"
            # セルサイズ。デフォルトは10。
            qr = qrcode.QRCode(box_size=4)
            qr.add_data(qr_value)
            qr.make()
            img = qr.make_image()
            # QRコードの保存
            img.save('/var/www/qrcode/qrdist/' + qr_path)

            return render_template('make_qrcode.html', qr_path=qr_path, qr_value=qr_value)

    return render_template('make_qrcode.html')


if __name__ == "__main__":
    app.run(host="src.kd2.jp", port=80)
