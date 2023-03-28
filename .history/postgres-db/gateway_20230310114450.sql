CREATE TABLE IF NOT EXISTS feed(
  id SERIAL NOT NULL PRIMARY KEY,
  feed_name VARCHAR(10) NOT NULL UNIQUE 
);

CREATE TABLE IF NOT EXISTS feed_value(
  feed_name VARCHAR(10) NOT NULL REFERENCES feed(feed_name),
  timestamp TIME NOT NULL,
  value VARCHAR(5) NOT NULL,
  PRIMARY KEY(feed_name, timestamp),
  UNIQUE (timestamp, feed_name)
);

INSERT INTO feed (feed_name) VALUES (sensor1);
INSERT INTO feed (feed_name) VALUES (sensor2);
INSERT INTO feed (feed_name) VALUES (button1);
INSERT INTO feed (feed_name) VALUES (button2);
INSERT INTO feed (feed_name) VALUES (FanValue);
INSERT INTO feed (feed_name) VALUES (LightValue);
INSERT INTO feed (feed_name) VALUES (FanDisplay);
INSERT INTO feed (feed_name) VALUES (LightDisplay);