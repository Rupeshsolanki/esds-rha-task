from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/key', methods=['GET','POST'])
def generate_RSA():
        if request.method == 'GET':
            from Crypto.PublicKey import RSA
            new_key = RSA.generate(2048)
            public_key = new_key.publickey().exportKey("PEM")
            private_key = new_key.exportKey("PEM")
            return  '{} {}'.format(private_key,public_key)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 
