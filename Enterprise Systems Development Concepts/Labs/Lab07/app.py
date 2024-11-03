from flask import Flask, jsonify, redirect, url_for
from flask_dance.contrib.github import github
from oauth import github_blueprint

app = Flask(__name__)
app.secret_key = "bSe/QVjSQ2kctmlG22ZJI1vFQlbUkE1mkI871Vs0k1I="
app.register_blueprint(github_blueprint, url_prefix="/login")


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/test")
def test():
    return jsonify({"message": "Hello, World!"})


@app.route("/login")
def login():
    if not github.authorized:
        return redirect(url_for("github.login"))
    response = github.get("/user")
    return jsonify(response.json())


if __name__ == "__main__":
    from OpenSSL import SSL

    context = SSL.Context(SSL.SSLv23_METHOD)
    context.use_privatekey_file("localhost.key")
    context.use_certificate_file("localhost.crt")

    app.run(
        debug=True,
        host="localhost",
        port=5000,
        # ssl_context=context,
    )
