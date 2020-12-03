-- this script should be run BEFORE creating constraints

SET DATESTYLE TO SQL, DMY;

-- load employee table 
COPY employee
FROM '/mocks/MOCK_employee_table.tsv'
DELIMITER E'\t'
CSV HEADER;

SELECT setval(pg_get_serial_sequence('employee', 'employee_id'), max(employee_id)) FROM employee;

-- load job table
COPY job
FROM '/mocks/MOCK_job_table.tsv'
DELIMITER E'\t'
CSV HEADER;

DELETE FROM job
WHERE job_id NOT IN (
                    SELECT t1.job_id 
                    FROM 
                        (SELECT MIN(job_id) AS job_id, 
                                title, 
                                category,
                                department
                        FROM job
                        GROUP BY title, category, department
                        ) AS t1
                    );

-- drop 2/3 of table, i guess it's too big
DELETE FROM job
WHERE random() <= 0.66;

SELECT setval(pg_get_serial_sequence('job', 'job_id'), max(job_id)) FROM job;

-- load workload table
COPY workload
FROM '/mocks/MOCK_workload_table.tsv'
DELIMITER E'\t'
CSV HEADER;

DELETE FROM workload
WHERE employee_id NOT IN (SELECT employee_id FROM employee)
OR job_id NOT IN (SELECT job_id FROM job);

DELETE FROM workload
WHERE workload_id IN (SELECT MAX(workload_id) 
                      FROM workload 
                      WHERE end_date IS NULL 
                      GROUP BY employee_id, job_id 
                      HAVING COUNT(*) > 1
                      );

-- drop 2/3 of table, i guess it's too big
DELETE FROM workload
WHERE random() <= 0.66;

SELECT setval(pg_get_serial_sequence('workload', 'workload_id'), max(workload_id)) FROM workload;


-- load job_schedule table
COPY job_schedule
FROM '/mocks/MOCK_job_schedule_table.tsv'
DELIMITER E'\t'
CSV HEADER;

DELETE FROM job_schedule
WHERE job_id NOT IN (SELECT job_id FROM job);

DELETE FROM job_schedule
WHERE job_schedule_id NOT IN (
                            SELECT js.job_schedule_id
                            FROM job_schedule AS js
                            JOIN job AS j ON j.job_id = js.job_id
                            WHERE js.department = j.department
                            );

DELETE FROM job_schedule
WHERE job_schedule_id NOT IN (
                        SELECT t1.job_schedule_id 
                        FROM 
                            (SELECT MIN(job_schedule_id) AS job_schedule_id,
                                    job_id, 
                                    department 
                            FROM job_schedule
                            GROUP BY job_id, department
                            ) AS t1
                        );

-- DELETE FROM job_schedule
-- WHERE random() <= 0.66;

SELECT setval(pg_get_serial_sequence('job_schedule', 'job_schedule_id'), max(job_schedule_id)) FROM job_schedule;
