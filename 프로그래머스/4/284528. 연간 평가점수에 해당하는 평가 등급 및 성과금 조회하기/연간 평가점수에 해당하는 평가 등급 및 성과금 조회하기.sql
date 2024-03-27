select emp_no, emp_name
,   case 
        when avg(score) >= 96 then 'S'
        when avg(score) >= 90 then 'A'
        when avg(score) >= 80 then 'B'
        else 'C'
    end as grade
,   sal *
    case 
        when avg(score) >= 96 then 0.2
        when avg(score) >= 90 then 0.15
        when avg(score) >= 80 then 0.1
        else 0
    end as bonus
from hr_employees 
join hr_grade using(emp_no)
join hr_department using(dept_id)
group by emp_no
order by emp_no