-- create database and table with auto generated and unique id--
-- cities description:
-- 	  id INT unique, auto generated, can’t be null and is a primary key
--	  state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- 	  name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FORIEGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
