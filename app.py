from flask import Flask,redirect,jsonify,url_for,request,render_template
from flask_mysqldb import MySQL
import json
app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSW ORD'] = ''
app.config['MYSQL_DB'] = 'todolist'
app.config['MYSQL_CURSORCLASS']="DictCursor"
mysql = MySQL(app)

@app.route('/todo/api/v1.0/tasks',methods=['GET'])
def home():
    cur=mysql.connection.cursor( )
    cur.execute("SELECT * FROM test")
    # fatchdata = cur.fetchall()
    # cur.close()
    # print(fatchdata)
    #row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    cur.close()
    # json_data=[]
    # for result in rv:
    #     json_data.append(dict(zip(row_headers,result)))
    
    return jsonify({"result": rv})

@app.route('/todo/api/v1.0/tasks/<int:id>',methods=['GET'])
def get_one(id):
    cur=mysql.connection.cursor( )
    cur.execute(f"SELECT * FROM test WHERE id ={id} ")
    # fatchdata = cur.fetchall()
    # cur.close()WHERE id=1
    # print(fatchdata)
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    cur.close()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    
    return jsonify({"result": rv})

@app.route('/todo/api/v1.0/tasks',methods=['POST'])
def post_one():
    cur=mysql.connection.cursor( )

    id = request.json['id']
    title = request.json['title']
    description= request.json['description']
    done=request.json['done']

   # cur.execute(f"INSERT INTO test (id,title,description,done) VALUES ('4','hotels','going hotels','0') ")
    cur.execute(f"INSERT INTO test (id,title,description,done) VALUES ('{id}','{title}','{description}','{done}') ")
    # fatchdata = cur.fetchall()
    # cur.close()WHERE id=1
    # print(fatchdata)
    mysql.connection.commit()
    #curs=mysql.connection.cursor( )
    cur.execute("SELECT * FROM test")
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    cur.close()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    
    return jsonify({"result": rv})  

@app.route('/todo/api/v1.0/tasks/<int:name>',methods=['PUT'])
def edit_one(name):
    cur=mysql.connection.cursor( )
    

    id = request.json['id']
    title = request.json['title']
    description= request.json['description']
    done=request.json['done']

   # cur.execute(f"UPDATE test SET id={id}, title={title}, description={description}, done={done} WHERE id={name} ")
    cur.execute(f"UPDATE test SET id='{id}', title='{title}', description='{description}', done='{done}' WHERE id={name} ")

    mysql.connection.commit()
    #curs=mysql.connection.cursor( )
    cur.execute("SELECT * FROM test")
    row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    cur.close()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    
    return jsonify({"result": rv})  

@app.route('/todo/api/v1.0/tasks/<int:id>',methods=['DELETE'])
def delete_one(id):
    cur=mysql.connection.cursor( )
    cur.execute(f"DELETE FROM test WHERE id={id}")
    mysql.connection.commit()
    #curs=mysql.connection.cursor( )
    cur.execute("SELECT * FROM test")
   # row_headers=[x[0] for x in cur.description] #this will extract row headers
    rv = cur.fetchall()
    cur.close()
    #json_data=[]
    #for result in rv:
     #   json_data.append(dict(zip(row_headers,result)))
    
    return jsonify({"result": rv})


if __name__ == "__main__":
    app.run(debug=True,port=5000)