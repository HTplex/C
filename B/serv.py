from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	print dir(request)
	s="   id1="+request.args.get('id1')+" id2="+request.args.get('id2')
	return s


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80,debug=True)