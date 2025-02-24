-- job 7:
--2.
SELECT matchid, player FROM goal WHERE teamid = 'GER';   
--3.
SELECT id, stadium, team1, team2 FROM game WHERE id = 1012;
--4. 
SELECT goal.player, goal.teamid, game.stadium, game.mdate FROM goal JOIN game ON goal.matchid = game.id WHERE goal.teamid = 'GER';
--5. 
SELECT game.team1, game.team2, goal.player FROM goal JOIN game ON goal.matchid = game.id WHERE goal.player LIKE 'Mario%';
--6. 
SELECT goal.*, eteam.* FROM goal JOIN eteam ON goal.teamid = eteam.id;
--7. 
SELECT goal.player, goal.teamid, eteam.coach, goal.gtime FROM goal JOIN eteam ON goal.teamid = eteam.id WHERE goal.gtime <= 10;
--8. 
SELECT game.mdate, eteam.teamname FROM game JOIN eteam ON game.team1 = eteam.id WHERE eteam.coach = 'Fernando Santos';
--9. 
SELECT goal.player, goal.matchid FROM goal JOIN game ON goal.matchid = game.id WHERE game.stadium = 'National Stadium, Warsaw';
--10. 
SELECT teamid, COUNT(*) AS total_goals FROM goal GROUP BY teamid;
--11. 
SELECT game.stadium, COUNT(goal.player) AS total_goals FROM game JOIN goal ON game.id = goal.matchid GROUP BY game.stadium;
--12. 
SELECT game.id, game.mdate, COUNT(goal.player) AS total_goals FROM game JOIN goal ON game.id = goal.matchid WHERE goal.teamid = 'FRA' GROUP BY game.id, game.mdate;

