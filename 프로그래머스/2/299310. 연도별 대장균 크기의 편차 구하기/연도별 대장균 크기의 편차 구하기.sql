-- 코드를 작성해주세요

select YEAR1 AS YEAR, MAXSIZE - SIZE_OF_COLONY  AS YEAR_DEV, ID
from (select *, year(DIFFERENTIATION_DATE) AS YEAR1
    from ecoli_data) e1
left join (select year(DIFFERENTIATION_DATE) AS YEAR2, MAX(SIZE_OF_COLONY) AS MAXSIZE
            from ecoli_data
            group by year(DIFFERENTIATION_DATE) ) e2 ON e1.YEAR1 = e2.YEAR2
ORDER by 1 asc, 2 asc
