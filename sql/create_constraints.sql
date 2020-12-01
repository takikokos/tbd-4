ALTER TABLE public.workload ADD CONSTRAINT job_workload_fk
FOREIGN KEY (job_id)
REFERENCES public.job (job_id)
ON DELETE CASCADE
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.job_schedule ADD CONSTRAINT job_job_schedule_fk
FOREIGN KEY (job_id)
REFERENCES public.job (job_id)
ON DELETE CASCADE
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.workload ADD CONSTRAINT employee_workload_fk
FOREIGN KEY (employee_id)
REFERENCES public.employee (employee_id)
ON DELETE CASCADE
ON UPDATE NO ACTION
NOT DEFERRABLE;