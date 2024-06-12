-- 코드를 작성해주세요
-- 110

-- 형질을 변환하고나서 
#SUBSTRING(CONV(GENOTYPE, 10, 2), LENGTH(CONV(GENOTYPE, 10, 2)),1)


select e1.ID, e1.GENOTYPE, e2.GENOTYPE as PARENT_GENOTYPE
from ecoli_data as e1 
join ecoli_data as e2 ON e1.PARENT_ID = e2.ID 
WHERE e1.GENOTYPE & e2.GENOTYPE = e2.GENOTYPE
ORDER BY e1.ID


