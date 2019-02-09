import pymysql
import json
from flask import Flask, request

app = Flask(__name__)
conn = pymysql.connect(host='numberplate.ca8irzpscuzv.eu-west-3.rds.amazonaws.com', port=3306, user='root', passwd='password', db='numberplate')

@app.route('/', methods=['GET'])
def home():
    cur = conn.cursor()
    cur.execute("SELECT id, plate, name FROM customers")
    result = []
    for row in cur:
        (id, plate, name) = row
        result.append({'name' : name, 'id' : id, 'plate': plate})
    print(json.dumps(result))
    cur.close()
    return json.dumps(result)

@app.route('/entries', methods=['GET'])
def entries():
    cur = conn.cursor()
    cur.execute("SELECT id, in_out, reg_time, customer_id FROM entries")
    result = []
    for row in cur:
        (id, in_out, reg_time, customer_id) = row
        result.append({'reg_time' : str(reg_time), 'id' : id, 'in_out': in_out, 'customer_id': customer_id})
    print(json.dumps(result))
    cur.close()
    return json.dumps(result)

@app.route('/add/customer', methods=['POST'])
def add_plate():
    cur = conn.cursor()
    content = request.get_json(force=True)
    cur.execute("INSERT INTO customers (plate, name) VALUES ('" + content['plate'] + "', '" + content['name'] + "')")
    return 'ok'

@app.route('/add/entry', methods=['POST'])
def add_entry():
    cur = conn.cursor()
    content = request.get_json(force=True)
    cur.execute("INSERT INTO entries (customer_id, in_out) VALUES ('" + content['customer_id'] + "', '" + content['in_out'] + "')")
    return 'ok'

@app.route('/recognize', methods=['POST'])
def recognize_photo():
    f = request.files['file']
    f.save('./%s' % f.filename)
    return 'file uploaded successfully'