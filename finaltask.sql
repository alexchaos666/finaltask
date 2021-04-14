create table dash_1
(
clients varchar2(100)
,tb varchar2(50)
);
/
create table dash_2
(
clients varchar2(100)
,segm varchar2(50)
);
/
create table dash_3
(
clients varchar2(100)
,summ number(10,2)
,commission number(10,2)
,tb varchar2(50)
);
/
SELECT * 
FROM dash_3
/
SELECT * 
FROM dash_final
/
create table dash_final
(
tb varchar2(50)
, total_comm number(10,2)
, total_summ number(10,2)
)
;

/


select  
t1.tb,
sum(t1.commission) as total_comm,
sum (t1.summ) as total_summ
from dash_3 t1
group by t1.tb
order by total_comm  desc
/
begin
pkg_ilin.make_rating_dash_final;
end;

