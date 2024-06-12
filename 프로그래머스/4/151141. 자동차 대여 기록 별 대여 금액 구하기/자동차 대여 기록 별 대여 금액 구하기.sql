# 
WITH TMP AS (
        SELECT A.*, B.DAILY_FEE,CASE WHEN DUR_TIME >= 90 THEN '90일 이상'
                    WHEN DUR_TIME >= 30 THEN '30일 이상'
                    WHEN DUR_TIME >= 7 THEN '7일 이상' ELSE NULL END AS LENTDAYS
        FROM (
            SELECT *, DATEDIFF(END_DATE, START_DATE)+1 AS DUR_TIME
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY ) A
        JOIN CAR_RENTAL_COMPANY_CAR B ON A.CAR_ID = B.CAR_ID
        WHERE B.CAR_TYPE = '트럭')
        
SELECT T.HISTORY_ID,
        TRUNCATE(CASE WHEN DISCOUNT_RATE IS NULL THEN DAILY_FEE * DUR_TIME 
            ELSE DAILY_FEE * (1-DISCOUNT_RATE*0.01) * DUR_TIME END, 0) AS FEE
FROM TMP T
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C ON C.CAR_TYPE = '트럭' AND DURATION_TYPE = T.LENTDAYS
ORDER BY 2 DESC, 1 DESC

