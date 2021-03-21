-- *******************************************************
-- Team members:  Joshua Mckerracher & Andrew Friedrich 
-- Team name:  Buggy_debuggers
-- Team name:  Group 13
-- Project Title: Backlog Podcast Game Tracking Database 
-- new
-- https://thebacklog340.herokuapp.com/home
-- ******************************************************** 


drop table if exists `podcastEpisode`;
drop table if exists `gameGenre`;
drop table if exists `distributionPlatform`;
drop table if exists `game`;
drop table if exists `gameGenre`;
drop table if exists `gameCreator`;
drop table if exists `distributionPlatFKzz`;
drop table if exists `platformFKzz`;

-- Create podcastEpisode Table

CREATE TABLE IF NOT EXISTS podcastEpisode (
    `episodeNumber` int(5) not null unique auto_increment,
    `title` VARCHAR(255) CHARACTER SET utf8 not null,
    `episodeDate` DATE not null,
	primary key (`episodeNumber`)
);

-- Create list of podcasts inserted into podcastEpisode

INSERT INTO podcastEpisode VALUES
    (1001,'Episode 1 - Star Wars: TIE Fighter','2017-07-30'),
    (1002,'Episode 2 - Starcraft Remastered','2017-08-06'),
    (1003,'Episode 3 - Bethesda-sode!','2017-08-15'),
    (1004,'Episode 4 - Ninja Gaiden II','2017-08-29'),
    (1005,'Episode 5 - Gamer Court!','2017-10-02'),
    (1006,'Episode 6 - Are Loot Boxes Evil?','2017-10-10'),
    (1007,'Episode 7 - Game Mods, New Releases and More!','2017-10-24'),
    (1008,'Episode 8 - How GOOD was Star Wars ACTUALLY?','2017-10-31'),
    (1009,'Episode 9 - Tech & Mech Talk Megasode','2017-11-01'),
    (1010,'Episode 10 - Is Piracy Dead?','2017-11-28'),
    (1011,'Episode 11 - Worst Year in Gaming EVER?!','2017-12-29'),
    (1012,'Episode 12 - CO-OPISODE!','2017-12-30'),
    (1013,'Episode 13 - Anime Week!!! ','2018-02-08'),
    (1014,'Episode 14 - Mass Effect: Andromeda','2018-03-05');

-- Create gameGenre table

CREATE TABLE IF NOT EXISTS gameGenre (
    `idGenre` INT(5) not null unique auto_increment,
    `nameGenre` VARCHAR(255) CHARACTER SET utf8 not null,
	primary key (`idGenre`)
);

-- Create list of game genres 

INSERT INTO gameGenre VALUES
    (1001,'Real Time Strategy (RTS)'),
    (1002,'Role-Playing (RPG)'),
    (1003,'Shooter'),
    (1004,'Sport'),
    (1005,'Adventure'),
    (1006,'Turn Based Strategy (TBS)'),
    (1007,'Hack and Slash'),
    (1008,'Arcade'),
    (1009,'Simulator'),
    (1010,'Pinball'),
    (1011,'Puzzle'),
    (1012,'Racing'),
    (1013,'Pinball'),
    (1014,'Platform'),
    (1015,'MOBA'),
    (1016,'Fighting');

-- Create gameCreator table

CREATE TABLE IF NOT EXISTS gameCreator (
    `idCreator` int(5) Not Null auto_increment unique,
    `nameCreator` VARCHAR(255) CHARACTER SET utf8 Not null,
	primary key (`idCreator`)
);

-- create list of game creators

INSERT INTO gameCreator VALUES
    (1001,'LucasArts'),
    (1002,'Activision/Blizzard'),
    (1003,'ElectronicArts (EA)'),
    (1004,'Capcom'),
    (1005,'Konami '),
    (1006,'Microsoft'),
    (1007,'Bungie'),
    (1008,'Sony'),
    (1009,'Bethesda'),
    (1010,'Bioware'),
    (1011,'CD Projekt'),
    (1012,'Paradox'),
    (1013,'The Coalition'),
    (1014,'343 Studios'),
    (1015,'Nintendo'),
    (1016,'Obsidian Entertainment');
		

-- create platform table

CREATE TABLE IF NOT EXISTS platform (
    `idPlatform` int(5) unique auto_increment not null,
    `namePlatform` VARCHAR(255) CHARACTER SET utf8 not null,
    `playedOnline` boolean default '0' not null,
    `multiPlat` boolean default '0' not null,
	primary key (`idPlatform`)
);

-- create list of platforms where 0 is considered "no" and 1 is considered "yes"

INSERT INTO platform VALUES
    (1001,'PC (Personal Computer)','1','1'),
    (1002,'MAC (Personal Computer, MAC compatible)','1','1'),
    (1003,'Xbox (Original Xbox)','1','1'),
    (1004,'Xbox360','1','1'),
    (1005,'XboxOne (Includes Xbox One S & Xbox One X)','1','1'),
    (1006,'XboxSeries (Includes Xbox Series S & Xbox Series X)','1','1'),
    (1007,'Playstation1','0','1'),
    (1008,'Playstation2','0','1'),
    (1009,'Playstation3','1','1'),
    (1010,'Playstation4','1','1'),
    (1011,'Playstation5','1','1'),
    (1012,'Nintendo64','0','0'),
    (1013,'NintendoGameCube','0','0'),
    (1014,'NintendoWii','1','0'),
    (1015,'NintendoWiiU','1','0'),
    (1016,'NintendoSwitch','1','0');

-- create game table - this is the main table which everything is connected to
-- MM many to many tables connected to game

CREATE TABLE IF NOT EXISTS game (
    `nameGame` VARCHAR(255) CHARACTER SET utf8 not null,
    `releaseDate` DATE not null,
    `cost` NUMERIC(5, 2) not null,
    `gameGenre` int(5),
    `gameCreator` int(5),
    `podcastEpisode` INT(5),
	primary key (`nameGame`),
	constraint foreign key (`podcastEpisode`) references `podcastEpisode` 
	(`episodeNumber`) on update cascade on delete cascade,
	constraint foreign key (`gameCreator`) references `gameCreator` 
	(`idCreator`) on update cascade on delete cascade,
	constraint foreign key (`gameGenre`) references `gameGenre` (`idGenre`) 
	on update cascade on delete cascade

);

-- create distributionPlatFKzz MM / M:M / many to many table connecting distributionPlatform and game 



-- create platformFKzz MM / M:M / many to many table connecting platform and game

create table platformFKzz (
    `nameGame` varchar(255),
    `idPlatform` int(5),  
    constraint `platform_game_pk` Primary KEY (`nameGame`, `idPlatform`),
    constraint `FK_game_02` foreign key (`nameGame`) references `game` (`nameGame`),
    constraint `FK_platform_02` foreign key(`idPlatform`) references `platform` (`idPlatform`)
);

-- create list of games - name / year / cost / gameGenre / gameCreator / podcastEpisode

INSERT INTO game VALUES
    ('StreetFighter4','1995-01-01',17.9,1016,1004,1001),
    ('TieFighter','1996-01-01',65.1,1009,1001,1001),
    ('StarCraftRemaster','1997-01-01',69.3,1001,1002,1002),
    ('ElderScrollsArena','1998-01-01',9.3,1002,1009,1003),
    ('ElderScrollsMorrowind','1999-01-01',31.5,1002,1009,1003),
    ('ElderScrollsOblivion','2000-01-01',9.5,1002,1009,1003),
    ('ElderScrollsSkyrim','2001-01-01',31.9,1002,1009,1003),
    ('Fallout3','2002-01-01',18.1,1002,1009,1003),
    ('Fallout4','2003-01-01',56.9,1002,1009,1003),
    ('Fallout76','2004-01-01',47.3,1002,1009,1003),
    ('NinjaGaiden2','2005-01-01',61.1,1007,1005,1004),
    ('DarkSouls','2006-01-01',29.7,1007,1005,1004),
    ('DemonSouls','2007-01-01',12,1007,1005,1005),
    ('Bloodborne','2008-01-01',1.6,1007,1005,1005),
    ('Darksiders','2009-01-01',32.7,1007,1005,1005),
    ('NinjaGaiden','2010-01-01',13.6,1007,1005,1005),
    ('DevilMayCry','2011-01-01',8.6,1007,1005,1005),
    ('SuperMeatBoy','2012-01-01',18.3,1005,1008,1005),
    ('Cuphead','2013-01-01',22.7,1005,1010,1005),
    ('BattleblockTheater','2014-01-01',36.2,1005,1010,1005),
    ('SuperMarioBrothers','2015-01-01',15.3,1005,1012,1005),
    ('Sonic','2016-01-01',58.8,1005,1015,1005),
    ('RogueLegacy','2017-01-01',40.6,1005,1012,1005),
    ('WorldOfWarcraft','2017-01-01',28.6,1002,1002,1006),
    ('GearsOfWar','2017-01-01',12.6,1003,1013,1006),
    ('SouthParkFracturedButWhole','2017-01-01',14.9,1005,1003,1006),
    ('LordOfTheRingsShadowOfWar','1995-01-01',52,1001,1003,1006),
    ('CommandAndConquerRenegade','1996-01-01',53.5,1001,1003,1007),
    ('MassEffectAndromeda','1997-01-01',21.2,1002,1003,1014),
    ('Wolfenstein2','1998-01-01',42,1003,1009,1007),
    ('AssassinsCreed','1999-01-01',16.5,1004,1014,1007),
    ('StarWarsArcade','2000-01-01',0.7,1016,1015,1007),
    ('TitanFall','2001-01-01',50.1,1009,1003,1007),
    ('ElderScrollsOnline','2002-01-01',27.1,1002,1006,1007),
    ('GatlingGears','2003-01-01',40.4,1003,1010,1008),
    ('StreetsOfRage','2004-01-01',6.3,1016,1016,1008),
    ('TalesFromTheBoarderlands','2005-01-01',27.9,1005,1015,1008),
    ('LifeIsStrange','2006-01-01',24.5,1005,1015,1008),
    ('TheDivision','2007-01-01',32.9,1005,1015,1008),
    ('RareReplay','2008-01-01',9.6,1005,1015,1008),
    ('HeroesOfMightAndMagic','2009-01-01',35.1,1006,1004,1009),
    ('RadiantSilvergun','2010-01-01',69.4,1003,1003,1009),
    ('HaloTheMasterChiefCollection','2011-01-01',43.5,1003,1002,1009),
    ('RocketLeague','2012-01-01',32.3,1012,1001,1009),
    ('StardustGalaxyWarriorsStellarClimax','2013-01-01',1.1,1008,1009,1010),
    ('Warhammer40KDawnOfWar','2014-01-01',12.8,1001,1008,1010),
    ('SinsOfASolarEmpire','2015-01-01',5.8,1001,1006,1010),
    ('DungeonsAndDragonsTowerOfDoom','2016-01-01',65.9,1007,1004,1010),
    ('DungeonsAndDragonsShadowsOverMysteria','2017-01-01',52.1,1007,1004,1011),
    ('MassEffect1','2018-01-01',1.5,1002,1003,1012),
    ('MassEffect2','2019-01-01',65,1002,1003,1013),
    ('MassEffect3','2020-01-01',19.2,1002,1003,1014);
	
	
-- Insert Many to many relationships into platformFKzz - idPlatform and nameGame
INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES(
	(SELECT idPlatform FROM platform WHERE (idPlatform) = 1001), 
	(SELECT nameGame FROM game WHERE nameGame LIKE "%StreetFighter4%")
	);
	
INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%TieFighter%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%StarCraftRemaster%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%ElderScrollsArena%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%ElderScrollsMorrowind%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%ElderScrollsOblivion%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%ElderScrollsSkyrim%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Fallout3%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Fallout4%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Fallout76%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Darksiders%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%DevilMayCry%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%SuperMeatBoy%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Cuphead%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%BattleblockTheater%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Sonic%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%RogueLegacy%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%WorldOfWarcraft%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%GearsOfWar%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%SouthParkFracturedButWhole%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%LordOfTheRingsShadowOfWar%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%CommandAndConquerRenegade%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%MassEffectAndromeda%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Wolfenstein2%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT 
nameGame FROM game WHERE nameGame LIKE "%AssassinsCreed%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%TitanFall%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%ElderScrollsOnline%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%GatlingGears%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%StreetsOfRage%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%TalesFromTheBoarderlands%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%LifeIsStrange%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%TheDivision%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%HeroesOfMightAndMagic%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%HaloTheMasterChiefCollection%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%RocketLeague%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%StardustGalaxyWarriorsStellarClimax%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Warhammer40KDawnOfWar%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%SinsOfASolarEmpire%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%DungeonsAndDragonsTowerOfDoom%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%DungeonsAndDragonsShadowsOverMysteria%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%MassEffect1%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%MassEffect2%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1001),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%MassEffect3%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1003),
 (SELECT nameGame FROM game WHERE nameGame LIKE "NinjaGaiden"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%StreetFighter4%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%NinjaGaiden2%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%DevilMayCry%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%SuperMeatBoy%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%BattleblockTheater%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Sonic%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%RogueLegacy%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%GearsOfWar%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%SouthParkFracturedButWhole%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%LordOfTheRingsShadowOfWar%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%AssassinsCreed%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%TalesFromTheBoarderlands%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%LifeIsStrange%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%TheDivision%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%RadiantSilvergun%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%MassEffect1%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%MassEffect2%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1004),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%MassEffect3%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Cuphead%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%GearsOfWar%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%MassEffectAndromeda%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Wolfenstein2%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%TitanFall%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%ElderScrollsOnline%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%GatlingGears%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%StreetsOfRage%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%RareReplay%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%HaloTheMasterChiefCollection%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%RocketLeague%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%StardustGalaxyWarriorsStellarClimax%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%DungeonsAndDragonsTowerOfDoom%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1005),
 (SELECT 
nameGame FROM game WHERE nameGame LIKE "%DungeonsAndDragonsShadowsOverMysteria%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%StreetFighter4%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%DarkSouls%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%DemonSouls%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Bloodborne%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%DevilMayCry%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%SuperMeatBoy%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%BattleblockTheater%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Sonic%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%RogueLegacy%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%SouthParkFracturedButWhole%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%LordOfTheRingsShadowOfWar%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%AssassinsCreed%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%TalesFromTheBoarderlands%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%LifeIsStrange%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%TheDivision%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%MassEffect2%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1009),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%MassEffect3%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1010),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%MassEffectAndromeda%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1010),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%Wolfenstein2%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1010),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%ElderScrollsOnline%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1010),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%RocketLeague%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1012),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%SuperMarioBrothers%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 
VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1013),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%SuperMarioBrothers%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 

VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1014),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%SuperMarioBrothers%"));

INSERT INTO platformFKzz(idPlatform, nameGame) 

VALUES((SELECT idPlatform FROM platform WHERE (idPlatform) = 1015),
 (SELECT nameGame FROM game WHERE nameGame LIKE "%SuperMarioBrothers%"));


