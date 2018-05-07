CREATE DATABASE IF NOT EXISTS ad_info default charset utf8 COLLATE utf8_general_ci;

use ad_info;

CREATE TABLE IF NOT EXISTS `ad_info` (
      `ad_id`             INT(11) UNSIGNED         NOT NULL AUTO_INCREMENT                    COMMENT '自增id,广告id',
      `companyName`       VARCHAR(128)             NOT NULL                                   COMMENT '公司全称',
      `positionfullName`  VARCHAR(128)             NOT NULL                                   COMMENT '职位全称',
      `positionName`      VARCHAR(32)              NOT NULL                                   COMMENT '职位简称',
      `city`              VARCHAR(32)              NOT NULL                                   COMMENT '所在城市',
      `positionAdvantage` VARCHAR(512)             NOT NULL                                   COMMENT '公司福利',
      `salarymin`         INT(2)                   NOT NULL DEFAULT 0                         COMMENT '最低工资',
      `salarymax`         INT(2)                   NOT NULL DEFAULT 0                         COMMENT '工资上限',
      `workYear`          INT(2)                   NOT NULL DEFAULT 0                         COMMENT '工作年限',
      `request_url`       VARCHAR(128)             NOT NULL                                   COMMENT '跳转地址',
      `record_url`        VARCHAR(128)             NOT NULL DEFAULT '1'                       COMMENT '记录点击',
      `priority`          INT(2)                   NOT NULL DEFAULT 30                        COMMENT '优先级',
      `clk_id`            INT                      NOT NULL DEFAULT 0                         COMMENT '点击里路id',
      `ctime`             TIMESTAMP                NOT NULL DEFAULT CURRENT_TIMESTAMP         COMMENT '记录创建时间',
      `stime`             TIMESTAMP                NOT NULL DEFAULT '0000-00-00 00:00:00'     COMMENT '广告投放开始时间',
      `etime`             TIMESTAMP                NOT NULL DEFAULT '0000-00-00 00:00:00'     COMMENT '广告投放结束时间',
      PRIMARY KEY (`ad_id`),
      KEY `city` (`city`),
      KEY `posname` (`positionName`),
      KEY `salary` (`salarymin`, `salarymax`),
      KEY `year` (`workYear`),
      KEY `time` (`stime`, `etime`),
      KEY `priority` (`priority`),
      KEY `clk_id` (`clk_id`)
) ENGINE = InnoDB AUTO_INCREMENT = 10000 DEFAULT CHARSET = utf8;

CREATE TABLE IF NOT EXISTS `tbl_cpc_clk` (
    `id`                  INT(11) UNSIGNED        NOT NULL AUTO_INCREMENT                    COMMENT '自增id',
	  `ad_id`				        INT(11) UNSIGNED        NOT NULL DEFAULT 0                         COMMENT '广告id',
	  `num`                 INT(11) UNSIGNED        NOT NULL DEFAULT 0                         COMMENT '广告点击数',
	  `date`                DATE                    NOT NULL DEFAULT '0000-00-00'              COMMENT '日期',
	  `clk_id`              INT                     NOT NULL DEFAULT 0                         COMMENT '点击记录id',
	  PRIMARY KEY (`id`),
	  UNIQUE KEY (`ad_id`, `date`, `clk_id`),
	  KEY `clk_id` (`clk_id`)
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8;

CREATE TABLE IF NOT EXISTS `tbl_tariff` (
    `id`                  INT(11) UNSIGNED        NOT NULL AUTO_INCREMENT                    COMMENT '自增id',
    `ad_id`               INT(11)                 NOT NULL DEFAULT 0                         COMMENT '广告id',
    `stored`              DECIMAL(10, 2)          NOT NULL DEFAULT '0.00'                    COMMENT '预存金额',
    `balance`             DECIMAL(10, 2)          NOT NULL DEFAULT '0.00'                    COMMENT '剩余金额',
    `cpc_spend`           DECIMAL(10, 2)          NOT NULL DEFAULT '0.00'                    COMMENT '每次点击费用',
    `utime`               TIMESTAMP               NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录更新时间',
    PRIMARY KEY (`id`),
    KEY `ad_id` (`ad_id`)
) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8;