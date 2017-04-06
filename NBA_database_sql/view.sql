CREATE VIEW career AS
    SELECT 
        d.firstName,
        d.lastName,
        p.points / p.GP AS points,
        p.assists / p.GP AS assists,
        p.rebounds / p.GP AS rebounds,
        p.steals / p.GP AS steals,
        p.blocks / p.GP AS blocks
    FROM
        draft AS d,
        players AS p
    WHERE
        d.playerID = p.playerID
;

create view player_info as 
SELECT 
    d.firstName, d.lastName, p.points / p.GP AS points, p.year
FROM
    draft AS d,
    players AS p
WHERE
    d.playerID = p.playerID
ORDER BY p.year
;
