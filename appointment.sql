-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 19, 2025 at 07:47 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `appointment`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
  `AppointmentID` int(11) NOT NULL,
  `PatientID` int(11) NOT NULL,
  `DoctorID` int(11) NOT NULL,
  `AppointmentDate` date NOT NULL,
  `AppointmentTime` time NOT NULL,
  `Status` enum('pending','accepted','cancelled','completed','noshow') NOT NULL DEFAULT 'pending',
  `NoShowReason` text DEFAULT NULL,
  `MarkedAsNoShowBy` int(11) DEFAULT NULL,
  `MarkedAsNoShowAt` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`AppointmentID`, `PatientID`, `DoctorID`, `AppointmentDate`, `AppointmentTime`, `Status`, `NoShowReason`, `MarkedAsNoShowBy`, `MarkedAsNoShowAt`) VALUES
(111, 1, 3, '2025-01-05', '09:00:00', 'completed', NULL, NULL, NULL),
(112, 2, 3, '2025-01-05', '10:00:00', 'completed', NULL, NULL, NULL),
(113, 1, 3, '2025-01-12', '11:00:00', 'completed', NULL, NULL, NULL),
(114, 5, 3, '2025-01-12', '14:00:00', 'completed', NULL, NULL, NULL),
(115, 2, 3, '2025-01-19', '15:00:00', 'cancelled', NULL, NULL, NULL),
(116, 1, 3, '2025-01-26', '09:30:00', 'completed', NULL, NULL, NULL),
(117, 1, 3, '2025-02-02', '10:00:00', 'completed', NULL, NULL, NULL),
(118, 2, 3, '2025-02-02', '11:00:00', 'completed', NULL, NULL, NULL),
(119, 5, 3, '2025-02-09', '14:00:00', 'cancelled', NULL, NULL, NULL),
(120, 1, 3, '2025-02-16', '15:00:00', 'completed', NULL, NULL, NULL),
(121, 2, 3, '2025-02-23', '09:00:00', 'pending', NULL, NULL, NULL),
(122, 1, 3, '2025-03-02', '10:00:00', 'completed', NULL, NULL, NULL),
(123, 2, 3, '2025-03-02', '11:00:00', 'completed', NULL, NULL, NULL),
(124, 5, 3, '2025-03-09', '14:00:00', 'completed', NULL, NULL, NULL),
(125, 1, 3, '2025-03-16', '15:00:00', 'completed', NULL, NULL, NULL),
(126, 2, 3, '2025-03-23', '09:00:00', 'completed', NULL, NULL, NULL),
(127, 6, 3, '2025-03-30', '10:30:00', 'completed', NULL, NULL, NULL),
(128, 7, 3, '2025-04-06', '11:00:00', 'completed', NULL, NULL, NULL),
(129, 5, 3, '2025-04-06', '14:00:00', 'completed', NULL, NULL, NULL),
(130, 1, 3, '2025-04-13', '15:00:00', 'completed', NULL, NULL, NULL),
(131, 7, 3, '2025-04-20', '09:00:00', 'cancelled', NULL, NULL, NULL),
(132, 5, 3, '2025-04-27', '10:00:00', 'completed', NULL, NULL, NULL),
(133, 1, 3, '2025-05-04', '11:00:00', 'completed', NULL, NULL, NULL),
(134, 2, 3, '2025-05-04', '14:00:00', 'completed', NULL, NULL, NULL),
(135, 5, 3, '2025-05-11', '15:00:00', 'completed', NULL, NULL, NULL),
(136, 6, 3, '2025-05-18', '09:00:00', 'pending', NULL, NULL, NULL),
(137, 7, 3, '2025-05-25', '10:00:00', 'completed', NULL, NULL, NULL),
(138, 1, 3, '2025-12-11', '09:00:00', 'completed', NULL, NULL, NULL),
(139, 2, 3, '2025-12-13', '10:00:00', 'completed', NULL, NULL, NULL),
(140, 5, 3, '2025-12-15', '14:00:00', 'cancelled', NULL, NULL, NULL),
(141, 6, 3, '2025-12-18', '15:00:00', 'noshow', 'Patient did not arrive', 3, '2025-12-18 05:49:49'),
(142, 7, 3, '2025-12-20', '09:30:00', 'accepted', NULL, NULL, NULL),
(143, 2, 4, '2025-01-07', '09:00:00', 'completed', NULL, NULL, NULL),
(144, 1, 4, '2025-01-07', '10:00:00', 'completed', NULL, NULL, NULL),
(145, 5, 4, '2025-01-14', '11:00:00', 'completed', NULL, NULL, NULL),
(146, 6, 4, '2025-01-14', '14:00:00', 'completed', NULL, NULL, NULL),
(147, 2, 4, '2025-01-21', '15:00:00', 'cancelled', NULL, NULL, NULL),
(148, 1, 4, '2025-01-28', '09:30:00', 'completed', NULL, NULL, NULL),
(149, 1, 4, '2025-02-04', '10:00:00', 'completed', NULL, NULL, NULL),
(150, 2, 4, '2025-02-04', '11:00:00', 'completed', NULL, NULL, NULL),
(151, 5, 4, '2025-02-11', '14:00:00', 'completed', NULL, NULL, NULL),
(152, 6, 4, '2025-02-18', '15:00:00', 'completed', NULL, NULL, NULL),
(153, 7, 4, '2025-02-25', '09:00:00', 'completed', NULL, NULL, NULL),
(154, 1, 4, '2025-03-04', '10:00:00', 'completed', NULL, NULL, NULL),
(155, 2, 4, '2025-03-04', '11:00:00', 'completed', NULL, NULL, NULL),
(156, 5, 4, '2025-03-11', '14:00:00', 'completed', NULL, NULL, NULL),
(157, 6, 4, '2025-03-18', '15:00:00', 'completed', NULL, NULL, NULL),
(158, 7, 4, '2025-03-25', '09:00:00', 'completed', NULL, NULL, NULL),
(159, 1, 4, '2025-04-01', '11:00:00', 'completed', NULL, NULL, NULL),
(160, 2, 4, '2025-04-08', '14:00:00', 'completed', NULL, NULL, NULL),
(161, 5, 4, '2025-04-15', '15:00:00', 'completed', NULL, NULL, NULL),
(162, 6, 4, '2025-04-22', '09:00:00', 'cancelled', NULL, NULL, NULL),
(163, 7, 4, '2025-04-29', '10:00:00', 'completed', NULL, NULL, NULL),
(164, 1, 4, '2025-05-06', '11:00:00', 'completed', NULL, NULL, NULL),
(165, 2, 4, '2025-05-06', '14:00:00', 'completed', NULL, NULL, NULL),
(166, 5, 4, '2025-05-13', '15:00:00', 'completed', NULL, NULL, NULL),
(167, 6, 4, '2025-05-20', '09:00:00', 'pending', NULL, NULL, NULL),
(168, 7, 4, '2025-05-27', '10:00:00', 'completed', NULL, NULL, NULL),
(169, 1, 4, '2025-12-12', '09:00:00', 'completed', NULL, NULL, NULL),
(170, 2, 4, '2025-12-14', '10:00:00', 'completed', NULL, NULL, NULL),
(171, 5, 4, '2025-12-16', '14:00:00', 'completed', NULL, NULL, NULL),
(172, 6, 4, '2025-12-19', '15:00:00', 'accepted', NULL, NULL, NULL),
(173, 7, 4, '2025-12-21', '09:30:00', 'pending', NULL, NULL, NULL),
(174, 1, 3, '2025-12-18', '19:00:00', 'completed', NULL, NULL, NULL),
(175, 1, 3, '2025-12-18', '09:00:00', 'cancelled', NULL, NULL, NULL),
(176, 1, 3, '2025-12-18', '21:00:00', 'completed', NULL, NULL, NULL),
(177, 1, 3, '2025-12-25', '09:00:00', 'pending', NULL, NULL, NULL),
(178, 1, 3, '2025-12-18', '22:00:00', 'cancelled', NULL, NULL, NULL),
(179, 1, 3, '2025-12-18', '22:00:00', 'pending', NULL, NULL, NULL),
(180, 1, 3, '2025-12-18', '23:00:00', 'pending', NULL, NULL, NULL),
(181, 1, 3, '2025-12-18', '23:00:00', 'pending', NULL, NULL, NULL),
(182, 1, 3, '2025-12-19', '09:00:00', 'noshow', 'Patient absent', 3, '2025-12-18 16:12:19'),
(183, 1, 3, '2025-12-19', '10:00:00', 'completed', NULL, NULL, NULL),
(184, 1, 3, '2025-12-19', '07:00:00', 'completed', NULL, NULL, NULL),
(185, 1, 3, '2025-12-19', '19:00:00', 'pending', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `DoctorID` int(11) NOT NULL,
  `Specialization` varchar(100) DEFAULT NULL,
  `LicenseNumber` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`DoctorID`, `Specialization`, `LicenseNumber`) VALUES
(3, 'Dentist', 'LIC-001'),
(4, 'Psychiatrist', 'LIC-002');

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `NotificationID` int(11) NOT NULL,
  `UserID` int(11) NOT NULL,
  `Message` text NOT NULL,
  `IsRead` tinyint(1) DEFAULT 0,
  `CreatedAt` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `notification`
--

INSERT INTO `notification` (`NotificationID`, `UserID`, `Message`, `IsRead`, `CreatedAt`) VALUES
(1, 3, 'Appointment rescheduled by John Doe to 2025-12-18 at 09:00:00.', 1, '2025-12-18 13:32:34'),
(2, 3, 'New appointment request from John Doe on 2025-12-18 at 22:00:00.', 1, '2025-12-18 13:32:45'),
(3, 1, 'Your appointment was CANCELLED. Reason: im busy', 1, '2025-12-18 13:34:22'),
(4, 3, 'New appointment: John Doe on 2025-12-18 at 22:00:00.', 1, '2025-12-18 13:55:26'),
(5, 1, 'Your appointment with Dr. Robert Levi was CONFIRMED.', 1, '2025-12-18 13:56:01'),
(6, 1, 'Your appointment with Dr. Robert Levi was CONFIRMED.', 1, '2025-12-18 13:56:04'),
(7, 3, 'New appointment: John Doe on 2025-12-18 at 23:00:00.', 1, '2025-12-18 14:23:17'),
(8, 1, 'Your appointment was CANCELLED. Reason: busy', 1, '2025-12-18 14:23:38'),
(9, 3, 'New appointment: John Doe on 2025-12-18 at 23:00:00.', 1, '2025-12-18 14:46:03'),
(10, 1, 'Your appointment with Dr. Robert Levi was CONFIRMED.', 1, '2025-12-18 14:47:39'),
(11, 1, 'Your appointment with Dr. Robert Levi was CONFIRMED.', 1, '2025-12-18 14:47:42'),
(12, 1, 'Your appointment with Dr. Robert Levi was CONFIRMED.', 1, '2025-12-18 14:47:44'),
(13, 3, 'New appointment: John Doe on 2025-12-19 at 09:00:00.', 1, '2025-12-18 16:12:01'),
(14, 1, 'Your appointment with Dr. Robert Levi was CONFIRMED.', 1, '2025-12-18 16:12:14'),
(15, 3, 'New appointment: John Doe on 2025-12-19 at 10:00:00.', 1, '2025-12-18 16:58:46'),
(16, 1, 'Your appointment with Dr. Robert Levi was CONFIRMED.', 1, '2025-12-18 16:59:06'),
(17, 3, 'Reschedule: John Doe to 2025-12-25 at 09:00:00.', 1, '2025-12-18 17:14:04'),
(18, 3, 'New appointment: John Doe on 2025-12-19 at 07:00:00.', 1, '2025-12-18 17:19:36'),
(19, 3, 'New appointment: John Doe on 2025-12-19 at 19:00:00.', 1, '2025-12-18 19:24:15'),
(20, 1, 'Your appointment with Dr. Robert Levi was CONFIRMED.', 1, '2025-12-18 19:25:22');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `PatientID` int(11) NOT NULL,
  `DateOfBirth` date DEFAULT NULL,
  `Gender` enum('M','F','O') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`PatientID`, `DateOfBirth`, `Gender`) VALUES
(1, '1990-01-15', 'M'),
(2, '1985-05-20', 'F'),
(4, '1988-03-22', 'M'),
(5, '1992-07-14', 'F'),
(6, '1980-11-30', 'M'),
(7, '1978-11-30', 'M'),
(8, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `UserID` int(11) NOT NULL,
  `FirstName` varchar(100) NOT NULL,
  `LastName` varchar(100) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Phone` varchar(20) DEFAULT NULL,
  `Password` varchar(255) NOT NULL,
  `UserType` enum('P','D') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`UserID`, `FirstName`, `LastName`, `Email`, `Address`, `Phone`, `Password`, `UserType`) VALUES
(1, 'John', 'Doe', 'patient', '123 Main St', '123-456-7890', 'patient', 'P'),
(2, 'Jane', 'Smith', 'jane@example.com', '456 Oak St', '987-654-3210', 'password123', 'P'),
(3, 'Robert', 'Levi', 'doctor', 'Hospital St', '555-123-4567', 'doctor', 'D'),
(4, 'Chancee', 'Chi', 'dr.chi@careline.com', 'Clinic Ave', '555-987-6543', 'doctor456', 'D'),
(5, 'John', 'Doe', 'john@test.com', '123 Main St', '1234567890', 'password', 'P'),
(6, 'Jane', 'Smith', 'jane@test.com', '456 Oak St', '0987654321', 'password', 'P'),
(7, 'Bob', 'Johnson', 'bob@test.com', '789 Pine St', '5551234567', 'password', 'P'),
(8, 'Levin', 'Hoo', 'levinhoo@gmail.com', '', '09531623428', '0930Levi?!', 'P');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointment`
--
ALTER TABLE `appointment`
  ADD PRIMARY KEY (`AppointmentID`),
  ADD KEY `PatientID` (`PatientID`),
  ADD KEY `DoctorID` (`DoctorID`),
  ADD KEY `idx_appointment_date` (`AppointmentDate`),
  ADD KEY `idx_appointment_status` (`Status`),
  ADD KEY `MarkedAsNoShowBy` (`MarkedAsNoShowBy`),
  ADD KEY `idx_appointment_noshow` (`Status`,`AppointmentDate`);

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`DoctorID`),
  ADD UNIQUE KEY `LicenseNumber` (`LicenseNumber`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`NotificationID`),
  ADD KEY `UserID` (`UserID`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`PatientID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`UserID`),
  ADD UNIQUE KEY `Email` (`Email`),
  ADD KEY `idx_user_email` (`Email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointment`
--
ALTER TABLE `appointment`
  MODIFY `AppointmentID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=186;

--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `NotificationID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `UserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointment`
--
ALTER TABLE `appointment`
  ADD CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`PatientID`) REFERENCES `patient` (`PatientID`) ON DELETE CASCADE,
  ADD CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`DoctorID`) REFERENCES `doctor` (`DoctorID`) ON DELETE CASCADE,
  ADD CONSTRAINT `appointment_ibfk_3` FOREIGN KEY (`MarkedAsNoShowBy`) REFERENCES `user` (`UserID`);

--
-- Constraints for table `doctor`
--
ALTER TABLE `doctor`
  ADD CONSTRAINT `doctor_ibfk_1` FOREIGN KEY (`DoctorID`) REFERENCES `user` (`UserID`) ON DELETE CASCADE;

--
-- Constraints for table `notification`
--
ALTER TABLE `notification`
  ADD CONSTRAINT `notification_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`) ON DELETE CASCADE;

--
-- Constraints for table `patient`
--
ALTER TABLE `patient`
  ADD CONSTRAINT `patient_ibfk_1` FOREIGN KEY (`PatientID`) REFERENCES `user` (`UserID`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
