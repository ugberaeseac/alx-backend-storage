-- SQL script that ranks country origins of bands
-- ordered by the number of non-unique fans
-- import table dump metals_bands.sql.zip
-- column names must be origin and nb_fans
-- script can be executed on any database
SELECT DISTINCT origin, SUM(fans) AS nb_fans FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
