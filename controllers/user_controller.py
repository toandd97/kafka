from flask import jsonify, request, render_template
from flask import Blueprint
from models.user import User
from producer import MessageProducer
from consumer import MessageConsumer


broker = 'localhost:9092'
topic = 'test-topic'
group_id = 'consumer-1'

example_blueprint = Blueprint('example_blueprint', __name__)

@example_blueprint.route("/")
def home():
    return render_template("home.html")

@example_blueprint.route("/register", methods=["POST"])
def register():
    data = request.json
    
    send_message = {"username": data['username'], "password" : data['password']}
    message_producer = MessageProducer(broker, topic)
    if message_producer.send_msg(send_message):
        return jsonify({"success": True, "message": "User has been registered"}), 200


@example_blueprint.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    if not User.check_user(username, password):
        return jsonify({"success": False, "message": "Invalid username or password"})

    user = User.get_user_by_username(username)
    return jsonify({"success": True, "message": "Logged in successfully", "user": user})

# @example_blueprint.route("/user/<string:user_id>")
# def get_user(user_id):
#     user = User.get_user_by_id(user_id)
#     return jsonify(user)