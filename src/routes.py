from flask import request, jsonify
from src import app  # Assuming your Flask application is initialized in '__init__.py'
from models import Student, Parent

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

# Route to display all parents
@app.route('/parents', methods=['GET'])
def get_parents():
    parents = session.query(Parent).all()
    parent_list = [{'id': parent.id, 'parent_name': parent.parent_name, 'date_of_birth': parent.date_of_birth,'email':parent.email,'phone_number':parent.phone_number} for parent in parents]
    return jsonify({'parents': parent_list})

# Route to create a new parent
@app.route('/parents', methods=['POST'])
def create_parent():
    data = request.get_json()
    parent_name = data.get('student_name')
    date_of_birth = data.get('last_name')
    email = data.get('email')
    phone_number = data.get('phone_number')

    new_parent = Parent(student_name=student_name,date_of_birth=date_of_birth,email=email,phone_number=phone_number)
    session.add(new_parent)
    session.commit()

    return jsonify({'message': 'Parent created successfully'})

# Route to update a parent
@app.route('/parents/<int:id>', methods=['PUT'])
def update_parent(id):
    data = request.get_json()
    parent = session.query(Parent).get(id)

    if parent:
        parent.student_name = data.get('student_name', parent.student_name)
        parent.date_of_birth = data.get('date_of_birth', parent.date_of_birth)
        parent.email = data.get('email',parent.email)
        parent.phone_number = data.get('phone_number',parent.phone_number)
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
