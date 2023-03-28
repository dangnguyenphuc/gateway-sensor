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
