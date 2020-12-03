DROP VIEW IF EXISTS schedule_report;
DROP VIEW IF EXISTS employee_report;
DROP VIEW IF EXISTS current_workload_info;
DROP VIEW IF EXISTS employee_paid_amount_report;

CREATE OR REPLACE VIEW current_workload_info AS 
SELECT 
    w.*, 
    j.title AS job_title, 
    j.department AS job_department,
    e.name AS employee_name,
    e.contract_type
FROM workload AS w
JOIN employee AS e
ON w.employee_id = e.employee_id
JOIN job AS j
ON w.job_id = j.job_id
WHERE w.end_date IS NULL;

CREATE OR REPLACE VIEW schedule_report AS 
SELECT 
    MAX(js.department) AS department, 
    MAX(j.title) AS title,
    MAX(js.salary) AS salary,
    MAX(js.max_job_allocation) AS max_job_allocation,
    ROUND(CAST(SUM(COALESCE(w.allocation, 0)) AS NUMERIC), 1) AS current_job_allocation,
    COUNT(DISTINCT w.employee_id) AS employee_amount
FROM job_schedule AS js
LEFT JOIN current_workload_info AS w
ON js.job_id = w.job_id AND js.department = w.job_department
JOIN job AS j 
ON js.job_id = j.job_id
GROUP BY js.job_schedule_id
ORDER BY department, title;

CREATE OR REPLACE VIEW employee_report AS 
SELECT 
    e.employee_id,
    e.name,
    e.contract_type,
    w.job_title,
    w.job_department,
    COALESCE(w.allocation, 0) AS allocation,
    COALESCE(js.salary, 0) AS salary
FROM employee AS e
LEFT JOIN current_workload_info AS w
ON e.employee_id = w.employee_id
LEFT JOIN job_schedule AS js
ON w.job_id = js.job_id
ORDER BY e.employee_id, w.job_title, w.job_department;

CREATE OR REPLACE VIEW employee_paid_amount_report AS
SELECT
    e.employee_id,
    e.name,
    e.hire_date,
    j.title,
    j.department,
    SUM(js.salary * w.allocation * ((COALESCE(w.end_date, CURRENT_DATE) - w.start_date) / 30)) OVER win AS paid
FROM employee AS e
JOIN workload AS w
ON w.employee_id = e.employee_id
JOIN job AS j
ON w.job_id = j.job_id
JOIN job_schedule AS js
ON w.job_id = js.job_id
WINDOW win AS (PARTITION BY e.employee_id, j.job_id )
ORDER BY e.employee_id, j.title, j.department;
