sqlAlchemy_and_sql_scripts: Some sql scripts for data manipulation and cleaning as well as sqlAlchemy script for creating a table and populating with fake data

RUN: mysql -u root -p in the terminal

SAMPLE QUERY for mysql_db.py 

SELECT
  p.first_name,
  p.last_name,
  p.salary,
  j.description
FROM
  persons AS p
JOIN
  jobs AS j ON
  p.job_id = j.job_id
WHERE 
  p.salary > 130000
ORDER BY
  p.salary DESC;
