select p.MEMBER_NAME, r.REVIEW_TEXT, DATE_FORMAT(r.REVIEW_DATE, "%Y-%m-%d") as REVIEW_DATE
from MEMBER_PROFILE as p, REST_REVIEW as r
where p.MEMBER_ID = r.MEMBER_ID and
p.MEMBER_ID = (select MEMBER_ID 
                  from REST_REVIEW
                  group by MEMBER_ID
                  order by count(*) desc limit 1)
order by REVIEW_DATE, REVIEW_TEXT;