
CREATE TABLE public.job (
                job_id SERIAL NOT NULL,
                title VARCHAR NOT NULL,
                description VARCHAR NOT NULL,
                category VARCHAR NOT NULL,
                CONSTRAINT job_pk PRIMARY KEY (job_id)
);


CREATE TABLE public.job_schedule (
                job_schedule_id SERIAL NOT NULL,
                job_id INTEGER NOT NULL,
                department VARCHAR NOT NULL,
                max_job_allocation REAL NOT NULL,
                salary REAL NOT NULL,
                CONSTRAINT job_schedule_pk PRIMARY KEY (job_schedule_id, job_id)
);


CREATE TABLE public.employee (
                employee_id SERIAL NOT NULL,
                gender VARCHAR NOT NULL,
                education VARCHAR NOT NULL,
                family_status VARCHAR NOT NULL,
                hire_date DATE NOT NULL,
                passport VARCHAR NOT NULL,
                phone VARCHAR NOT NULL,
                home_address VARCHAR NOT NULL,
                name VARCHAR NOT NULL,
                birthday DATE NOT NULL,
                contract_type VARCHAR NOT NULL,
                CONSTRAINT employee_pk PRIMARY KEY (employee_id)
);


CREATE TABLE public.workload (
                workload_id SERIAL NOT NULL,
                allocation REAL NOT NULL,
                job_id INTEGER NOT NULL,
                employee_id INTEGER NOT NULL,
                start_date DATE NOT NULL,
                end_date DATE,
                CONSTRAINT workload_pk PRIMARY KEY (workload_id)
);

