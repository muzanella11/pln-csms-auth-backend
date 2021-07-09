# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.31)
# Database: pln_csms_auth
# Generation Time: 2021-07-09 17:34:51 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table identity_types
# ------------------------------------------------------------

DROP TABLE IF EXISTS `identity_types`;

CREATE TABLE `identity_types` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `label` varchar(100) DEFAULT NULL,
  `description` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `identity_types` WRITE;
/*!40000 ALTER TABLE `identity_types` DISABLE KEYS */;

INSERT INTO `identity_types` (`id`, `name`, `label`, `description`, `created_at`, `updated_at`)
VALUES
	(1,'ktp','Kartu Tanda Penduduk','Kartu Tanda Penduduk','2021-07-05 21:11:48','2021-07-05 21:12:07');

/*!40000 ALTER TABLE `identity_types` ENABLE KEYS */;
UNLOCK TABLES;


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
  `privilege_type` int(10) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;

INSERT INTO `user_roles` (`id`, `name`, `label`, `privilege_type`, `created_at`, `updated_at`)
VALUES
	(1,'super-admin','Super Admin',1,'2021-07-05 19:03:14','2021-07-05 19:06:58'),
	(2,'admin','Admin',2,'2021-07-05 19:03:38','2021-07-05 19:06:58'),
	(3,'staff','Staff',3,'2021-07-05 19:04:03','2021-07-05 19:06:58'),
	(4,'user','User',4,'2021-07-05 19:04:11','2021-07-05 19:06:58');

/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table user_session
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user_session`;

CREATE TABLE `user_session` (
  `id` int(100) unsigned NOT NULL AUTO_INCREMENT,
  `token` text,
  `expired` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `user_session` WRITE;
/*!40000 ALTER TABLE `user_session` DISABLE KEYS */;

INSERT INTO `user_session` (`id`, `token`, `expired`, `created_at`, `updated_at`)
VALUES
	(19,'O9VW5848TEF-ZT3STDQBD4N-GWPNU8BBI5G-VDETZ4LVIPW-UUFYEUNYHKR-AVCSW6RK3ZY-D060IDAAUQQ-QV3Z5C7BLT8','1626023233000','2021-07-09 17:07:13','2021-07-09 17:07:13'),
	(20,'I8KPU3G5MPT-PJ4AQJBOODO-RIXWMKIWZXO-LZRNRT1GMK5-FR9ACWEGIYM-JCY1JFAX4WV-EKIS3X4LCA9-56GPZKCRXMA','1626024863000','2021-07-09 17:34:23','2021-07-09 17:34:23');

/*!40000 ALTER TABLE `user_session` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table users
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `fullname` varchar(50) DEFAULT NULL,
  `email` text,
  `password` text,
  `nip` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` int(1) DEFAULT NULL,
  `identity` varchar(50) DEFAULT NULL,
  `identity_type` int(10) DEFAULT NULL,
  `user_role` varchar(50) DEFAULT NULL,
  `address` text,
  `avatar` text,
  `session_token` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;

INSERT INTO `users` (`id`, `fullname`, `email`, `password`, `nip`, `dob`, `gender`, `identity`, `identity_type`, `user_role`, `address`, `avatar`, `session_token`, `created_at`, `updated_at`)
VALUES
	(1,'Super Admin','superadmin@gmail.com','gAAAAABg6H6Ig8OStTiqzWc9lOXUyAmPjNGdttpL_KQeO4JGLHnYCu2qtsfP8eY5Vfsu1CN4a1ER04kGmqYKNyavHhfnT_v5yQ==','123','1945-08-17',1,'12345678',1,'1','jalan mana aja','avatar','I8KPU3G5MPT-PJ4AQJBOODO-RIXWMKIWZXO-LZRNRT1GMK5-FR9ACWEGIYM-JCY1JFAX4WV-EKIS3X4LCA9-56GPZKCRXMA','2021-07-09 16:51:20','2021-07-09 17:34:23');

/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
