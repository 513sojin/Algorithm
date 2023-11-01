# select i.ANIMAL_ID, i.NAME
# from ANIMAL_OUTS as i
# left join ANIMAL_INS as o
# on i.ANIMAL_ID = o.ANIMAL_ID
# where o.ANIMAL_ID is null
# order by o.ANIMAL_ID;

# out 에 있고 in에는 없는 기록

select o.ANIMAL_ID, o.NAME
from ANIMAL_OUTS as o
left outer join ANIMAL_INS as i
on o.ANIMAL_ID = i.ANIMAL_ID
where i.ANIMAL_ID is null
order by o.ANIMAL_ID;