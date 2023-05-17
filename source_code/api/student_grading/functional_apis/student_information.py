from flask import Flask, jsonify
from student_grading.source_code.api.settings import logger, connection, handle_exceptions

from student_grading.source_code.api import app


@app.route("/student_information/<int:student_id>", methods=["GET"], endpoint="student_information")
@handle_exceptions
def student_information(student_id):
    cur, conn = connection()

    # Retrieve patient details from the patient_data table
    cur.execute("SELECT name,maths,physics,chemistry FROM student_data WHERE student_id = %s", (student_id,))
    row = cur.fetchone()
    if not row:
        return jsonify({"message": f"No rows found "})
    data_list = []
    name, maths, physics, chemistry = row
    data = {
        "name": name,
        "maths": maths,
        "physics": physics,
        "chemistry": chemistry
    }
    data_list.append(data)
    return jsonify(data_list), 200