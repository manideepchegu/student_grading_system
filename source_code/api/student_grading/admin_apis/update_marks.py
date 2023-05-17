from flask import Flask, request, jsonify
from student_grading.source_code.api.settings import logger, connection, handle_exceptions

from student_grading.source_code.api import app


@app.route("/update/<int:student_id>", methods=["PUT"], endpoint="update_marks")
@handle_exceptions
def update_marks(student_id):
    cur, conn = connection()

    if "maths" not in request.json or "physics" not in request.json or "chemistry" not in request.json:
        return jsonify({"message": "Details missing"})

    data = request.get_json()
    maths = data['maths']
    physics = data['physics']
    chemistry = data['chemistry']

    cur.execute('SELECT * FROM student_data WHERE student_id=%s', (student_id,))
    get_marks = cur.fetchone()

    if not get_marks:
        return jsonify({"message": "Student ID not found"})

    cur.execute("""UPDATE student_data SET maths=%s, physics=%s, chemistry=%s WHERE student_id = %s""",
                (maths, physics, chemistry, student_id))
    conn.commit()
    return jsonify({"message": "Updated successfully"})