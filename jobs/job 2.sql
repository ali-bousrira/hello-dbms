Job 2 : 
1. SELECT Country FROM world WHERE Country like 'B%';
2. SELECT Country FROM world WHERE Country like 'Al%';
3. SELECT Country FROM world WHERE Country like '%y ';
4. SELECT Country FROM world WHERE Country like '%land ';
5. SELECT Country FROM world WHERE Country LIKE '%w%';
6. SELECT Country FROM world WHERE Country LIKE '%oo%' or name LIKE '%ee%';
7. SELECT Country FROM world WHERE LENGTH(Country) - LENGTH(REPLACE(Country, 'a', '')) >= 3;
8. SELECT Country FROM world WHERE Country LIKE '_r%';
