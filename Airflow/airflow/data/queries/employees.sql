-- Active: 1686219220302@@127.0.0.1@3306@employees
USE employees;

#Mostra estrutura de colunas e tipos de dados da tabela selecionada
DESCRIBE employees;

#Contagem de funcionarios
SELECT count(*) FROM employees;

# Employees table
select * from employees
    limit 10;

# Departments TABLE
select * from departments
    limit 10;

#Table dept EMPTY
select * from dept_emp
    limit 10;

SELECT emp_no, count(dept_no) as qtd
    from dept_emp
    GROUP BY emp_no;

SELECT * from dept_emp
    WHERE emp_no = 10116;

#dept manager TABLE
SELECT *  FROM dept_manager
    limit 10;

#Salaries TABLEs
SELECT * FROM salaries
    limit 10;

#Titles TABLE
SELECT * FROM titles
    limit 10;

# Tabela de funcionarios com salario e titulacao

SELECT emp.emp_no
        , emp.first_name
        , emp.last_name
        , ti.title
        , sal.salary
    FROM employees as emp
    INNER JOIN (SELECT sa.emp_no, MAX(sa.salary) as salary 
        FROM salaries as sa GROUP BY sa.emp_no) as sal
        ON sal.emp_no = emp.emp_no
        INNER JOIN titles as ti
        ON ti.emp_no = emp.emp_no
        LIMIT 100;
