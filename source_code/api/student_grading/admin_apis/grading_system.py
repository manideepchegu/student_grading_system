
from flask import Flask, jsonify
from student_grading.source_code.api.settings import logger, connection, handle_exceptions

from student_grading.source_code.api import app


@app.route("/student/grading/<int:student_id>", methods=["PUT"], endpoint="grading")
@handle_exceptions
def grading(student_id):
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    cur.execute("SELECT maths,physics,chemistry from student_data where student_id=%s",(student_id,))
    row = cur.fetchone()
    if not row:
        return jsonify({"message": f"No rows found "})
    maths, physics, chemistry = row
    average = (maths + physics + chemistry)/3
    if 80 <= average <= 100:
        grades = "A"
    elif 65 <= average <= 79:
        grades = "B"
    elif 55 <= average <= 64:
        grades = "C"
    elif 50 <= average <= 54:
        grades = "D"
    else:
        grades = "E"
    cur.execute('UPDATE student_data SET grades=%s WHERE student_id=%s',(grades,student_id))
    conn.commit()
    return "updated successfully"
