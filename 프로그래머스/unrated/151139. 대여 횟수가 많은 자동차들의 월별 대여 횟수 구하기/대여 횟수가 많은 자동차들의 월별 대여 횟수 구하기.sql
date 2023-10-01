select MONTH(START_DATE) as MONTH, CAR_ID, count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where CAR_ID in (select CAR_ID 
                 from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                 where DATE_FORMAT(START_DATE, "%Y-%m") between '2022-08' and '2022-10'
                 group by CAR_ID
                 having count(*) >= 5
                )
    and DATE_FORMAT(START_DATE, "%Y-%m") between '2022-08' and '2022-10'
group by MONTH(START_DATE), CAR_ID
having RECORDS > 0
order by MONTH, CAR_ID desc;
