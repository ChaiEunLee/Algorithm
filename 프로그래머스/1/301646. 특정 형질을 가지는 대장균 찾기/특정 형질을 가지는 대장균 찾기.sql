-- 코드를 작성해주세요
#2번 형질이 보유하지 않으면서 1번이나 3번 형질을 보유하고 있는 대장균 개체의 수(COUNT)를
# 16/8/4/2/1
-- 101 : 5
-- 1101 : 13
-- 10101 : 21
-- 11101 : 29


# select count(*) AS COUNT
# from (select CONV(genotype,10,2) as bingeno
#         from ecoli_data ) as z
# where (SUBSTRING(bingeno, LENGTH(bingeno)-1,1) = '0' or SUBSTRING(bingeno, LENGTH(bingeno)-1,1) = '')
#     and (SUBSTRING(bingeno, LENGTH(bingeno),1) = '1' or SUBSTRING(bingeno, LENGTH(bingeno)-2,1) = '1')

SELECT 
    COUNT(*) AS COUNT
FROM
    ECOLI_DATA
WHERE
    (GENOTYPE & 2) = 0 # 2번 형질 보유하면 안됨
    AND
    (GENOTYPE & 5) > 0 # 1번 or 3번 형질 보유해야함.
;


