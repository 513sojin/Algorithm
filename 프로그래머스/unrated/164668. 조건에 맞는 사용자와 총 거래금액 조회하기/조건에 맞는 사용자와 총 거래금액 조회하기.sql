select b.WRITER_ID, u.NICKNAME, sum(b.PRICE) as TOTAL_SALES
from USED_GOODS_BOARD as b, USED_GOODS_USER as u
where b.WRITER_ID = u.USER_ID and b.STATUS = 'DONE'
group by b.WRITER_ID
having sum(b.PRICE) >= 700000
order by sum(b.PRICE)

