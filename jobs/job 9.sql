-- Job 9:

-- 1.
SELECT continent, AVG(literacy) AS avg_literacy FROM world GROUP BY continent;

-- 2. 
SELECT continent, AVG(net_migration) AS avg_net_migration FROM world GROUP BY continent;

-- 3. 
SELECT name, birthrate FROM world ORDER BY birthrate DESC LIMIT 5;

-- 4. 
SELECT name, deathrate FROM world ORDER BY deathrate DESC LIMIT 5;

-- 5. 
SELECT name, infant_mortality FROM world ORDER BY infant_mortality ASC LIMIT 5;

-- 6. 
SELECT continent, AVG(arable) AS avg_arable_land FROM world GROUP BY continent;
