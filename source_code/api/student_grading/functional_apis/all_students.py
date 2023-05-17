
from flask import Flask, jsonify
from student_grading.source_code.api.settings import logger, connection, handle_exceptions

from student_grading.source_code.api import app


@app.route("/students/all", methods=["GET"], endpoint="all_students_information")
@handle_exceptions
def all_students_information():
    cur, conn = connection()

    # Retrieve patient details from the patient_data table
    cur.execute("SELECT student_id,name,maths,physics,chemistry FROM student_data ")
    rows = cur.fetchall()
    if not rows:
        return jsonify({"message": f"No rows found "})
    data_list = []
    for row in rows:
        student_id, name, maths, physics, chemistry = row
        data = {
            "student_id": student_id,
            "name": name,
            "maths": maths,
            "physics": physics,
            "chemistry": chemistry

        }
        data_list.append(data)
    return jsonify(data_list), 200
