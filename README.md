# flask_qrcode
Making QRCodes with Python3.7, Flask, qrcode  
  
QRコード : 株式会社デンソーウェーブ謹製  

  
  
モジュールインストール
---
\# pip3 install Flask  
\# pip3 install qrcode  
\# pip3 install pillow  
\# pip3 intalll flask\_wtf  
\# pip3 install mod\_wsgi  

---
  
  
  
Apache設定
---
LoadModule wsgi\_module /usr/local/lib/python3.7/site-packages/mod\_wsgi/server/mod\_wsgi-py37.cpython-37m-x86_64-linux-gnu.so   
WSGIScriptAlias /qrcode /var/www/qrcode/adapter.wsgi  
&lt;Directory "/var/www/qrcode/"&gt;  
  options Indexes FollowSymLinks ExecCGI  
&lt;/Directory&gt;

---
  
  
