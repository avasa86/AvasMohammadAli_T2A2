# AvasMohammadAli_T2A2

## Introduction
This project aims to solve the problem of issues faced by University Students or High School students. We will be creating a Student Management System which which will help us in managing students, teachers, enrollment,grading system and assignment.


## What we are trying to solve?
 - **Data Storage and tracking:** Keep track of student,teachers and data storage etc.
 - **Data Retrieval and Manipulation:** Retrieve information about classes, students, instructors, and related data. It should also enable clients to perform operations like adding new classes, enrolling students, assigning instructors, and updating class details.
 - **Data Retrieval and Manipulation:** The API Server should allow clients to retrieve information about classes, students, instructors, and related data. It should also enable clients to perform operations like adding new classes, enrolling students, assigning instructors, and updating class details.
 - **Error Handling and Validation:** Meaningful error messages and status codes to clients, indicating the nature of the problem encountered (e.g., invalid input, authorization failure, server error, etc.).
 - **Adaptability:** Is able to adapt and evolve with the requirements as the complexity of the requirements evolve.
 - **Security and Data Protection:** Implement best practices for securing data in transit and at rest. This involves encryption, secure connections (HTTPS), and other security measures.
 - **Integration with External Services** For some of the requirements of the class management system, there must be a possibility that it might rely on external services that can help in improving the overall user experience.

 ## Choice of database system
 I chose SQLite3 as a database management system:
 - **Serverless and Self-Contained:** SQLite3 is a serverless database, meaning it doesn't require a separate server process to operate. It's self-contained within the application, making it easy to set up and manage.

- **Zero Configuration:** Unlike other database systems that require complex setup procedures, SQLite3 requires minimal configuration. You don't need to install or configure a database server, making it incredibly easy to get started.

- **Lightweight:** SQLite3 is a lightweight database engine with a small memory footprint. It's designed to be efficient and consume minimal system resources, making it suitable for embedded systems and applications with limited resources.

- **Portability:** SQLite3 databases are platform-independent, which means you can use the same database file on different operating systems without any modifications.
ACID Compliant: SQLite3 is ACID (Atomicity, Consistency, Isolation, Durability) compliant, ensuring that transactions are reliably processed and that the database remains in a consistent state even in the event of errors or failures.

- **Embeddable**: SQLite3 is designed to be embedded directly into applications. It's often used in scenarios where the application needs to manage its data locally without relying on a separate database server.

- **Simplicity and Ease of Use:** The SQL syntax used in SQLite3 is straightforward and standard, making it easy for developers to work with. It supports a broad range of SQL features, making it versatile for various types of applications.

- **Low Maintenance:** Since SQLite3 doesn't require a separate server process, there's no need to perform routine maintenance tasks like backups, updates, or patches.

- **Suitable for Small to Medium-Sized Projects:** It's an excellent choice for small to medium-sized projects or applications where performance requirements are not extremely demanding. For larger, high-traffic applications, other database systems might be more appropriate.

- **Development and Testing:** SQLite3 is often used during development and testing stages because of its simplicity and ease of use. It's great for prototyping and quickly iterating on database-related functionality.

## Benefits of ORM Model
- **Simplified Database Interaction:** Makes database interaction much easier

- **Abstraction Layer:** ORM provides a layer of abstraction over the database. Developers can interact with database objects using familiar programming constructs (like classes and methods) instead of writing raw SQL queries.

- **Object-Oriented Paradigm**: ORM allows developers to work with data in an object-oriented manner. Database records are mapped to objects, making it intuitive and easier to work with data.
 
- **CRUD Operations:** ORM tools often provide methods for creating, reading, updating, and deleting records (CRUD operations). Developers can use these methods without writing complex SQL queries.

- **Query Language (e.g., SQL) Generation:** ORM tools can generate optimized SQL queries based on the actions performed on objects. This reduces the need for manual query writing.

- **Relationship Handling:** ORM tools handle relationships between different entities (tables) in the database. For example, defining one-to-many or many-to-many relationships in object models.

- **Referential Integrity:** ORMs can enforce referential integrity by automatically managing foreign keys and ensuring that relationships between objects are maintained.
  
- **Object Identity:** ORM tools often implement an identity map pattern, which ensures that the same object is reused when queried multiple times. This can improve performance by reducing redundant database calls.

- **Lazy Loading and Eager Loading:** ORMs provide options for loading related data lazily (on-demand) or eagerly (all at once). This can help optimize performance based on specific use cases.
   
- **Code Reusability:** Developers can reuse object-oriented code for database operations, reducing the need to write repetitive SQL queries.

- **Faster Development:** ORM tools handle many aspects of database interaction, allowing developers to focus on application logic rather than low-level database operations.
   
- **Database Independence:** Developers can switch between different database systems (e.g., MySQL, PostgreSQL, SQLite) without making significant changes to the application code. The ORM handles the database-specific details.

- **Cleaner Codebase:** ORM promotes cleaner, more organized code by separating database interaction logic from application logic. This makes the codebase easier to understand and maintain.

We talk about the participating entities in this project.
The participating entities are as follows:
- Student
- Teacher
- Assignment
- Grades
- Parents

After going through the requirements, and capturing all the requiring details, we have the following in our statement:
### 1.Student
- **StudentId**: stores the id of the student
- **StudentName**: stores the student name
- **DateOfBirth**: stores the date of birth of student
- **PhoneNumber**: stores the PhoneNumber of students
- **Email**: stores the email of the user

### 2.Teacher
- **TeacherId**: stores the id of the teacher
- **TeacherName**: stores the name of the teacher
- **DateOfBirth**: stores the date of birth of the teacher
- **PhoneNumber**: stores the PhoneNumber of the teacher
- **Email**: stores the email of the user

### 3. Parent
- **ParentId**: stores the id of the parent
- **ParentName**: stores the name of the parent
- **DateOfBirth**: parent details

### 4.Course
- **CourseId**: stores the id of the course
- **CourseCode**: stores the course code
- **CourseName**: stores the name of the course
- **Description**: A short description about the course

### 5.Assignment
- **AssignmentID**: stores the id of the assignment
- **AssignmentName**: stores name of the assignment
- **AssignmentDetails**: stores the details of the assignment
- **Full Marks**: stores the maximum marks of the assigment

