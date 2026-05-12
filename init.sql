CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO users (username, email) VALUES ('Artur', 'artur@kazan-engineer.ru')
ON CONFLICT DO NOTHING;