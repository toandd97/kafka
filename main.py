from consumer import MessageConsumer
from models.user import User
from flask import jsonify


import os
import json
import requests
broker = 'localhost:9092'
topic = 'test-topic'
group_id = 'consumer-1'


# def function(x, received, User):
#     match x:
#         case 'create':
#             print('vao day create')
#             print("name: {}, email: {} , pass: {}".format(received.value["username"], received.value["email"], received.value["password"]))
#             User(received.value["username"], received.value["email"], received.value["password"]).create()




#             # data1 = {"username": received.value["username"], 'email': received.value['email'], 'password': received.value['password']}
#             # URL = "http://localhost:5000/register"
#             # print(URL)
#             #
#             # headers = {"Content-Type": "application/json"}
#             #
#             # response = requests.request(
#             #     "POST", URL, headers=headers, data=json.dumps(data1),
#             # )
#             # print(response)

#             return {"status": 200, "data": {"message": "record uploaded to Elastic Search"}}
#         case 'b':
#             return 2
#         case _:
#             print('0')
#             return 0


if __name__ == '__main__':
    while True:
        received = MessageConsumer(broker, topic, group_id).activate_listener()
        # MessageConsumer.get_data(received)
        print(received)
        # if received != None:
        #     print('vao day')
        #     function(received.value["function"], received, User)


        #     # match received.value["function"]:
        #     #     case 'create':
        #     #         User(received.value["username"], received.value["email"], received.value["password"]).create()
        #     #         # return jsonify({"success": True, "message": "User has been registered"})
        #     #
        #     #     case default:
        #     #         print('haha')
        #     # print('1111')




