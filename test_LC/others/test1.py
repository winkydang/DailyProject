from flask import Flask

app = Flask(__name__)


# @decorator
@app.route("/")
def view_func1():
    # dict
    return {"status": "success"}


if __name__ == '__main__':
    app.run()
