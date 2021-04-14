CREATE TABLE `Entries` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `date` VARCHAR NOT NULL,
    `concept` TEXT NOT NULL, 
    `entry` TEXT NOT NULL, 
    `mood_id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);

CREATE TABLE `Moods` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`label`	TEXT NOT NULL
);

INSERT INTO `Moods` VALUES (null, "Happy");
INSERT INTO `Moods` VALUES (null, "Excited");
INSERT INTO `Moods` VALUES (null, "Calm");
INSERT INTO `Moods` VALUES (null, "Content");
INSERT INTO `Moods` VALUES (null, "Relaxed");
INSERT INTO `Moods` VALUES (null, "Sad");
INSERT INTO `Moods` VALUES (null, "Nervous");
INSERT INTO `Moods` VALUES (null, "Upset");
INSERT INTO `Moods` VALUES (null, "Tense");
INSERT INTO `Moods` VALUES (null, "Whelmed");

SELECT * FROM Moods;