CREATE TABLE IF NOT EXISTS chat_triggers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  trigger TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS chat_responses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  response TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS chat_triggers_responses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  triggerId INTEGER NOT NULL,
  responseId INTEGER NOT NULL,
  FOREIGN KEY(triggerId) REFERENCES chat_triggers(id),
  FOREIGN KEY(responseId) REFERENCES chat_responses(id)
);

CREATE VIEW IF NOT EXISTS chat_all AS
SELECT chat_triggers.id as trigger_id, trigger, response
FROM chat_triggers
INNER JOIN chat_triggers_responses ON chat_triggers.id = chat_triggers_responses.triggerId
INNER JOIN chat_responses ON chat_responses.id = chat_triggers_responses.responseId;

CREATE TABLE IF NOT EXISTS bot (
  id INTEGER PRIMARY KEY,
  setting INTEGER NOT NULL,
  FOREIGN KEY(setting) REFERENCES bot_settings(id)
);

CREATE TABLE IF NOT EXISTS bot_settings (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  voice_name TEXT NOT NULL,
  language TEXT NOT NULL,
  gender TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS translation_voices (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  language TEXT NOT NULL
);

INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (1, "Salli", "en-US", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (2, "Joey", "en-US", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (3, "Naja", "da-DK", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (4, "Mads", "da-DK", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (5, "Marlene", "de-DE", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (6, "Hans", "de-DE", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (7, "Nicole", "en-AU", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (8, "Russell", "en-AU", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (9, "Amy", "en-GB", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (10, "Brian", "en-GB", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (11, "Emma", "en-GB", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (12, "Gwyneth", "en-GB-WLS", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (13, "Geraint", "en-GB-WLS", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (14, "Gwyneth", "cy-GB", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (15, "Geraint", "cy-GB", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (16, "Raveena", "en-IN", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (17, "Chipmunk", "en-US", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (18, "Eric", "en-US", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (19, "Ivy", "en-US", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (20, "Jennifer", "en-US", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (21, "Justin", "en-US", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (22, "Kendra", "en-US", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (23, "Kimberly", "en-US", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (24, "Conchita", "es-ES", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (25, "Enrique", "es-ES", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (26, "Penelope", "es-US", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (27, "Miguel", "es-US", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (28, "Chantal", "fr-CA", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (29, "Celine", "fr-FR", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (30, "Mathieu", "fr-FR", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (31, "Dora", "is-IS", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (32, "Karl", "is-IS", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (33, "Carla", "it-IT", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (34, "Giorgio", "it-IT", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (35, "Liv", "nb-NO", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (36, "Lotte", "nl-NL", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (37, "Ruben", "nl-NL", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (38, "Agnieszka", "pl-PL", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (39, "Jacek", "pl-PL", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (40, "Ewa", "pl-PL", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (41, "Jan", "pl-PL", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (42, "Maja", "pl-PL", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (43, "Vitoria", "pt-BR", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (44, "Ricardo", "pt-BR", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (45, "Cristiano", "pt-PT", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (46, "Ines", "pt-PT", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (47, "Carmen", "ro-RO", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (48, "Maxim", "ru-RU", "Male");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (49, "Tatyana", "ru-RU", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (50, "Astrid", "sv-SE", "Female");
INSERT OR IGNORE INTO bot_settings (id,  voice_name,  language,  gender) VALUES (51, "Filiz", "tr-TR", "Female");

INSERT OR IGNORE INTO bot (id,  setting) VALUES (1, 10);

INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (1, "Danish");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (2, "Dutch");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (3, "English");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (4, "French");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (5, "German");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (6, "Icelandic");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (7, "Italian");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (8, "Norwegian");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (9, "Polish");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (10, "Portuguese");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (11, "Romanian");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (12, "Russian");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (13, "Spanish");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (14, "Swedish");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (15, "Turkish");
INSERT OR IGNORE INTO translation_voices (id,  language) VALUES (16, "Welsh");
