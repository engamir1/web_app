# this is flask App

import json

from bson import json_util
from bson.objectid import ObjectId
from connection import *
from flask import Flask, Response, jsonify, request

app = Flask(__name__)

# get all etenders
@app.route("/all_tenders", methods=["GET"])
def get_tenders():

    try:
        data = list(my_db_connect.etender_collection.find()[0:50])
        for tender in data:
            tender["_id"] = str(tender["_id"])

        return Response(
            response=json.dumps(data, ensure_ascii=False),
            status=200,
            mimetype="application/json",
        )
    except Exception as ex:
        return Response(
            response=json.dumps(
                {
                    "messsage": "cant get any tender",
                }
            ),
            status=500,
            mimetype="application/json",
        )

    # all_tenders = list(my_db_connect.etender_collection.find({}))
    # onlt_10 = all_tenders[0:10]
    # # for doc in all_tenders:
    # #     print((doc))
    # return json_util.dumps(onlt_10, ensure_ascii=False)
    # # return json.load(json_util.dumps(all_tenders))


# -----------------------------------------------------------------------------------
# get اعمال الصيانة والترميمات


@app.route("/special", methods=["GET"])
def get_special():
    list1 = []
    try:
        data = list(my_db_connect.etender_collection.find())
        for tender in data:
            tender["_id"] = str(tender["_id"])
            if "ترميم" in tender["tender_title"] or "صيانة" in tender["tender_title"]:
                list1.append(tender)
                # print("the title is " + tender["tender_title"])
        list_len = len(list1)
        return Response(
            response=json.dumps(list1,list_len, ensure_ascii=False),
            status=200,
            mimetype="application/json",
        )
    except Exception as ex:
        return Response(
            response=json.dumps(
                {
                    "messsage": "cant get any tender",
                }
            ),
            status=500,
            mimetype="application/json",
        )


# -----------------------------------------------------------------------------------
# todo add irrigation ministry only


@app.route("/irrigation", methods=["GET"])
def get_irrigation_only():
    list1 = []
    try:
        data = list(my_db_connect.etender_collection.find())
        for tender in data:
            tender["_id"] = str(tender["_id"])
            if "الرى" in tender["entity"] or "الموارد" in tender["entity"]:
                list1.append(tender)
                # print("the title is " + tender["tender_title"])
        return Response(
            response=json.dumps(list1, ensure_ascii=False),
            status=200,
            mimetype="application/json",
        )
    except Exception as ex:
        return Response(
            response=json.dumps(
                {
                    "messsage": "cant get any tender",
                }
            ),
            status=500,
            mimetype="application/json",
        )


# -----------------------------------------------------------------------------------
@app.route("/city", methods=["GET"])
def get_dakahlya_only():
    list1 = []
    try:
        data = list(my_db_connect.etender_collection.find())
        for tender in data:
            tender["_id"] = str(tender["_id"])
            # if "الدقهلية" in tender["entity"]:
            if (
                "دمياط"
                in tender["entity"]
                # and "ترميم" in tender["tender_title"]
                # or "صيانة" in tender["tender_title"]
            ):
                list1.append(tender)
                # print("the title is " + tender["tender_title"])
        return Response(
            response=json.dumps(list1, ensure_ascii=False),
            status=200,
            mimetype="application/json",
        )
    except Exception as ex:
        return Response(
            response=json.dumps(
                {
                    "messsage": "cant get any tender",
                }
            ),
            status=500,
            mimetype="application/json",
        )


# -----------------------------------------------------------------------------------
# edit tender data
@app.route("/tender/<id>", methods=["PATCH"])
def update_tender(id):
    try:
        dbResponse = my_db_connect.etender_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"insurance": request.form["insurance"]}},
        )
        for attr in dir(dbResponse):
            print(f"*********{dir}******")
        return Response(
            response=json.dumps(
                {
                    "messsage": "update tender",
                }
            ),
            status=200,
            mimetype="application/json",
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps(
                {
                    "messsage": "cant update tender",
                }
            ),
            status=500,
            mimetype="application/json",
        )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)  # run our Flask app
