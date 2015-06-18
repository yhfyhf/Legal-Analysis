CREATE DATABASE if not exists legal DEFAULT CHARSET=utf8;
USE legal;
CREATE TABLE if not exists `judgement` (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `url` varchar(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `time` varchar(20) DEFAULT NULL,
  `court` varchar(100) DEFAULT NULL,
  `content` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE if not exists `error` (
  `id` int(8) NOT NULL AUTO_INCREMENT,
  `message` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;