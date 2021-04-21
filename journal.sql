CREATE TABLE `Entry` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `date` VARCHAR NOT NULL,
    `concept` TEXT NOT NULL, 
    `entry` TEXT NOT NULL, 
    `mood_id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);

CREATE TABLE `Mood` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`label`	TEXT NOT NULL
);

CREATE TABLE `Tag` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL
);

CREATE TABLE `entry_tag` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`tag_id`    INTEGER NOT NULL,
    `entry_id`  INTEGER NOT NULL,
    FOREIGN KEY(`tag_id`) REFERENCES `Tag`(`id`)
    FOREIGN KEY(`entry_id`) REFERENCES `Entry`(`id`)
);

INSERT INTO `Mood` VALUES (null, "Happy");
INSERT INTO `Mood` VALUES (null, "Excited");
INSERT INTO `Mood` VALUES (null, "Calm");
INSERT INTO `Mood` VALUES (null, "Content");
INSERT INTO `Mood` VALUES (null, "Relaxed");
INSERT INTO `Mood` VALUES (null, "Sad");
INSERT INTO `Mood` VALUES (null, "Nervous");
INSERT INTO `Mood` VALUES (null, "Upset");
INSERT INTO `Mood` VALUES (null, "Tense");
INSERT INTO `Mood` VALUES (null, "Whelmed");

INSERT INTO 'Entry' VALUES (null, "04-13-2021", "Search Terms are for nerds!", "word term animal entry mood search", 4);

SELECT * FROM 'Entry'

INSERT INTO 'Tag' VALUES(null, "Soft-skills")

SELECT * FROM 'Tag'

INSERT INTO 'Entry_tag' VALUES(null, 1, 4)

SELECT * FROM 'Entry_tag'

SELECT
    e.id,
    e.date,
    e.concept,
    e.entry,
    e.mood_id, 
    m.label,
    t.name
FROM entry e
JOIN mood m
    ON m.id = e.mood_id
JOIN entry_tag et
    ON et.entry_id = e.id
JOIN tag t
    ON t.id = et.tag_id

SELECT
    et.id,
    et.tag_id,
    et.entry_id
FROM entry_tag et
    WHERE et.entry_id = 5
    


SELECT 
    et.id,
    et.entry_id,
    et.tag_id,
    t.id,
    t.name
FROM entry_tag et
JOIN tag t
    ON t.id = et.tag_id
WHERE et.entry_id = 5

SELECT 
    et.id,
    et.entry_id,
    et.tag_id,
    t.name
FROM entry_tag et
JOIN tag t
    ON t.id = et.tag_id
WHERE et.entry_id = 2

