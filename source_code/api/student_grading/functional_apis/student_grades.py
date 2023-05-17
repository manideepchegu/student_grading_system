from flask import Flask, jsonify
from student_grading.source_code.api.settings import logger, connection, handle_exceptions

from student_grading.source_code.api import app



@app.route("/grade/<int:student_id>", methods=["GET"], endpoint="student_grade")
@handle_exceptions
def student_information(student_id):
    cur, conn = connection()

    # Retrieve patient details from the patient_data table
    cur.execute("SELECT grades FROM student_data WHERE student_id = %s", (student_id,))
    row = cur.fetchone()
    if not row:
        return jsonify({"message": f"No rows found "})
    grades = row
    data = {"grades" : grades}
    return jsonify(data), 200
