SELECT fname, lname, name
FROM scientist, field
WHERE scientist.field_id = field.id;

SELECT discovery.name, field.name
FROM discovery, scientist, scientist_has_discovery, field
WHERE discovery.id = scientist_has_discovery.discovery_id
  AND scientist.id = scientist_has_discovery.scientist_id
  AND scientist.field_id = field.id
  AND field.name = 'Artificial Intelligence';

SELECT fname, lname, discovery.name
FROM scientist, discovery, scientist_has_discovery
WHERE scientist.id = scientist_has_discovery.scientist_id
  AND discovery.id = scientist_has_discovery.discovery_id;

SELECT lname, COUNT(*)
FROM scientist_has_discovery, scientist
WHERE scientist.id = scientist_has_discovery.scientist_id
GROUP BY lname;

SELECT fname , lname
FROM scientist
WHERE dday IS NULL;
