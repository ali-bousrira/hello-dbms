Job 5 :
1. SELECT name, Population FROM world WHERE Population > ( SELECT Population FROM world WHERE name = 'Russia' );
2. SELECT name, GDP ($ per capita)  FROM world WHERE GDP ($ per capita)  > ( SELECT GDP ($ per capita)  FROM world WHERE name = 'Italy' );
3. SELECT name, Population FROM world WHERE Population > ( SELECT Population FROM world WHERE name = 'United Kingdom' )  
AND Population < (SELECT Population FROM world WHERE name = 'Germany' );
4. SELECT name, Population, (Population / (SELECT Population FROM world WHERE name = 'Germany')) * 100 AS pourcentage_Population FROM world
WHERE Region LIKE '%EUROPE%';
5. SELECT Region, name, Area (sq. mi.) FROM world WHERE Area (sq. mi.) IN ( SELECT MAX(Area (sq. mi.)) FROM world GROUP BY Region )
ORDER BY Region;
6. SELECT Region FROM world GROUP BY Region HAVING MIN(Population) <= 25000000 AND MAX(Population) <= 25000000;