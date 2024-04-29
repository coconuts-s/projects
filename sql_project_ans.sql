-- Create the database
CREATE DATABASE IF NOT EXISTS college_management;

-- Use the database
USE college_management;

-- Create the students table
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL
);

-- Create the courses table
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    instructor VARCHAR(255) NOT NULL,
    credits INT NOT NULL
);

-- Create the enrollment table
CREATE TABLE IF NOT EXISTS enrollment (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Insert the new data into the tables
INSERT INTO students (student_name, date_of_birth, gender, email, phone_number, address)
VALUES
    ('Alice Johnson', '1998-05-15', 'Female', 'alice@example.com', '123-456-7890', '123 Main St, City'),
    ('Bob Smith', '1999-08-20', 'Male', 'bob@example.com', '234-567-8901', '456 Elm St, Town'),
    ('Charlie Brown', '1997-12-10', 'Male', 'charlie@example.com', '345-678-9012', '789 Oak St, Village'),
    ('David Miller', '1996-09-25', 'Male', 'david@example.com', '456-789-0123', '321 Pine St, City'),
    ('Emma Davis', '1998-03-30', 'Female', 'emma@example.com', '567-890-1234', '654 Oak St, Town'),
    ('Olivia Wilson', '1999-11-05', 'Female', 'olivia@example.com', '678-901-2345', '987 Elm St, City'),
    ('Ethan Martinez', '1997-07-18', 'Male', 'ethan@example.com', '789-012-3456', '789 Pine St, Town'),
    ('Mia Anderson', '1998-01-22', 'Female', 'mia@example.com', '890-123-4567', '654 Oak St, Village'),
    ('Noah Garcia', '1997-04-12', 'Male', 'noah@example.com', '901-234-5678', '321 Elm St, City'),
    ('Sophia Thomas', '1999-10-03', 'Female', 'sophia@example.com', '012-345-6789', '987 Pine St, Town');

INSERT INTO courses (course_name, instructor, credits)
VALUES
    ('Mathematics 101', 'Prof. Smith', 3),
    ('English Literature', 'Prof. Johnson', 3),
    ('Computer Science', 'Prof. Brown', 4),
    ('History', 'Prof. White', 3);

INSERT INTO enrollment (student_id, course_id, enrollment_date)
VALUES
    (1, 1, '2024-01-10'),
    (1, 2, '2024-01-10'),
    (2, 3, '2024-01-11'),
    (3, 1, '2024-01-12'),
    (4, 3, '2024-01-12'),
    (5, 2, '2024-01-13'),
    (5, 4, '2024-01-13'),
    (6, 1, '2024-01-14'),
    (6, 2, '2024-01-14'),
    (6, 3, '2024-01-14'),
    (7, 3, '2024-01-15'),
    (7, 4, '2024-01-15'),
    (8, 2, '2024-01-16'),
    (9, 1, '2024-01-17'),
    (9, 4, '2024-01-17'),
    (10, 3, '2024-01-18'),
    (10, 4, '2024-01-18');

#########################################################################################################################################################################################################
-- Q1 List all students enrolled in the 'Computer Science' course.
SELECT student_name, address FROM students S
INNER JOIN enrollment E ON S.student_id = E.student_id
INNER JOIN courses C ON E.course_id = C.course_id
WHERE course_name = "Computer Science";

-- Q2. Find the total number of credits for each student.
SELECT student_name, address, sum(credits) AS "Total Credits" FROM students S
INNER JOIN enrollment E ON S.student_id = E.student_id
INNER JOIN courses C ON E.course_id = C.course_id
GROUP BY student_name;

-- Q3. List all courses along with the number of students enrolled in each course.
SELECT course_name, group_concat(student_name), address, count(student_name) AS "Total Students" FROM students S
INNER JOIN enrollment E ON S.student_id = E.student_id
INNER JOIN courses C ON E.course_id = C.course_id
GROUP BY course_name;

-- Q4. Find the student with the highest number of enrollments.
SELECT student_name, address, count(enrollment_id) FROM students S
INNER JOIN enrollment E ON S.student_id = E.student_id
GROUP BY student_name
ORDER BY count(enrollment_id) desc
limit 1;

-- Q5. List all courses with no enrollments.
SELECT C.course_id, course_name, instructor, credits FROM courses C
INNER JOIN enrollment E ON C.course_id = E.course_id
GROUP BY course_name
HAVING count(E.course_id) = 0;

-- Q6. Find the average age of male students.
SELECT AVG(DATEDIFF(NOW(), date_of_birth) / 365) AS average_age FROM students
WHERE gender = 'Male';

-- Q7. Find the instructor(s) who teach the most courses.
SELECT instructor, COUNT(course_id) AS num_courses_taught FROM courses
GROUP BY instructor
HAVING num_courses_taught = (
    SELECT COUNT(course_id) AS max_courses FROM courses
    GROUP BY instructor
    ORDER BY max_courses DESC
    LIMIT 1
);

-- Q8. List all students who have not enrolled in any course.
SELECT S.student_id, student_name FROM enrollment E
RIGHT JOIN students S ON E.student_id = S.student_id
WHERE E.student_id is null;

-- Q9. Find the course with the highest number of credits.
SELECT * FROM courses
WHERE credits = (
SELECT max(credits) FROM courses
);

-- Q10. List all students enrolled in more than one course.
SELECT s.student_id, s.student_name, count(s.student_id) FROM students s
INNER JOIN enrollment e ON s.student_id = e.student_id
GROUP BY student_name
HAVING count(e.student_id) > 1;

-- Q11. Find the course(s) with the longest enrollment history (i.e., the earliest enrollment date).
SELECT c.course_id, course_name, enrollment_date, max(DATEDIFF(NOW(), enrollment_date)) AS Longest_Enrollment FROM courses c
INNER JOIN enrollment e ON c.course_id= e.course_id
GROUP BY course_name 
HAVING Longest_Enrollment = (
SELECT max(DATEDIFF(NOW(), enrollment_date)) FROM enrollment
)
ORDER BY course_id; # CORRECT ANSWER

-- Q12. List all students who have enrolled in a course taught by 'Prof. Brown'.
SELECT student_name, course_name, instructor FROM enrollment e
INNER JOIN students s ON e.student_id = s.student_id
INNER JOIN courses c ON e.course_id = c.course_id
WHERE instructor = "Prof. Brown";

-- Q13. Find the total number of male and female students.
SELECT gender, count(student_id) AS count FROM students
GROUP BY gender;

-- Q14. List all courses along with the number of male and female students enrolled in each course.
SELECT e.course_id, course_name, instructor, GROUP_CONCAT(gender), SUM(CASE WHEN gender = 'Male' THEN 1 ELSE 0 END) AS male_students,
    SUM(CASE WHEN gender = 'Female' THEN 1 ELSE 0 END) AS female_students
FROM enrollment e
INNER JOIN students s ON e.student_id = s.student_id
INNER JOIN courses c ON e.course_id = c.course_id
GROUP BY course_name
ORDER BY e.course_id;

-- Q15. Find the student(s) with the highest total number of credits enrolled.
SELECT s.student_id, student_name, GROUP_CONCAT(credits) AS Credits, sum(credits) AS Total_credits 
FROM enrollment e
INNER JOIN students s ON e.student_id = s.student_id
INNER JOIN courses c ON e.course_id = c.course_id
GROUP BY student_name
HAVING Total_credits = (

SELECT SUM(credits) AS total_credits 
FROM enrollment e
INNER JOIN students s ON e.student_id = s.student_id
INNER JOIN courses c ON e.course_id = c.course_id
GROUP BY student_name
ORDER BY total_credits DESC
LIMIT 1
);

-- Q16 List all courses with enrollment dates in January 2024.
SELECT DISTINCT c.course_id, course_name FROM courses c
INNER JOIN enrollment e ON c.course_id = e.course_id
GROUP BY course_name, enrollment_date
HAVING MONTH(enrollment_date) = 1 AND YEAR(enrollment_date) = 2024
ORDER BY course_id;

-- Q17. Find the student(s) enrolled in the course with the highest number of credits.
SELECT s.student_id AS Id, s.student_name AS "Student Name", 
GROUP_CONCAT(c.course_name SEPARATOR ", ") AS "Course Name", 
GROUP_CONCAT(credits SEPARATOR " + ") AS Credits, 
SUM(credits) AS "Total Credits" 
FROM enrollment e
INNER JOIN students s ON e.student_id = s.student_id
INNER JOIN courses c ON e.course_id = c.course_id
GROUP BY student_name;

-- Q18. List all courses with at least one female student enrolled.
SELECT c.course_id, c.course_name, SUM(CASE WHEN gender = 'Female' THEN 1 ELSE 0 END) AS female_students
FROM enrollment e
INNER JOIN students s ON e.student_id = s.student_id
INNER JOIN courses c ON e.course_id = c.course_id
GROUP BY course_name
HAVING (
SELECT SUM(CASE WHEN gender = 'Female' THEN 1 ELSE 0 END) AS female_students
FROM enrollment e
INNER JOIN students s ON e.student_id = s.student_id
INNER JOIN courses c ON e.course_id = c.course_id
GROUP BY course_name
ORDER BY e.course_id
) > 1; # ERROR

SELECT c.course_id, c.course_name
FROM enrollment e
INNER JOIN students s ON e.student_id = s.student_id
INNER JOIN courses c ON e.course_id = c.course_id
GROUP BY c.course_id, c.course_name
HAVING SUM(CASE WHEN s.gender = 'Female' THEN 1 ELSE 0 END) > 0; # CORRECT ANSWER

-- Q19. Find the student(s) with the earliest enrollment date.
SELECT s.student_id, student_name, enrollment_date, max(DATEDIFF(NOW(), enrollment_date)) AS Longest_Enrollment 
FROM students s
INNER JOIN enrollment e ON s.student_id = e.student_id
GROUP BY student_name
HAVING Longest_Enrollment = (
SELECT max(DATEDIFF(NOW(), enrollment_date)) FROM enrollment
)
ORDER BY course_id;

-- Q20. List all students who live in 'City'.
SELECT * FROM students
WHERE address LIKE "%City";