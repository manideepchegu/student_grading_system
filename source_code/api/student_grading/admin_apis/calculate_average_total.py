from flask import Flask, jsonify
from student_grading.source_code.api.settings import logger, connection, handle_exceptions

from student_grading.source_code.api import app


@app.route("/average/<int:student_id>", methods=["POST"], endpoint="calculate_average")
@handle_exceptions
def calculate_average(student_id):
    cur, conn = connection()
    cur.execute("SELECT maths,physics,chemistry FROM student_data WHERE student_id = %s", (student_id,))
    row = cur.fetchone()
    if not row:
        return jsonify({"message": f"No rows found "})
    maths, physics, chemistry = row
    total = maths + physics + chemistry
    average = total/3
    cur.execute("INSERT INTO total_marks (student_id, total, average) VALUES (%s, %s, %s)",
                (student_id, total, average))
    conn.commit()
    return jsonify({"total": total, "average": average})