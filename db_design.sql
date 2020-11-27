
CREATE TABLE public.job (
                job_id INTEGER NOT NULL,
                title VARCHAR NOT NULL,
                description VARCHAR NOT NULL,
                category VARCHAR NOT NULL,
                CONSTRAINT job_pk PRIMARY KEY (job_id)
);


CREATE TABLE public.job_schedule (
                job_schedule_id INTEGER NOT NULL,
                job_id INTEGER NOT NULL,
                department VARCHAR NOT NULL,
                max_job_allocation REAL NOT NULL,
                salary REAL NOT NULL,
                CONSTRAINT job_schedule_pk PRIMARY KEY (job_schedule_id, job_id)
);


CREATE TABLE public.employee (
                employee_id INTEGER NOT NULL,
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
                workload_id INTEGER NOT NULL,
                allocation REAL NOT NULL,
                job_id INTEGER NOT NULL,
                employee_id INTEGER NOT NULL,
                start_date DATE NOT NULL,
                end_date DATE,
                CONSTRAINT workload_pk PRIMARY KEY (workload_id)
);


ALTER TABLE public.workload ADD CONSTRAINT job_workload_fk
FOREIGN KEY (job_id)
REFERENCES public.job (job_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.job_schedule ADD CONSTRAINT job_job_schedule_fk
FOREIGN KEY (job_id)
REFERENCES public.job (job_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.workload ADD CONSTRAINT employee_workload_fk
FOREIGN KEY (employee_id)
REFERENCES public.employee (employee_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
