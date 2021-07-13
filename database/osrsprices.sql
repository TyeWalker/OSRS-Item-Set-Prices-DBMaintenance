-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3303
-- Generation Time: Jul 13, 2021 at 05:53 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `osrsprices`
--

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
CREATE TABLE IF NOT EXISTS `item` (
  `itemID` varchar(15) NOT NULL,
  `itemName` varchar(100) NOT NULL,
  `itemGELimit` int(10) NOT NULL,
  `itemHighAlch` int(10) NOT NULL,
  PRIMARY KEY (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `itemhightimes`
--

DROP TABLE IF EXISTS `itemhightimes`;
CREATE TABLE IF NOT EXISTS `itemhightimes` (
  `itemHighID` int(20) NOT NULL AUTO_INCREMENT,
  `itemID` varchar(15) NOT NULL,
  `itemHigh` int(15) NOT NULL,
  `itemHighTime` datetime(6) NOT NULL,
  PRIMARY KEY (`itemHighID`),
  KEY `itemID` (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `itemlatest`
--

DROP TABLE IF EXISTS `itemlatest`;
CREATE TABLE IF NOT EXISTS `itemlatest` (
  `itemID` varchar(15) NOT NULL,
  `itemHigh` int(15) NOT NULL,
  `itemHighTime` datetime(6) NOT NULL,
  `itemLow` int(15) NOT NULL,
  `itemLowTime` datetime(6) NOT NULL,
  PRIMARY KEY (`itemID`),
  KEY `itemID` (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `itemlowtimes`
--

DROP TABLE IF EXISTS `itemlowtimes`;
CREATE TABLE IF NOT EXISTS `itemlowtimes` (
  `itemLowID` int(20) NOT NULL AUTO_INCREMENT,
  `itemID` varchar(15) NOT NULL,
  `itemLow` int(15) NOT NULL,
  `itemLowTime` datetime(6) NOT NULL,
  PRIMARY KEY (`itemLowID`),
  KEY `itemID` (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `onedayvolume`
--

DROP TABLE IF EXISTS `onedayvolume`;
CREATE TABLE IF NOT EXISTS `onedayvolume` (
  `itemID` varchar(15) NOT NULL,
  `odHighPriceVolume` int(15) NOT NULL,
  `odLowPriceVolume` int(15) NOT NULL,
  KEY `itemID` (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `onehourvolume`
--

DROP TABLE IF EXISTS `onehourvolume`;
CREATE TABLE IF NOT EXISTS `onehourvolume` (
  `itemID` varchar(15) NOT NULL,
  `ohHighPriceVolume` int(15) NOT NULL,
  `ohLowPriceVolume` int(15) NOT NULL,
  PRIMARY KEY (`itemID`),
  KEY `itemID` (`itemID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
