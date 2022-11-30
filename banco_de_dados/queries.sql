
-- pega um colaborador e retorna seu departamento e total de dependentes
select dep.name as departamento, em.name as nome, Count(depend.id) as total_dependentes from departments as dep
join Employees as em
on em.department_id = dep.id
join Dependents as depend
on responsible_id = em.id
where em.id = 3 and depend.responsible_id = em.id
group by em.id
