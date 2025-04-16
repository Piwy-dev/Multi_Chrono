CREATE TABLE IF NOT EXISTS timer(
    minutes INTEGER NOT NULL,
    seconds INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS teams (
    initial_minutes INTEGER NOT NULL,
    initial_seconds INTEGER NOT NULL,
    team_name TEXT NOT NULL,
    start_time TIMESTAMP NOT NULL,
    started BOOLEAN NOT NULL
);