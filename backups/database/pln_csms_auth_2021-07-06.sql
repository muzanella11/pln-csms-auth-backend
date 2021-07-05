# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.31)
# Database: pln_csms_auth
# Generation Time: 2021-07-05 19:16:09 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table privilege_types
# ------------------------------------------------------------

DROP TABLE IF EXISTS `privilege_types`;

CREATE TABLE `privilege_types` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `label` varchar(100) DEFAULT NULL,
  `description` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `privilege_types` WRITE;
/*!40000 ALTER TABLE `privilege_types` DISABLE KEYS */;

INSERT INTO `privilege_types` (`id`, `name`, `label`, `description`, `created_at`, `updated_at`)
VALUES
	(1,'super-admin','Super Admin','Untuk privilege super admin','2021-07-05 18:08:02',NULL),
	(2,'admin','Admin','Untuk privilege admin','2021-07-05 18:08:26',NULL),
	(3,'staff','Staff','Untuk privilege staff','2021-07-05 18:08:55',NULL),
	(4,'user','User','Untuk privilege user','2021-07-05 18:09:31',NULL);

/*!40000 ALTER TABLE `privilege_types` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table user_roles
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_roles`;

CREATE TABLE `user_roles` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `label` varchar(50) DEFAULT NULL,
  `privilege_type` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;

INSERT INTO `user_roles` (`id`, `name`, `label`, `privilege_type`, `created_at`, `updated_at`)
VALUES
	(1,'super-admin','Super Admin','1','2021-07-05 19:03:14','2021-07-05 19:06:58'),
	(2,'admin','Admin','2','2021-07-05 19:03:38','2021-07-05 19:06:58'),
	(3,'staff','Staff','3','2021-07-05 19:04:03','2021-07-05 19:06:58'),
	(4,'user','User','4','2021-07-05 19:04:11','2021-07-05 19:06:58');

/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
