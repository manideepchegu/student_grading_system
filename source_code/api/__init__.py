from flask import Flask


app = Flask(__name__)
# CORS(app)
app.config['CACHE_TYPE'] = 'simple'
# cache.init_app(app)

from student_grading.source_code.api.student_grading.admin_apis import create_student_id, calculate_average_total, delete_student, grading_system, update_marks
from student_grading.source_code.api.student_grading.functional_apis import all_students, get_total_average, student_information, student_grades
