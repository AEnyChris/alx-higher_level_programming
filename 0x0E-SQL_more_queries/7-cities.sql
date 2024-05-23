-- create database and table with auto generated and unique id--

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY (id),
	FORIEGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
