USE unikovka;

-- ============================
-- 1) TEAMS
-- ============================
INSERT INTO teams (name, email, players) VALUES
('Riddle Masters', 'riddlemasters@example.com', 4),
('Escape Squad', 'escapesquad@example.com', 5),
('Brain Breakers', 'brainbreakers@example.com', 3),
('Mystery Hunters', 'mysteryhunters@example.com', 6),
('Puzzle Force', 'puzzleforce@example.com', 2),
('Key Seekers', 'keyseekers@example.com', 4);

-- ============================
-- 2) ROOMS
-- ============================
INSERT INTO rooms (name, capacity, notes) VALUES
('Horror Cellar', 6, 'Temná atmosféra'),
('Space Lab', 5, 'Sci-fi prostředí'),
('Ancient Tomb', 8, 'Bezbarierový přístup'),
('Detective Office', 4, 'Retro styl'),
('Time Machine', 6, NULL);

-- ============================
-- 3) GAMES
-- ============================
INSERT INTO games (name, difficulty, max_players, time, theme, teams_id, rooms_id) VALUES
('The Lost Soul', 4, 6, 60, 'Horror', 1, 1),
('Galactic Escape', 3, 5, 45, 'Sci-fi', 2, 2),
('Pharaoh’s Curse', 5, 8, 75, 'History', 3, 3),
('Murder Mystery', 2, 4, 50, 'Detective', 4, 4),
('Chrono Escape', 3, 6, 60, 'Time Travel', 5, 5),
('Alien Containment', 4, 5, 55, 'Sci-fi', 6, 2),
('Secret Archives', 1, 4, 40, 'Detective', 1, 4);

-- ============================
-- 4) VOTING
-- ============================
INSERT INTO voting (star, notes) VALUES
(5, 'Skvělá atmosféra!'),
(4, 'Trochu těžké, ale super.'),
(3, 'Průměrné, čekal jsem víc.'),
(5, 'Perfektní zážitek.'),
(2, 'Příliš složité úkoly.'),
(4, 'Dobrá hra, doporučuji.'),
(1, 'Nefunkční rekvizity.'),
(5, 'Top hra!'),
(3, 'Fajn, ale nic extra.'),
(4, 'Zábavné a napínavé.');

-- ============================
-- 5) TRIES
-- ============================
INSERT INTO tries (date, time, sucess, teams_id, voting_id, games_id) VALUES
('2026-04-01 14:00:00', 52, 1, 1, 1, 1),
('2026-04-02 16:30:00', 47, 1, 2, 2, 2),
('2026-04-03 18:00:00', 60, 0, 3, 3, 3),
('2026-04-04 13:15:00', 45, 1, 4, 4, 4),
('2026-04-05 17:20:00', 70, 0, 5, 5, 3),
('2026-04-06 15:10:00', 50, 1, 6, 6, 5),
('2026-04-07 19:00:00', 55, 0, 1, 7, 6),
('2026-04-08 12:45:00', 40, 1, 2, 8, 7),
('2026-04-09 14:30:00', 62, 0, 3, 9, 1),
('2026-04-10 16:00:00', 48, 1, 4, 10, 2);
