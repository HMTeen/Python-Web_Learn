from flask import Flask,render_template
app = Flask(__name__)

@app.route('/test')
def index():
    return render_template('./html_file.html')

@app.route('/get_news')
def get_news():
    return '自建网站'

if __name__ == '__main__':
    app.run()


