from flask import Flask, jsonify,request
from student_grading.source_code.api.settings import logger, connection, handle_exceptions

from student_grading.source_code.api import app


@app.route("/student_id", methods=["post"], endpoint="create_student_id")
@handle_exceptions
def create_student_id():
    cur, conn = connection()
    if "name" and "physics" and "maths" and "chemistry" not in request.json:
        raise Exception("data missing")
    data = request.get_json()
    name = data['name']
    maths = data['maths']
    physics = data['physics']
    chemistry = data['chemistry']
    cur.execute('INSERT INTO student_data(name,maths,physics,chemistry)''VALUES (%s,%s, %s, %s);',
                (name, maths, physics, chemistry))
    conn.commit()
    return jsonify({"message" : "created successfully"})
