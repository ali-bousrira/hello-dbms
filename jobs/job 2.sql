Job 2 : 
1. SELECT name FROM world WHERE name = "B%";
2. SELECT name FROM world WHERE name = "Al%";
3. SELECT name FROM world WHERE name = "%y";
4. SELECT name FROM world WHERE name = "%land";
5. SELECT name FROM world WHERE name LIKE "%w%";
6. SELECT name FROM world WHERE name LIKE "%oo%" or name LIKE "%ee%";
7. SELECT name FROM world WHERE LENGTH(name) - LENGTH(REPLACE(name, 'a', '')) >= 3;
8. SELECT name FROM world WHERE name LIKE "_r%";