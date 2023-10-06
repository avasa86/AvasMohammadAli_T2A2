from flask import request, jsonify
from src import app  # Assuming your Flask application is initialized in '__init__.py'
from models import Student, Parent, Teacher, Coursem Assignment,Grade

# Create engine and session
engine = create_engine('sqlite:///class_management.db') 
Session = sessionmaker(bind=engine)
session = Session()

# Route to display all students
@app.route('/students', methods=['GET'])
def get_students():
    students = session.query(Student).all()
    student_list = [{'id': student.id, 'student_name': student.student_name, 'date_of_birth': student.date_of_birth,'email':student.email,'phone_number':student.phone_number} for student in students]
    return jsonify({'students': student_list})

# Route to create a new student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student_name = data.get('student_name')
    date_of_birth = data.get('last_name')
    email = data.get('email')
    phone_number = data.get('phone_number')


    new_student = Student(student_name=student_name,date_of_birth=date_of_birth,email=email,phone_number=phone_number)
    session.add(new_student)
    session.commit()

    return jsonify({'message': 'Student created successfully'})

# Route to update a student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    student = session.query(Student).get(id)

    if student:
        student.student_name = data.get('student_name', student.student_name)
        student.date_of_birth = data.get('date_of_birth', student.date_of_birth)
        student.email = data.get('email',student.email)
        student.phone_number = data.get('phone_number',student.phone_number)
        session.commit()
        return jsonify({'message': 'Student updated successfully'})
    else:
        return jsonify({'error': 'Student not found'}), 404

# Route to delete a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = session.query(Student).get(id)

    if student:
        session.delete(student)
        session.commit()
        return jsonify({'message': 'Student deleted successfully'})
    else:
        return jsonify({'error': 'Student not found'}), 404

# Validation and sanitization functions
def validate_email(email):
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
    return re.match(email_regex, email) is not None

def validate_date_of_birth(date_of_birth):
    try:
        datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def sanitize_input(input_string):
    return input_string.replace("'", '"')

# Route to create a new parent
@app.route('/parents', methods=['POST'])
def create_parent():
    data = request.get_json()

    parent_name = sanitize_input(data.get('parent_name'))
    date_of_birth = sanitize_input(data.get('date_of_birth'))
    email = sanitize_input(data.get('email'))
    phone_number = sanitize_input(data.get('phone_number'))

    if not validate_email(email):
        return jsonify({'error': 'Invalid email address'}), 400

    if not validate_date_of_birth(date_of_birth):
        return jsonify({'error': 'Invalid date of birth'}), 400

    new_parent = Parent(
        parent_name=parent_name,
        date_of_birth=date_of_birth,
        email=email,
        phone_number=phone_number
    )

    session.add(new_parent)
    session.commit()

    return jsonify({'message': 'Parent created successfully'})

# Route to get all parents
@app.route('/parents', methods=['GET'])
def get_parents():
    parents = session.query(Parent).all()
    parent_list = [{'id': parent.id, 'parent_name': parent.parent_name, 'date_of_birth': parent.date_of_birth,
                    'email': parent.email, 'phone_number': parent.phone_number} for parent in parents]
    return jsonify({'parents': parent_list})

# Route to get a specific parent
@app.route('/parents/<int:id>', methods=['GET'])
def get_parent(id):
    parent = session.query(Parent).get(id)
    if parent:
        parent_info = {'id': parent.id, 'parent_name': parent.parent_name, 'date_of_birth': parent.date_of_birth,
                       'email': parent.email, 'phone_number': parent.phone_number}
        return jsonify({'parent': parent_info})
    else:
        return jsonify({'error': 'Parent not found'}), 404

# Route to update a parent
@app.route('/parents/<int:id>', methods=['PUT'])
def update_parent(id):
    data = request.get_json()
    parent = session.query(Parent).get(id)

    if parent:
        parent.parent_name = sanitize_input(data.get('parent_name', parent.parent_name))
        parent.date_of_birth = sanitize_input(data.get('date_of_birth', parent.date_of_birth))
        parent.email = sanitize_input(data.get('email', parent.email))
        parent.phone_number = sanitize_input(data.get('phone_number', parent.phone_number))

        if not validate_email(parent.email):
            return jsonify({'error': 'Invalid email address'}), 400

        if not validate_date_of_birth(parent.date_of_birth):
            return jsonify({'error': 'Invalid date of birth'}), 400

        session.commit()
        return jsonify({'message': 'Parent updated successfully'})
    else:
        return jsonify({'error': 'Parent not found'}), 404

# Route to delete a parent
@app.route('/parents/<int:id>', methods=['DELETE'])
def delete_parent(id):
    parent = session.query(Parent).get(id)

    if parent:
        session.delete(parent)
        session.commit()
        return jsonify({'message': 'Parent deleted successfully'})
    else:
        return jsonify({'error': 'Parent not found'}), 404


# Validation and sanitization functions
def validate_email(email):
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
    return re.match(email_regex, email) is not None

def validate_date_of_birth(date_of_birth):
    try:
        datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def sanitize_input(input_string):
    return input_string.replace("'", '"')

# Route to create a new teacher
@app.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.get_json()

    teacher_name = sanitize_input(data.get('teacher_name'))
    date_of_birth = sanitize_input(data.get('date_of_birth'))
    email = sanitize_input(data.get('email'))
    phone_number = sanitize_input(data.get('phone_number'))

    if not validate_email(email):
        return jsonify({'error': 'Invalid email address'}), 400

    if not validate_date_of_birth(date_of_birth):
        return jsonify({'error': 'Invalid date of birth'}), 400

    new_teacher = Teacher(
        teacher_name=teacher_name,
        date_of_birth=date_of_birth,
        email=email,
        phone_number=phone_number
    )

    session.add(new_teacher)
    session.commit()

    return jsonify({'message': 'Teacher created successfully'})

# Route to get all teachers
@app.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = session.query(Teacher).all()
    teacher_list = [{'id': teacher.id, 'teacher_name': teacher.teacher_name, 'date_of_birth': teacher.date_of_birth,
                     'email': teacher.email, 'phone_number': teacher.phone_number} for teacher in teachers]
    return jsonify({'teachers': teacher_list})

# Route to get a specific teacher
@app.route('/teachers/<int:id>', methods=['GET'])
def get_teacher(id):
    teacher = session.query(Teacher).get(id)
    if teacher:
        teacher_info = {'id': teacher.id, 'teacher_name': teacher.teacher_name, 'date_of_birth': teacher.date_of_birth,
                        'email': teacher.email, 'phone_number': teacher.phone_number}
        return jsonify({'teacher': teacher_info})
    else:
        return jsonify({'error': 'Teacher not found'}), 404

# Route to update a teacher
@app.route('/teachers/<int:id>', methods=['PUT'])
def update_teacher(id):
    data = request.get_json()
    teacher = session.query(Teacher).get(id)

    if teacher:
        teacher.teacher_name = sanitize_input(data.get('teacher_name', teacher.teacher_name))
        teacher.date_of_birth = sanitize_input(data.get('date_of_birth', teacher.date_of_birth))
        teacher.email = sanitize_input(data.get('email', teacher.email))
        teacher.phone_number = sanitize_input(data.get('phone_number', teacher.phone_number))

        if not validate_email(teacher.email):
            return jsonify({'error': 'Invalid email address'}), 400

        if not validate_date_of_birth(teacher.date_of_birth):
            return jsonify({'error': 'Invalid date of birth'}), 400

        session.commit()
        return jsonify({'message': 'Teacher updated successfully'})
    else:
        return jsonify({'error': 'Teacher not found'}), 404

# Route to delete a teacher
@app.route('/teachers/<int:id>', methods=['DELETE'])
def delete_teacher(id):
    teacher = session.query(Teacher).get(id)

    if teacher:
        session.delete(teacher)
        session.commit()
        return jsonify({'message': 'Teacher deleted successfully'})
    else:
        return jsonify({'error': 'Teacher not found'}), 404

# Validation and sanitization functions
def sanitize_input(input_string):
    return input_string.replace("'", '"')

def validate_teacher_id(teacher_id):
    if not teacher_id:
        return False

    teacher = session.query(Teacher).get(teacher_id)
    return teacher is not None

# Route to create a new course
@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()

    course_code = sanitize_input(data.get('course_code'))
    course_name = sanitize_input(data.get('course_name'))
    description = sanitize_input(data.get('description'))
    teacher_id = data.get('teacher_id')

    # Check if course code is not empty
    if not course_code:
        return jsonify({'error': 'Course code cannot be empty'}), 400

    # Validate teacher_id
    if not validate_teacher_id(teacher_id):
        return jsonify({'error': 'Invalid teacher ID'}), 400

    new_course = Course(
        course_code=course_code,
        course_name=course_name,
        description=description,
        teacher_id=teacher_id
    )

    session.add(new_course)
    session.commit()

    return jsonify({'message': 'Course created successfully'})

# Route to get all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    courses = session.query(Course).all()
    course_list = [{'id': course.id, 'course_code': course.course_code, 'course_name': course.course_name,
                    'description': course.description, 'teacher_id': course.teacher_id} for course in courses]
    return jsonify({'courses': course_list})

# Route to get a specific course
@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    course = session.query(Course).get(id)
    if course:
        course_info = {'id': course.id, 'course_code': course.course_code, 'course_name': course.course_name,
                       'description': course.description, 'teacher_id': course.teacher_id}
        return jsonify({'course': course_info})
    else:
        return jsonify({'error': 'Course not found'}), 404

# Route to update a course
@app.route('/courses/<int:id>', methods=['PUT'])
def update_course(id):
    data = request.get_json()
    course = session.query(Course).get(id)

    if course:
        course.course_code = sanitize_input(data.get('course_code', course.course_code))
        course.course_name = sanitize_input(data.get('course_name', course.course_name))
        course.description = sanitize_input(data.get('description', course.description))

        # Update the teacher_id if provided in the request
        teacher_id = data.get('teacher_id')
        if teacher_id and validate_teacher_id(teacher_id):
            course.teacher_id = teacher_id

        session.commit()
        return jsonify({'message': 'Course updated successfully'})
    else:
        return jsonify({'error': 'Course not found'}), 404

# Route to delete a course
@app.route('/courses/<int:id>', methods=['DELETE'])
def delete_course(id):
    course = session.query(Course).get(id)

    if course:
        session.delete(course)
        session.commit()
        return jsonify({'message': 'Course deleted successfully'})
    else:
        return jsonify({'error': 'Course not found'}), 404


# Validation function for maximum_marks
def validate_maximum_marks(maximum_marks):
    if not isinstance(maximum_marks, int) or maximum_marks <= 0:
        return False
    return True

# Sanitization function for input strings
def sanitize_input(input_string):
    return input_string.replace("'", "''")

# Route to create a new assignment
@app.route('/assignments', methods=['POST'])
def create_assignment():
    data = request.get_json()

    assignment_name = sanitize_input(data.get('assignment_name'))
    assignment_details = sanitize_input(data.get('assignment_details'))
    maximum_marks = data.get('maximum_marks')

    # Validate maximum_marks
    if not validate_maximum_marks(maximum_marks):
        return jsonify({'error': 'Invalid maximum marks'}), 400

    new_assignment = Assignment(
        assignment_name=assignment_name,
        assignment_details=assignment_details,
        maximum_marks=maximum_marks
    )

    session.add(new_assignment)
    session.commit()

    return jsonify({'message': 'Assignment created successfully'})

# Route to get all assignments
@app.route('/assignments', methods=['GET'])
def get_assignments():
    assignments = session.query(Assignment).all()
    assignment_list = [{'id': assignment.id, 'assignment_name': assignment.assignment_name,
                        'assignment_details': assignment.assignment_details, 'maximum_marks': assignment.maximum_marks}
                       for assignment in assignments]
    return jsonify({'assignments': assignment_list})

# Route to get a specific assignment
@app.route('/assignments/<int:id>', methods=['GET'])
def get_assignment(id):
    assignment = session.query(Assignment).get(id)
    if assignment:
        assignment_info = {'id': assignment.id, 'assignment_name': assignment.assignment_name,
                            'assignment_details': assignment.assignment_details, 'maximum_marks': assignment.maximum_marks}
        return jsonify({'assignment': assignment_info})
    else:
        return jsonify({'error': 'Assignment not found'}), 404

# Route to update an assignment
@app.route('/assignments/<int:id>', methods=['PUT'])
def update_assignment(id):
    data = request.get_json()
    assignment = session.query(Assignment).get(id)

    if assignment:
        assignment.assignment_name = sanitize_input(data.get('assignment_name', assignment.assignment_name))
        assignment.assignment_details = sanitize_input(data.get('assignment_details', assignment.assignment_details))

        maximum_marks = data.get('maximum_marks')
        if maximum_marks and validate_maximum_marks(maximum_marks):
            assignment.maximum_marks = maximum_marks

        session.commit()
        return jsonify({'message': 'Assignment updated successfully'})
    else:
        return jsonify({'error': 'Assignment not found'}), 404

# Route to delete an assignment
@app.route('/assignments/<int:id>', methods=['DELETE'])
def delete_assignment(id):
    assignment = session.query(Assignment).get(id)

    if assignment:
        session.delete(assignment)
        session.commit()
        return jsonify({'message': 'Assignment deleted successfully'})
    else:
        return jsonify({'error': 'Assignment not found'}), 404


# Validation function for grade_value
def validate_grade_value(grade_value):
    return isinstance(grade_value, float) and 0 <= grade_value <= 100

# Sanitization function for input strings
def sanitize_input(input_string):
    return input_string.replace("'", "''")

# Route to create a new grade
@app.route('/grades', methods=['POST'])
def create_grade():
    data = request.get_json()

    student_id = data.get('student_id')
    assignment_id = data.get('assignment_id')
    grade_value = data.get('grade_value')

    # Validate grade_value
    if not validate_grade_value(grade_value):
        return jsonify({'error': 'Invalid grade value'}), 400

    new_grade = Grade(
        student_id=student_id,
        assignment_id=assignment_id,
        grade_value=grade_value
    )

    session.add(new_grade)
    session.commit()

    return jsonify({'message': 'Grade created successfully'})

# Route to get all grades
@app.route('/grades', methods=['GET'])
def get_grades():
    grades = session.query(Grade).all()
    grade_list = [{'id': grade.id, 'student_id': grade.student_id, 'assignment_id': grade.assignment_id,
                   'grade_value': grade.grade_value} for grade in grades]
    return jsonify({'grades': grade_list})

# Route to get a specific grade
@app.route('/grades/<int:id>', methods=['GET'])
def get_grade(id):
    grade = session.query(Grade).get(id)
    if grade:
        grade_info = {'id': grade.id, 'student_id': grade.student_id, 'assignment_id': grade.assignment_id,
                      'grade_value': grade.grade_value}
        return jsonify({'grade': grade_info})
    else:
        return jsonify({'error': 'Grade not found'}), 404

# Route to update a grade
@app.route('/grades/<int:id>', methods=['PUT'])
def update_grade(id):
    data = request.get_json()
    grade = session.query(Grade).get(id)

    if grade:
        grade.student_id = data.get('student_id', grade.student_id)
        grade.assignment_id = data.get('assignment_id', grade.assignment_id)

        grade_value = data.get('grade_value')
        if grade_value and validate_grade_value(grade_value):
            grade.grade_value = grade_value

        session.commit()
        return jsonify({'message': 'Grade updated successfully'})
    else:
        return jsonify({'error': 'Grade not found'}), 404

# Route to delete a grade
@app.route('/grades/<int:id>', methods=['DELETE'])
def delete_grade(id):
    grade = session.query(Grade).get(id)

    if grade:
        session.delete(grade)
        session.commit()
        return jsonify({'message': 'Grade deleted successfully'})
    else:
        return jsonify({'error': 'Grade not found'}), 404

