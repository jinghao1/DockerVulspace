CREATE DATABASE IF NOT EXISTS mysite CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
use mysite;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for muser
-- ----------------------------
DROP TABLE IF EXISTS `muser`;
CREATE TABLE `muser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of muser
-- ----------------------------
BEGIN;
INSERT INTO `muser` VALUES (1, 'song', '17703186691');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;

CREATE USER IF NOT EXISTS 'mysiteuser'@'%' IDENTIFIED BY 'mysitepass';
GRANT ALL PRIVILEGES ON mysite.* TO 'mysiteuser'@'%';

FLUSH PRIVILEGES;
