from flask import Flask, jsonify
from student_grading.source_code.api.settings import logger, connection, handle_exceptions

from student_grading.source_code.api import app


@app.route("/student_total_information/<int:student_id>", methods=["GET"], endpoint="student_total_information")
@handle_exceptions
def student_total_information(student_id):
    cur, conn = connection()

    # Retrieve patient details from the patient_data table
    cur.execute("SELECT total,average FROM total_marks WHERE student_id = %s", (student_id,))
    row = cur.fetchone()
    if not row:
        return jsonify({"message": f"No rows found "})
    data_list = []
    total , average= row
    data = {
        "total": total,
        "average": average,
    }
    data_list.append(data)
    return jsonify(data_list), 200