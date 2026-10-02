DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
	user_id INT PRIMARY KEY,
	username VARCHAR(50),
	bio TEXT,
	created_at DATETIME
);

CREATE TABLE posts (
	post_id INT PRIMARY KEY,
	content TEXT,
	created_at DATETIME,
	user_id INT,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- users
INSERT INTO users (user_id, username, bio, created_at)
VALUES (1, 'Linda', 'My hobby is running', '2026-11-13 12:00:00');

INSERT INTO users (user_id, username, bio, created_at)
VALUES (2, 'Joy', 'My hobby is photography', '2026-05-19 12:00:00');

INSERT INTO users (user_id, username, bio, created_at)
VALUES (3, 'Love', 'My hobby is pickleball', '2026-12-31 12:00:00');

INSERT INTO users (user_id, username, bio, created_at)
VALUES (4, 'Ava', 'My hobby is drawing', '2026-07-04 12:00:00');

INSERT INTO users (user_id, username, bio, created_at)
VALUES (5, 'Mariam', 'My hobby is going to concerts', '2026-01-05 12:00:00');

INSERT INTO users (user_id, username, bio, created_at)
VALUES (6, 'Clarke', 'My hobby is going to the gym', '2026-02-17 12:00:00');

INSERT INTO users (user_id, username, bio, created_at)
VALUES (7, 'Bri', 'My hobby is studying', '2026-02-11 12:00:00');

INSERT INTO users (user_id, username, bio, created_at)
VALUES (8, 'Sophea', 'My hobby is shopping', '2026-02-14 12:00:00');

INSERT INTO users (user_id, username, bio, created_at)
VALUES (9, 'Michele', 'My hobby is doing makeup', '2026-07-12 12:00:00');

INSERT INTO users (user_id, username, bio, created_at)
VALUES (10, 'Victoria', 'My hobby is vlogging', '2026-09-27 12:00:00');

-- posts
INSERT INTO posts (post_id, content, created_at, user_id)
VALUES (1, 'red', '2026-11-13 01:00:00', 1);

INSERT INTO posts (post_id, content, created_at, user_id)
VALUES (2, 'orange', '2026-05-17 02:00:00', 2);

INSERT INTO posts (post_id, content, created_at, user_id)
VALUES (3, 'yellow', '2026-12-31 03:00:00', 3);

INSERT INTO posts (post_id, content, created_at, user_id)
VALUES (4, 'green', '2026-07-04 04:00:00', 4);

INSERT INTO posts (post_id, content, created_at, user_id)
VALUES (5, 'blue', '2026-01-05 05:00:00', 5);

INSERT INTO posts (post_id, content, created_at, user_id)
VALUES (6, 'purple', '2026-02-17 06:00:00', 6);

INSERT INTO posts (post_id, content, created_at, user_id)
VALUES (7, 'pink', '2026-02-11 07:00:00', 7);

INSERT INTO posts (post_id, content, created_at, user_id)
VALUES (8, 'magenta', '2026-02-14 08:00:00', 8);

INSERT INTO posts (post_id, content, created_at, user_id)
VALUES (9, 'aquamarine', '2026-07-12 09:00:00', 9);

INSERT INTO posts (post_id, content, created_at, user_id)
VALUES (10, 'cyan', '2026-09-07 10:00:00', 10);
