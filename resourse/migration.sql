-- Создание таблицы пользователей
CREATE TABLE users (
                       user_id SERIAL PRIMARY KEY,
                       username VARCHAR(255) UNIQUE NOT NULL,
                       password VARCHAR(255) NOT NULL,
                       display_name VARCHAR(255) NOT NULL,
                       avatar_choice INTEGER NOT NULL
);

-- Создание таблицы сообщений
CREATE TABLE messages (
                          message_id SERIAL PRIMARY KEY,
                          sender_id INTEGER REFERENCES users(user_id),
                          receiver_id INTEGER REFERENCES users(user_id),
                          content VARCHAR(255) NOT NULL,
                          timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                          is_encrypted BOOLEAN DEFAULT FALSE
);

-- Создание таблицы ключей
CREATE TABLE keys (
                      key_id SERIAL PRIMARY KEY,
                      user_id INTEGER REFERENCES users(user_id),
                      key_value VARCHAR(255) NOT NULL,
                      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);