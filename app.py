import pymysql
import json
from flask import Flask, request

app = Flask(__name__)
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='number_plate')

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

@app.route('/add', methods=['POST'])
def add_plate():
    cur = conn.cursor()
    content = request.get_json(force=True)
    cur.execute("INSERT INTO customers (plate, name) VALUES ('" + content['plate'] + "', '" + content['name'] + "')")
    return 'ok'