from datetime import date

class Filters:
    @staticmethod
    def filter_jobs(joblist: list)->list:
        joblist = Filters._missed_deadline(joblist)
        return joblist
    
    @staticmethod
    def _missed_deadline(joblist: list) -> list:
        return [
            job for job in joblist
            if job["date_begins"] is None
            or date.fromisoformat(job["date_begins"]) > date.today()
        ]