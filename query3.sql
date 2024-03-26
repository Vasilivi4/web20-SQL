SELECT g.name AS group_name, AVG(grade) AS average_grade
FROM grades gr
    JOIN students s ON gr.student_id = s.id
    JOIN groups g ON s.group_id = g.id
WHERE gr.subject_id = 7
GROUP BY g.id;