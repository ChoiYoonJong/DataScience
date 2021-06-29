drop table sawon;

create table sawon (
sabun number(3),
saname VARCHAR2(10),
deptno number(3),
sajob varchar2(10),
sapay number(10),
sahire date Default sysdate,
sasex varchar2(6),   
samgr number(3),    
constraint sawon_sabun_pk  primary key(sabun),
constraint sawon_deptno_fk foreign key(deptno) references dept(deptno),
constraint sawon_saname_nn check(saname IS NOT NULL),
constraint sawon_sasex_ck   check(sasex in('남자','여자')),
constraint sawon_samgr_fk  foreign key(samgr) references sawon(sabun)
);