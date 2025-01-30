# """Flask app for Cupcakes"""
# from flask import Flask, request, jsonify, render_template
# from models import db, Cupcake

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db.init_app(app)

# with app.app_context():
#     db.create_all()

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/api/cupcakes", methods=["GET"])
# def list_cupcakes():
#     cupcakes = Cupcake.query.all()
#     serialized = [cupcake.to_dict() for cupcake in cupcakes]
#     return jsonify(cupcakes=serialized)

# @app.route("/api/cupcakes/<int:cupcake_id>", methods=["GET"])
# def get_cupcake(cupcake_id):
#     cupcake = Cupcake.query.get_or_404(cupcake_id)
#     return jsonify(cupcake=cupcake.to_dict())

# @app.route("/api/cupcakes", methods=["POST"])
# def create_cupcake():
#     data = request.json
#     cupcake = Cupcake(
#         flavor=data["flavor"],
#         size=data["size"],
#         rating=data["rating"],
#         image=data.get("image", "https://tinyurl.com/demo-cupcake"),
#     )
#     db.session.add(cupcake)
#     db.session.commit()
#     return jsonify(cupcake=cupcake.to_dict()), 201

# @app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
# def update_cupcake(cupcake_id):
#     cupcake = Cupcake.query.get_or_404(cupcake_id)
#     data = request.json
#     cupcake.flavor = data.get("flavor", cupcake.flavor)
#     cupcake.size = data.get("size", cupcake.size)
#     cupcake.rating = data.get("rating", cupcake.rating)
#     cupcake.image = data.get("image", cupcake.image)
#     db.session.commit()
#     return jsonify(cupcake=cupcake.to_dict())

# @app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
# def delete_cupcake(cupcake_id):
#     cupcake = Cupcake.query.get_or_404(cupcake_id)
#     db.session.delete(cupcake)
#     db.session.commit()
#     return jsonify(message="Deleted")

from flask import Flask, jsonify, request, render_template
from models import db, Cupcake

# Define the Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

# Define routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/cupcakes", methods=["GET"])
def list_cupcakes():
    cupcakes = Cupcake.query.all()
    serialized = [cupcake.to_dict() for cupcake in cupcakes]
    return jsonify(cupcakes=serialized)

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["GET"])
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    data = request.json
    cupcake = Cupcake(
        flavor=data["flavor"],
        size=data["size"],
        rating=data["rating"],
        image=data.get("image", "https://tinyurl.com/demo-cupcake"),
    )
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake=cupcake.to_dict()), 201

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    data = request.json
    cupcake.flavor = data.get("flavor", cupcake.flavor)
    cupcake.size = data.get("size", cupcake.size)
    cupcake.rating = data.get("rating", cupcake.rating)
    cupcake.image = data.get("image", cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.to_dict())

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")