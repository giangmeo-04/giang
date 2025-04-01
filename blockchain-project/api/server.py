from flask import Flask
from api.routes import setup_routes

def start_server(blockchain):
    app = Flask(__name__)
    setup_routes(app)

    @app.route("/status")
    def status():
        return {"status": "Server is running", "blockchain": str(blockchain)}

    app.run(debug=True)

if __name__ == "__main__":
    from blockchain import Blockchain
    blockchain = Blockchain()
    start_server(blockchain)