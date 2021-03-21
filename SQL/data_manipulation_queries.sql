-- *******************************************************
-- Team members:  Joshua Mckerracher & Andrew Friedrich 
-- Team name:  Buggy_debuggers
-- Team name:  Group 13
-- Project Title: Backlog Podcast Game Tracking Database 
-- https://thebacklog340.herokuapp.com/home
--
-- 
-- ************ Data Manipulation Queries *****************
-- ******************************************************** 

-- new
-- https://thebacklog340.herokuapp.com/home
-- SEARCH QUERY: 
SELECT * FROM game WHERE nameGame LIKE "%:search_value%"

-- ADD QUERY:
-- EXAMPLE: INSERT INTO game(nameGame, releaseDate, cost, episodeNumber, idGenre, idCreator)
-- VALUES
-- (
-- 'YOURGAMENAME HERE', 'DATE_HERE 2021-01-01', COSTHERE, 1001, 1001, 1001);
INSERT INTO game(nameGame, releaseDate, cost, gameGenre, gameCreator, podcastEpisode)
VALUES
(':input', ':input', :input, :input, :input, :input);

-- if episode will be NULL
-- EXAMPLE: INSERT INTO game(nameGame, releaseDate, cost, episodeNumber, idGenre, idCreator)
-- VALUES
-- (
-- 'YOURGAMENAME HERE', 'DATE_HERE 2021-01-01', COSTHERE, 1001, 1001, 1001);
INSERT INTO game(nameGame, releaseDate, cost, gameGenre, gameCreator)
VALUES
(':input', ':input', :input, :input, :input);

-- REMOVE QUERY:
-- EXAMPLE: if you're deleting the TieFighter game:
-- DELETE FROM platformFKzz WHERE nameGame LIKE "%TieFighter%";
-- DELETE FROM distributionPlatFKzz WHERE nameGame LIKE "%TieFighter%"
-- DELETE FROM game WHERE nameGame LIKE "%TieFighter%";
DELETE FROM platformFKzz WHERE nameGame LIKE "%:input%";
DELETE FROM distributionPlatFKzz WHERE nameGame LIKE "%:input%"
DELETE FROM game WHERE nameGame LIKE "%:input%";

-- EDIT QUERY:
UPDATE game SET 
nameGame = ":entered_val", releaseDate = ":entered_date", cost = :entered_cost, 
gameGenre = (SELECT idGenre FROM gameGenre WHERE nameGenre LIKE "%:entered_val%"), 
gameCreator = (SELECT idCreator FROM gameCreator WHERE nameCreator LIKE "%:entered_val%"), 
podcastEpisode = (SELECT episodeNumber FROM podcastEpisode WHERE title LIKE "%:entered_val%") 
WHERE nameGame = ":entered_value";





-- https://thebacklog340.herokuapp.com/gamegenres
-- SEARCH QUERY:
SELECT * FROM gameGenre where nameGenre LIKE "%:search_inputs%";

-- ADD QUERY:
INSERT INTO gameGenre (nameGenre) VALUES (:entered_value);

-- REMOVE QUERY:
DELETE FROM gameGenre WHERE nameGenre LIKE "%:entered_value%";

-- EDIT QUERY:
UPDATE gameGenre SET nameGenre = ":entered_value" WHERE nameGenre LIKE "%:entered_value%";





-- https://thebacklog340.herokuapp.com/gamecreators
-- SEARCH QUERY:
SELECT * FROM gameCreator WHERE nameCreator LIKE "%:search_value%";

-- ADD QUERY:
INSERT INTO gameCreator (nameCreator) VALUES (:entered_value);

-- REMOVE QUERY:
DELETE FROM gameCreator WHERE nameCreator LIKE "%:entered_value%";

-- EDIT QUERY:
UPDATE gameCreator SET nameCreator = ":entered_value" WHERE nameCreator LIKE "%:entered_value%";





-- https://thebacklog340.herokuapp.com/platforms
-- SEARCH QUERY:
SELECT * FROM platform WHERE namePlatform LIKE "%:entered_value%"

-- ADD QUERY:
INSERT INTO platform (namePlatform, playedOnline, multiPlat)
VALUES (':entered_val', ’:entered_val’, :’entered_val’)

-- REMOVE QUERY:  
DELETE FROM platform WHERE namePlatform LIKE "%:entered_value%";

-- EDIT QUERY:
UPDATE platform SET namePlatform = ":entered_value", playedOnline = :entered_number, multiPlat=:entered_number WHERE namePlatform LIKE "%:entered_value%";





-- https://thebacklog340.herokuapp.com/podcastepisodes
-- SEARCH QUERY:
SELECT * FROM podcastEpisode WHERE title LIKE "%:entered_value%"

-- ADD QUERY:
INSERT INTO podcastEpisode(title, episodeDate) VALUES (‘:entered_title’, ‘:entered_date’)

-- REMOVE QUERY:
DELETE FROM podcastEpisode WHERE title LIKE “%:entered_title%”

-- EDIT QUERY:
UPDATE podcastEpisode SET title = “:entered_title”, episodeDate = “:entered_date” WHERE title LIKE “%:entered_title%”





-- https://thebacklog340.herokuapp.com/distributionplatforms
-- SEARCH QUERY:
SELECT * FROM distributionPlatform WHERE nameDistrib LIKE "%:entered_value%"

-- ADD QUERY:
INSERT INTO distributionPlatform(nameDistrib, platformRel) VALUES (‘:entered_value’, ‘:entered_date’)

-- REMOVE QUERY:
DELETE FROM distributionPlatform WHERE nameDistrib LIKE “%:entered_value%

-- EDIT QUERY:
UPDATE distributionPlatform SET nameDistrib = “:entered_name”, platformRel = “:entered_date” WHERE nameDistrib LIKE “%:entered_value%”





-- https://thebacklog340.herokuapp.com/gamesandplatforms
-- SEARCH QUERY:
SELECT * FROM platformFKzz WHERE nameGame LIKE "%:entered_value%";

-- ADD QUERY:
INSERT INTO platformFKzz(idPlatform, nameGame)
VALUES
(
(SELECT idPlatform FROM platform WHERE namePlatform LIKE "%:entered_value%"), 
(SELECT nameGame FROM game WHERE nameGame LIKE "%:entered_value%")
); 

-- REMOVE QUERY:
DELETE FROM platformFKzz WHERE nameGame LIKE "%:entered_value%";

-- EDIT QUERY:
UPDATE platformFKzz 
SET
nameGame = (SELECT nameGame FROM game WHERE nameGame LIKE "%:entered_value%"), 
idPlatform = (SELECT idPlatform FROM platform WHERE namePlatform LIKE "%:entered_value%") 
WHERE nameGame LIKE “%:entered_value%”;






-- https://thebacklog340.herokuapp.com/gamesanddistributionplatforms
-- SEARCH QUERY:
SELECT * FROM distributionPlatFKzz WHERE nameGame LIKE "%:entered_value%";

-- ADD QUERY:
INSERT INTO distributionPlatFKzz (idDistribPlat, nameGame)
VALUES
((SELECT idDistribPlat FROM distributionPlatform WHERE nameDistrib LIKE "%:entered_val%"), 
(SELECT nameGame FROM game WHERE nameGame LIKE "%:entered_val%"));

-- REMOVE QUERY:
DELETE FROM distributionPlatFKzz WHERE nameGame LIKE "%:entered_value%";

-- EDIT QUERY:
UPDATE distributionPlatFKzz
SET 
nameGame = (SELECT nameGame FROM game WHERE nameGame LIKE "%:entered_value%"), 
idDistribPlat = (SELECT idPlatform FROM platform WHERE namePlatform LIKE "%:entered_val%") 
WHERE nameGame LIKE “%:entered_value%”;





-- https://thebacklog340.herokuapp.com/search
-- If Game Name is selected:
SELECT * FROM game WHERE nameGame = ":selection"

-- If Game Genre is selected:
SELECT * FROM gameGenre WHERE nameGenre = ":selection"

-- If Game Creator is selected:
SELECT * FROM gameCreator WHERE nameCreator = ":selection"

-- If Platform is selected:
SELECT * FROM platform WHERE namePlatform = ":selection"

-- If Distribution Platform is selected:
SELECT * FROM distributionPlatform WHERE nameDistrib = ":selection"

-- If Podcast Episode is selected:
SELECT * FROM podcastEpisode WHERE title = ":selection"



-- ********* TWO DROPDOWNS USED *********
-- If Game Name and Game Genre is selected:
SELECT * FROM game INNER JOIN gameGenre ON game.gameGenre = gameGenre.idGenre;

-- Any two dropdowns X and Y selected:
SELECT * FROM X INNER JOIN Y ON X.attribute = Y.attribute;



-- ********* THREE DROPDOWNS USED *********
-- (Game, gameGenre, and gameCreator dropdowns used)
SELECT * FROM game, gameGenre, gameCreator
  WHERE
  game.nameGame = ":selection"
  AND
  gameGenre.nameGenre = ":selection"
  AND
  gameCreator.nameCreator = ":selection"

 -- Any three dropdowns X, Y, and Z selected:
SELECT * FROM X, Y, Z
  WHERE
  X.attribute = ":selection"
  AND
  Y.attribute = ":selection"
  AND
  Z.attribute = ":selection"


-- ********* ANY FOUR DROPDOWNS USED *********
SELECT * FROM A, B, C, D
  WHERE
  A.attribute = ":selection"
  AND
  B.attribute = ":selection"
  AND
  C.attribute = ":selection"
  AND
  D.attribute = ":selection"


-- ********* ANY FIVE DROPDOWNS USED *********
SELECT * FROM A, B, C, D, E
  WHERE
  A.attribute = ":selection"
  AND
  B.attribute = ":selection"
  AND
  C.attribute = ":selection"
  AND
  D.attribute = ":selection"
  AND
  E.attribute = ":selection"


-- ********* ANY SIX DROPDOWNS USED *********
SELECT * FROM A, B, C, D, E, F
  WHERE
  A.attribute = ":selection"
  AND
  B.attribute = ":selection"
  AND
  C.attribute = ":selection"
  AND
  D.attribute = ":selection"
  AND
  E.attribute = ":selection"
  AND
  F.attribute = ":selection"


