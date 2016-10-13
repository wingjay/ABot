import os

from flask import Flask
from flask import request


# Flask app should start in global layout
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hi, Here is wingjay ABot'
    

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')