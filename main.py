from flask import Flask, request, render_template, form
from flask import g
from db import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/data', methods=["post"])
def data():

    ricetpe1 = form.request["ricetype"]
    ricequality1 = form.request["ricequality"]
    ricequantity1 = form.request["ricequantity"]
    rsmentry1 = form.request["rsmentry"]
    # from db import *
    if(rsmentry1 == "in"):
        sql = "UPDATE customers SET ricequantity = ricequantity+ricequantity1 "

        mycursor.execute(sql)

        mydb.commit()

        print(mycursor.rowcount, "record(s) affected")

        return "quantity get added"
    else:
        sql = "UPDATE customers SET ricequantity = ricequantity-ricequantity1 "

        mycursor.execute(sql)

        mydb.commit()

        print(mycursor.rowcount, "record(s) affected")

        return "qunatity get loose"


if __name__ == '__main__':
    app.run()
