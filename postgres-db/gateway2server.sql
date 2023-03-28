-- Table: public.feed

-- DROP TABLE IF EXISTS public.feed;

CREATE TABLE IF NOT EXISTS public.feed
(
    id integer NOT NULL DEFAULT nextval('feed_id_seq'::regclass),
    feed_name character varying(15) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT feed_pkey PRIMARY KEY (id),
    CONSTRAINT feed_feed_name_key UNIQUE (feed_name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.feed
    OWNER to postgres;

-- Table: public.feed_value

-- DROP TABLE IF EXISTS public.feed_value;

CREATE TABLE IF NOT EXISTS public.feed_value
(
    feed_name character varying(10) COLLATE pg_catalog."default" NOT NULL,
    "timestamp" time without time zone NOT NULL,
    value character varying(5) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT feed_value_pkey PRIMARY KEY (feed_name, "timestamp"),
    CONSTRAINT feed_value_timestamp_feed_name_key UNIQUE ("timestamp", feed_name),
    CONSTRAINT feed_value_feed_name_fkey FOREIGN KEY (feed_name)
        REFERENCES public.feed (feed_name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.feed_value
    OWNER to postgres;

INSERT INTO feed (feed_name) VALUES ('sensor1');
INSERT INTO feed (feed_name) VALUES ('sensor2');
INSERT INTO feed (feed_name) VALUES ('button1');
INSERT INTO feed (feed_name) VALUES ('button2');
INSERT INTO feed (feed_name) VALUES ('FanValue');
INSERT INTO feed (feed_name) VALUES ('LightValue');
INSERT INTO feed (feed_name) VALUES ('FanDisplay');
INSERT INTO feed (feed_name) VALUES ('LightDisplay');

-- DELETE FROM feed_value; 
