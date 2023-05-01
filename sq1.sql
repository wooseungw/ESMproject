CREATE TABLE tuser (
 p_id        INT NOT NULL AUTO_INCREMENT,
 us_id     VARCHAR(20) NOT null,
 us_pw     VARCHAR(20) NOT null,
 us_api    VARCHAR(64) not null,
 
  PRIMARY KEY(p_id)
) ENGINE=InnoDB CHARSET=utf8;

CREATE TABLE tinput (
 
 i_id        	INT NOT NULL AUTO_INCREMENT  ,
 p_id        INT NOT NULL,
 in_fname		varchar(30),
 in_ftype		varchar(6),
 in_contents    LONGTEXT not null,
 in_date		date,
 PRIMARY KEY(i_id),
 FOREIGN KEY (p_id) REFERENCES tuser (p_id)
 
) ENGINE=InnoDB CHARSET=utf8;


CREATE TABLE tsummary (

 s_id        	INT NOT NULL AUTO_INCREMENT,
 su_impwords	text,
 su_contents    MEDIUMTEXT not null,
 
 
  PRIMARY KEY(s_id)
) ENGINE=InnoDB CHARSET=utf8;

CREATE TABLE textent (

 e_id        	INT NOT NULL AUTO_INCREMENT,
 
 ex_contents    LONGTEXT not null,
 
 
  PRIMARY KEY(e_id)
) ENGINE=InnoDB CHARSET=utf8;

CREATE TABLE tword (

 w_id        	INT NOT NULL AUTO_INCREMENT,
 w_name			text not null,
 w_contents   	MEDIUMTEXT not null,
 
 
  PRIMARY KEY(w_id)
) ENGINE=InnoDB CHARSET=utf8;


