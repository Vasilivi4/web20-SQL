SELECT s.name AS student_name, g.grade
FROM grades g
    JOIN students s ON g.student_id = s.id
    JOIN groups gr ON s.group_id = gr.id
WHERE g.subject_id = 1 AND gr.id = 3;