-- 코드를 입력하세요

# 세단, SUV
# 2022-11-01~2022-11-30 대여가능한 
# 30일간 대여 금액이 50 이상 200 미만

WITH CARLIST AS 
(SELECT *
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_ID NOT IN  (SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE DATE_FORMAT(END_DATE, '%Y-%m-%d') >= '2022-11-01' AND DATE_FORMAT(START_DATE, '%Y-%m-%d') <= '2022-11-30')
AND (CAR_TYPE = '세단' OR CAR_TYPE = 'SUV')
),
FEE AS (
select *
FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
where (car_type = '세단' and duration_type = '30일 이상' ) or (car_type = 'SUV' and duration_type = '30일 이상' ) 
) 

select A.CAR_ID, A.CAR_TYPE,  TRUNCATE(daily_fee * (1-discount_rate*0.01) * 30,0) AS FEE
from carlist a
left join fee b on a.car_type = b.car_type
WHERE TRUNCATE(daily_fee * (1-discount_rate*0.01) * 30,0) >= 500000 
AND TRUNCATE(daily_fee * (1-discount_rate*0.01) * 30,0) <2000000
ORDER BY FEE desc, A.car_type asc, A.CAR_ID desc

