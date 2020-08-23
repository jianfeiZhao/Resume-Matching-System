run load_all_jobs.py, it will load all jobs information from Azure, i.e. the job_info_no_dup table.

add a resume txt file from ECE/CS_resumes in the data folder, as well as the job.csv in the same directory with resume_match.py, don't forget to modify the resume file's name in the code where read in the resume txt file. 

run the resume_match.py, it will recommend the top 20 similar jobs according to your resume, and also return some specific job and jobs in a specific location. We suggest you run resume_match.ipynb on google colab, it will clearly show you how it works.