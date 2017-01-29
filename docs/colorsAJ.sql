/*
 Navicat Premium Data Transfer

 Source Server         : Local
 Source Server Type    : MySQL
 Source Server Version : 50521
 Source Host           : localhost
 Source Database       : test

 Target Server Type    : MySQL
 Target Server Version : 50521
 File Encoding         : utf-8

 Date: 01/28/2017 17:43:18 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `colorsAJ`
-- ----------------------------
DROP TABLE IF EXISTS `colorsAJ`;
CREATE TABLE `colorsAJ` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `red` int(11) NOT NULL,
  `green` int(11) NOT NULL,
  `blue` int(11) NOT NULL,
  `dmc` varchar(10) NOT NULL,
  `description` varchar(25) NOT NULL,
  `rgb` varchar(6) NOT NULL,
  `row` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

SET FOREIGN_KEY_CHECKS = 1;
