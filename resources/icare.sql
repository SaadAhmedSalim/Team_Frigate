-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 01, 2019 at 05:04 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `icare`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `NID` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Age` int(11) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pwd` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`NID`, `Name`, `Age`, `Gender`, `Email`, `Address`, `Pwd`) VALUES
(555666, 'saad', 55, 'Male', 'saad.salim@northsouth.edu', 'barisal', 'b7f6593421d9f21bdd5caef01b24f5c8'),
(1631111042, 'Saraf Sumaita Hasan', 21, 'Female', 'saraf.hasan@gmail.com', 'Mohakhali Dohs', '133edbe1acb0adb7ebc07ccc053f8cf4'),
(1631189042, 'Md. Masudur Rahman', 23, 'Male', 'masudurhimel@gmail.com', '36/4 Cantonment', '0ece044a192244eb89317e00c4cfdcd6');

-- --------------------------------------------------------

--
-- Table structure for table `allusers`
--

CREATE TABLE `allusers` (
  `Nid` int(11) NOT NULL,
  `Pwd` varchar(100) NOT NULL,
  `Role` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `allusers`
--

INSERT INTO `allusers` (`Nid`, `Pwd`, `Role`) VALUES
(12348564, 'ea48576f30be1669971699c09ad05c94', 'Patient'),
(1201234042, '4d1865b7cc70b3f54148e435550397e8', 'Patient'),
(1621234042, 'ac16292ec026ed4c5da174c1c308675a', 'Patient'),
(1631111042, '133edbe1acb0adb7ebc07ccc053f8cf4', 'Patient'),
(1631189042, '8b34af2a5ca702975a732df291a21777', 'Patient'),
(1711248042, 'ae2bac2e4b4da805d01b2952d7e35ba4', 'Patient'),
(1712429042, '113da2f47c69edf4f5e1575be77159c4', 'Patient');

-- --------------------------------------------------------

--
-- Table structure for table `docpatient`
--

CREATE TABLE `docpatient` (
  `Doc_Nid` int(11) NOT NULL,
  `Pat_Nid` int(11) NOT NULL,
  `Prescription_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `NID` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Age` int(11) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `SSC_GPA` double DEFAULT NULL,
  `SSC_Session` int(11) DEFAULT NULL,
  `SSC_inst` varchar(100) DEFAULT NULL,
  `HSC_GPA` double DEFAULT NULL,
  `HSC_Session` int(11) DEFAULT NULL,
  `HSC_inst` varchar(100) DEFAULT NULL,
  `BMDC_RegNo` int(11) DEFAULT NULL,
  `MBBS_Session` int(11) DEFAULT NULL,
  `MBBS_inst` varchar(100) DEFAULT NULL,
  `PostGrad_deatails` varchar(300) DEFAULT NULL,
  `Pwd` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`NID`, `Name`, `Age`, `Gender`, `Email`, `Address`, `SSC_GPA`, `SSC_Session`, `SSC_inst`, `HSC_GPA`, `HSC_Session`, `HSC_inst`, `BMDC_RegNo`, `MBBS_Session`, `MBBS_inst`, `PostGrad_deatails`, `Pwd`) VALUES
(1234, 'Md. Ariful Islam', 22, 'Male', 'arifulome@gmail.com', 'Sylhet', 5, 2013, 'BAF Shaheen KTL', 5, 2015, 'Adamjee Cantonment', 5050, 2015, 'SOMC', 'FCPS in Heart', '157cfcbc4fe5cb3ce90c312473cd3cd0'),
(4562, 'Mortuza Shahriar', 22, 'Male', 'mortuza.shahriar@gmail.com', 'Dhanmondi', 5, 2013, 'Dhaka Residential Model College', 5, 2013, 'Dhaka Residential Model College', 8888, 2015, 'Dhaka Medical College', 'Neurologist , FCPS', 'bce1ba183af3c7a6849a34d5cac08f22'),
(181229932, 'saad', 22, 'Male', 'saad.salim@northsouth.edu', '34 house b block bashundhora', 5, 2013, 'radio colony', 5, 2013, 'radio colony', 566259532, 2019, 'dmc', '', 'ed2b1f468c5f915f3f1cf75d7068baae'),
(222232345, 'niazi', 22, 'Male', 'mahrab570@gmail.com', 'rrr', 4, 2013, 'dmc', 5, 2015, 'dd', 34343412, 44, 'dmc', '', '0681b959321f574e7ad1869cc3011346');

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE `medicine` (
  `Name` varchar(100) NOT NULL,
  `Miligrams` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `NID` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Age` int(11) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Pwd` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`NID`, `Name`, `Age`, `Gender`, `Email`, `Address`, `Pwd`) VALUES
(111, 'asad', 21, 'Male', 'saad.salim@northsouth.edu', '34 house b block bashundhora', 'ed2b1f468c5f915f3f1cf75d7068baae'),
(12348564, 'mahabub', 21, 'Male', 'mahabub@gmail.com', '12 house A block ', 'ea48576f30be1669971699c09ad05c94'),
(1151234042, 'Munira Rahman', 35, 'Female', 'munira.rahman@gmail.com', 'Baridhara', '81dc9bdb52d04dc20036dbd8313ed055'),
(1201234042, 'Md. Mizanur Rahman', 35, 'Male', 'mizan.rahman@gmail.com', 'Balughat Cantonment', '4d1865b7cc70b3f54148e435550397e8'),
(1511933042, 'Pranta Ahmed', 22, 'Male', 'pranta.ahmed@gmail.com', 'Cantonment DOHS', '81dc9bdb52d04dc20036dbd8313ed055'),
(1621234042, 'Riftabin Kabir', 22, 'Male', 'rifta.kabir@gmail.com', 'Balughat Cantonment', 'ac16292ec026ed4c5da174c1c308675a'),
(1631111042, 'Saraf Sumaita Hasan', 21, 'Female', 'saraf.hasan@gmail.com', 'Mohakhali Dohs', '133edbe1acb0adb7ebc07ccc053f8cf4'),
(1631189042, 'Md. Masudur Rahman', 23, 'Male', 'masudurhimel@gmail.com', '36/4 Cantonment Dhaka-1206', '8b34af2a5ca702975a732df291a21777'),
(1711248042, 'Md. Niazi Mahrab', 22, 'Male', 'niazi.mahrab@northsouth.edu', 'bashundhara', 'ae2bac2e4b4da805d01b2952d7e35ba4'),
(1712429042, 'S M Mustafiz Ridom', 22, 'Male', 'mustafizridom@gmail.com', 'bashundhara ,Dhaka', '113da2f47c69edf4f5e1575be77159c4');

-- --------------------------------------------------------

--
-- Table structure for table `prescription`
--

CREATE TABLE `prescription` (
  `Doc_id` varchar(100) NOT NULL,
  `Patient_Id` varchar(100) NOT NULL,
  `Prescription_id` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prescription`
--

INSERT INTO `prescription` (`Doc_id`, `Patient_Id`, `Prescription_id`) VALUES
('1234', '1151234042', '1234-1151234042'),
('1234', '1201234042', '1234-1201234042'),
('1234', '1511933042', '1234-1511933042'),
('1234', '1711248042', '1234-1711248042'),
('1234', '1712429042', '1234-1712429042'),
('181229932', '12348564', '181229932-12348564'),
('4562', '1631189042', '4562-1631189042');

-- --------------------------------------------------------

--
-- Table structure for table `prescriptioncomplaint`
--

CREATE TABLE `prescriptioncomplaint` (
  `Prescription_Id` varchar(100) DEFAULT NULL,
  `Complaint` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prescriptioncomplaint`
--

INSERT INTO `prescriptioncomplaint` (`Prescription_Id`, `Complaint`) VALUES
('1234-1201234042', 'Back pain'),
('1234-1201234042', 'Inso'),
('1234-1201234042', 'Trouble to stand Straight '),
('1234-1711248042', 'Headache'),
('1234-1712429042', 'Insomnia'),
('4562-1631189042', 'Nausea'),
('1234-1151234042', 'Sleeping Disorder'),
('1234-1151234042', 'Insomnia'),
('1234-1511933042', 'Sickness'),
('181229932-12348564', 'heart');

-- --------------------------------------------------------

--
-- Table structure for table `prescriptionexamination`
--

CREATE TABLE `prescriptionexamination` (
  `Prescription_Id` varchar(100) DEFAULT NULL,
  `Examination_type` varchar(100) DEFAULT NULL,
  `Measurement` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prescriptionexamination`
--

INSERT INTO `prescriptionexamination` (`Prescription_Id`, `Examination_type`, `Measurement`) VALUES
('1234-1201234042', 'Weight', '60 kg'),
('1234-1201234042', 'Pulse', '80 bpm'),
('1234-1201234042', 'Pressure', 'High'),
('1234-1711248042', 'Weight', '75 kg'),
('1234-1711248042', 'Pressure', 'Normal'),
('1234-1712429042', 'bp', 'Low'),
('1234-1712429042', 'Weight', '76 kg'),
('1234-1712429042', 'Height', '6 ft'),
('4562-1631189042', 'Weight', '70 Kg'),
('4562-1631189042', 'bp', '80'),
('4562-1631189042', 'Pulse', 'Normal'),
('1234-1151234042', 'Weight', '60 Kg'),
('1234-1151234042', 'BMI', 'Normal'),
('1234-1511933042', 'bp', 'Normal'),
('181229932-12348564', 'bp', '120');

-- --------------------------------------------------------

--
-- Table structure for table `prescriptionmedicine`
--

CREATE TABLE `prescriptionmedicine` (
  `Prescription_Id` varchar(100) DEFAULT NULL,
  `Medicine` varchar(100) DEFAULT NULL,
  `Timing` varchar(100) DEFAULT NULL,
  `Duration` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prescriptionmedicine`
--

INSERT INTO `prescriptionmedicine` (`Prescription_Id`, `Medicine`, `Timing`, `Duration`) VALUES
('1234-1201234042', 'Paracetamol', 'Noon  Night  ', '1 week'),
('1234-1201234042', 'Telfast', 'Night  ', '1 month'),
('1234-1711248042', 'Paracetamol', 'Noon  ', '1 Month'),
('1234-1711248042', 'Telfast', 'Morning  Night  ', '1 week'),
('1234-1712429042', 'Cefotil', 'Morning  Noon  Night  ', '1 Month'),
('4562-1631189042', 'Fimoxyl', 'Night  ', '1 Week'),
('4562-1631189042', 'Spironolactone', 'Morning  Night  ', '3 Day'),
('1234-1151234042', 'Glucose', 'Night  ', '1 Month'),
('1234-1511933042', 'Telfast', 'Night  ', '1 MOnth'),
('181229932-12348564', 'Vitamin B-Complex', 'Morning  ', '1 week'),
('181229932-12348564', 'Measles vaccine', 'Noon  ', '2 week');

-- --------------------------------------------------------

--
-- Table structure for table `prescriptionsuggestion`
--

CREATE TABLE `prescriptionsuggestion` (
  `Prescription_Id` varchar(100) DEFAULT NULL,
  `Suggestion` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prescriptionsuggestion`
--

INSERT INTO `prescriptionsuggestion` (`Prescription_Id`, `Suggestion`) VALUES
('1234-1201234042', 'Try to maintain a regular life'),
('1234-1711248042', 'Maintain a regular life'),
('1234-1712429042', 'Sleep tight .'),
('4562-1631189042', 'Try to focus more on everything.'),
('1234-1151234042', 'Be tension free '),
('1234-1511933042', 'Sleep tight.');

-- --------------------------------------------------------

--
-- Table structure for table `prescriptiontests`
--

CREATE TABLE `prescriptiontests` (
  `Prescription_Id` varchar(100) DEFAULT NULL,
  `Tests` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `prescriptiontests`
--

INSERT INTO `prescriptiontests` (`Prescription_Id`, `Tests`) VALUES
('1234-1201234042', 'Bilirubin(blood)'),
('1234-1201234042', 'X-ray(Back Bone)'),
('1234-1711248042', 'Urine Test'),
('1234-1712429042', 'Bilirubin(blood)'),
('4562-1631189042', 'Urine Test'),
('1234-1151234042', 'Urine Test'),
('1234-1511933042', 'X ray'),
('181229932-12348564', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`NID`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- Indexes for table `allusers`
--
ALTER TABLE `allusers`
  ADD PRIMARY KEY (`Nid`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`NID`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- Indexes for table `medicine`
--
ALTER TABLE `medicine`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`NID`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- Indexes for table `prescription`
--
ALTER TABLE `prescription`
  ADD PRIMARY KEY (`Prescription_id`);

--
-- Indexes for table `prescriptioncomplaint`
--
ALTER TABLE `prescriptioncomplaint`
  ADD KEY `FK_prescriptionComplaint` (`Prescription_Id`);

--
-- Indexes for table `prescriptionexamination`
--
ALTER TABLE `prescriptionexamination`
  ADD KEY `FK_prescriptionExamination` (`Prescription_Id`);

--
-- Indexes for table `prescriptionmedicine`
--
ALTER TABLE `prescriptionmedicine`
  ADD KEY `FK_prescriptionMed` (`Prescription_Id`);

--
-- Indexes for table `prescriptionsuggestion`
--
ALTER TABLE `prescriptionsuggestion`
  ADD KEY `FK_prescriptionSuggestion` (`Prescription_Id`);

--
-- Indexes for table `prescriptiontests`
--
ALTER TABLE `prescriptiontests`
  ADD KEY `FK_prescriptionTests` (`Prescription_Id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `allusers`
--
ALTER TABLE `allusers`
  ADD CONSTRAINT `allusers_ibfk_1` FOREIGN KEY (`Nid`) REFERENCES `patient` (`NID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `prescriptioncomplaint`
--
ALTER TABLE `prescriptioncomplaint`
  ADD CONSTRAINT `FK_prescriptionComplaint` FOREIGN KEY (`Prescription_Id`) REFERENCES `prescription` (`Prescription_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `prescriptionexamination`
--
ALTER TABLE `prescriptionexamination`
  ADD CONSTRAINT `FK_prescriptionExamination` FOREIGN KEY (`Prescription_Id`) REFERENCES `prescription` (`Prescription_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `prescriptionmedicine`
--
ALTER TABLE `prescriptionmedicine`
  ADD CONSTRAINT `FK_prescriptionMed` FOREIGN KEY (`Prescription_Id`) REFERENCES `prescription` (`Prescription_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `prescriptionsuggestion`
--
ALTER TABLE `prescriptionsuggestion`
  ADD CONSTRAINT `FK_prescriptionSuggestion` FOREIGN KEY (`Prescription_Id`) REFERENCES `prescription` (`Prescription_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `prescriptiontests`
--
ALTER TABLE `prescriptiontests`
  ADD CONSTRAINT `FK_prescriptionTests` FOREIGN KEY (`Prescription_Id`) REFERENCES `prescription` (`Prescription_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
