USE unikovka;

-- ============================================
-- 1) SELECT
-- ============================================

SELECT * FROM teams;

SELECT * FROM games
WHERE difficulty > 3;

SELECT * FROM rooms
WHERE capacity >= 6;

SELECT * FROM tries
WHERE sucess = 1;

SELECT * FROM voting
WHERE notes LIKE '%super%';


-- ============================================
-- 2) INSERT
-- ============================================

INSERT INTO teams (name, email, players)
VALUES ('Shadow Breakers', 'shadow@example.com', 4);

INSERT INTO voting (star, notes) VALUES
(5, 'Výborná hra!'),
(3, 'Bylo to fajn, ale mohlo být lepší.');


-- ============================================
-- 3) UPDATE 
-- ============================================

UPDATE teams
SET players = 5
WHERE name = 'Puzzle Force';

UPDATE rooms
SET notes = 'Nově zrekonstruovaná místnost'
WHERE name = 'Detective Office';


-- ============================================
-- 4) DELETE
-- ============================================
DELETE FROM voting
WHERE star = 1;

DELETE FROM teams
WHERE name = 'Shadow Breakers';
