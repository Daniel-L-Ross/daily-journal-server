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