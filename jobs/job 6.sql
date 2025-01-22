Job 6 :
1. SELECT SUM(Population) FROM world
2. SELECT SUM(Population) FROM world GROUP BY Region
3. SELECT SUM(GDP ($ per capita)) FROM world GROUP BY Region
4. SELECT SUM(GDP ($ per capita)) FROM world WHERE Region LIKE '%AFRICA%'
5. SELECT COUNT(*) FROM world WHERE Aera (sq.mi.) > 1 000 000;
6. SELECT SUM(Population) FROM world WHERE Country IN ('Estonia', 'Latvia', 'Lithuania');
7. SELECT COUNT(*) FROM world GROUP BY Region;
8. SELECT Region, SUM(Population) FROM world GROUP BY Region HAVING SUM(Population) >= 100000000;