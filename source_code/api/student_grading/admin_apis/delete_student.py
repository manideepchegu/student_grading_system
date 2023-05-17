from flask import Flask, jsonify
from student_grading.source_code.api.settings import logger, connection, handle_exceptions

from student_grading.source_code.api import app


@app.route("/student/delete/<int:student_id>", methods=["DELETE"], endpoint="delete_student")
@handle_exceptions
def delete_item(student_id):
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    cur.execute('DELETE FROM student_data WHERE student_id=%s', (student_id,))
    logger(__name__).warning("close the database connection")
    conn.commit()
    if cur.rowcount > 0:
        return jsonify({"message": "student_id deleted successfully"})
    else:
        return jsonify({"message": "student_id not found"})

