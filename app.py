from flask import Flask


app = Flask('py-less')


@app.route("/")
def main():
    return "Alive!"


if __name__ == "__main__":
	app.run()
