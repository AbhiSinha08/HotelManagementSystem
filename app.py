# Main server app

from flask import Flask, render_template, request, redirect, url_for
import os
import database
import json

os.chdir(__file__.replace(os.path.basename(__file__), ''))

app = Flask(__name__)

@app.route('/')
def index():
    room = database.source("all_rooms.sql")
    types = database.source("all_room_types.sql")
    types = {type[0]: [type[1], type[2]] for type in types}

    customer = database.source("all_customers.sql")
    customer_dict = {c[0]: c[1] + " " + c[2] for c in customer}

    employees = database.source("all_employees.sql")
    jobs = database.source("all_jobs.sql")
    jobs = {job[0]: [job[1], job[2]] for job in jobs}

    reservations = database.source("all_reservations.sql")
    return render_template("index.html", len_room=len(room),
                            room=room, room_type=types,
                            customer=customer, len_cust=len(customer),
                            jobs=jobs, employees=employees,
                            len_emp=len(employees), len_res=len(reservations),
                            cust_dict=customer_dict, res=reservations)

@app.route('/t')
def transaction_details():
    id = request.args["id"]
    details = database.source("get_transaction.sql", id)[0]
    details = {"date": str(details[0]),
                "amount": details[1],
                "payment": details[2],
                "status": details[3]
            }
    return json.dumps(details)

@app.route('/del/<name>')
def delete(name):
    id = request.args["id"]
    print(id)
    if name == "room":
        database.source("del_room.sql", id, output=False)
    elif name == "res":
        database.source("del_reservation.sql", id, output=False)
    elif name == "cust":
        database.source("del_customer.sql", id, output=False)
    elif name == "emp":
        database.source("del_employee.sql", id, output=False)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()