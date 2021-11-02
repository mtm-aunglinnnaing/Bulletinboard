from flask import Flask, jsonify, request, session
from flask.wrappers import Request
from flaskext.mysql import MySQL
import pymysql
# from flask import Flask, render_template, request
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'crud'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/posts')
def posts():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM crud.posts")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/post/<int:id>')
def post_detail(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(
        "SELECT * FROM crud.posts WHERE id =%s", id)
    empRow = cursor.fetchone()
    respone = jsonify(empRow)
    respone.status_code = 200
    return respone


@app.route('/add-post', methods=['POST'])
def add_post():
    # try:
    _json = request.json
    _title = _json['title']
    _description = _json['description']
    _created_user_id = _json['created_user_id']
    _created_at = _json['created_at']
    _updated_at = _json['updated_at']
    sqlQuery = "INSERT INTO crud.posts(title, description, created_user_id, created_at, updated_at) VALUES(%s, %s, %s, %s, %s)"
    binData = (_title, _description, _created_user_id,
               _created_at, _updated_at)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sqlQuery, binData)
    conn.commit()
    respone = jsonify('Post added successfully!')
    respone.status_code = 200
    return respone


@app.route('/update-post', methods=['PUT'])
def update_post():
    _json = request.json
    _id = _json['id']
    _title = _json['title']
    _description = _json['description']
    _status = _json['status']
    _updated_at = _json['updated_at']
    sqlQuery = "UPDATE crud.posts SET title=%s, description=%s, status=%s, updated_at=%s WHERE id=%s"
    bindData = (_title, _description, _status, _updated_at, _id)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sqlQuery, bindData)
    conn.commit()
    respone = jsonify('post updated successfully!')
    respone.status_code = 200
    return respone


@app.route('/delete-post/<int:id>', methods=['DELETE'])
def delete_post(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM crud.posts WHERE id =%s", (id))
        conn.commit()
        respone = jsonify('User deleted successfully!!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/login', methods=['POST'])
def login():
    _json = request.json
    _email = _json['email']
    _password = _json['password']
    sqlQuery = "SELECT * FROM crud.users WHERE email = %s AND password = %s"
    binData = (_email, _password)
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sqlQuery, binData)
    empRow = cursor.fetchone()
    respone = jsonify(empRow)
    respone.status_code = 200
    return respone


@app.route('/users', methods=['GET'])
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM crud.users")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/user/<int:id>')
def user_detail(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(
        "SELECT * FROM crud.users WHERE id =%s", id)
    empRow = cursor.fetchone()
    respone = jsonify(empRow)
    respone.status_code = 200
    return respone


@app.route('/add-user', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']
    _type = _json['type']
    _phone = _json['phone']
    _dob = _json['dob']
    _address = _json['address']
    _profile = _json['profile']
    _created_user_id = _json['created_user_id']
    _updated_user_id = _json['updated_user_id']
    _created_at = _json['created_at']
    _updated_at = _json['updated_at']
    sqlQuery = "INSERT INTO crud.users(name, email, password, type, phone, dob, address, profile, created_user_id, updated_user_id, created_at, updated_at) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    binData = (_name, _email, _password, _type,
               _phone, _dob, _address, _profile, _created_user_id, _updated_user_id, _created_at, _updated_at)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sqlQuery, binData)
    conn.commit()
    respone = jsonify('User added successfully!')
    respone.status_code = 200
    return respone


@app.route('/update-user', methods=['PUT'])
def update_user():
    _json = request.json
    _id = _json['id']
    _name = _json['name']
    _email = _json['email']
    _type = _json['type']
    _phone = _json['phone']
    _dob = _json['dob']
    _profile = _json['profile']
    _address = _json['address']
    _updated_user_id = _json['updated_user_id']
    _updated_at = _json['updated_at']
    sqlQuery = "UPDATE crud.users SET name=%s, email=%s, type=%s, phone=%s, dob=%s, profile=%s, address=%s, updated_user_id=%s, updated_at=%s WHERE id=%s"
    bindData = (_name, _email, _type, _phone, _dob, _profile,
                _address, _updated_user_id, _updated_at, _id,)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sqlQuery, bindData)
    conn.commit()
    respone = jsonify('User updated successfully!')
    respone.status_code = 200
    return respone


@app.route('/delete-user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM crud.users WHERE id =%s", (id,))
        conn.commit()
        respone = jsonify('User deleted successfully!!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/change-password', methods=['PUT'])
def change_password():
    _json = request.json
    _id = _json['id']
    _password = _json['password']
    _updated_user_id = _json['updated_user_id']
    _updated_at = _json['updated_at']
    sqlQuery = "UPDATE crud.users SET password=%s, updated_user_id=%s, updated_at=%s WHERE id=%s"
    bindData = (_password, _updated_user_id, _updated_at, _id,)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sqlQuery, bindData)
    conn.commit()
    respone = jsonify('User updated successfully!')
    respone.status_code = 200
    return respone


app.config['UPLOAD_FOLDER'] = 'C:/Users/Aung Lin Naing/PycharmProjects/CRUD/frontend/src/assets/'


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(
            app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        respone = jsonify('file uploaded successfully!')
        respone.status_code = 200
        return respone


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
