drop table dept;

create table dept (
deptno number(3), 
dname varchar2(10) ,
loc varchar(20),
constraint dept_deptno_key Primary Key(deptno),
constraint dept_danme_uq unique(dname)
);