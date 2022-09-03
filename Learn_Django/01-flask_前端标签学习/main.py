from flask import Flask,render_template
app = Flask(__name__)

@app.route('/test')
def index():
    return render_template('./html_file.html')

@app.route('/news')
def get_news():
    return '网站跳转'

if __name__ == '__main__':
    app.run()


