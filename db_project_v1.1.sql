-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 10. Mai, 2022 19:40 PM
-- Tjener-versjon: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_project_v1.1`
--

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `customer_rep`
--

CREATE TABLE `customer_rep` (
  `employee_number` int(100) NOT NULL,
  `cr_id` int(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `customer_rep`
--

INSERT INTO `customer_rep` (`employee_number`, `cr_id`, `first_name`, `last_name`, `department`) VALUES
(1, 1, 'John', 'Wells', 'Sales');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `driver`
--

CREATE TABLE `driver` (
  `driver_id` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `driver`
--

INSERT INTO `driver` (`driver_id`) VALUES
(1);

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `franchise`
--

CREATE TABLE `franchise` (
  `customer_id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `emp_num` int(100) NOT NULL,
  `shipping_adress` varchar(100) NOT NULL,
  `buying_price` int(100) NOT NULL,
  `contract_start` date NOT NULL,
  `contract_end` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `franchise`
--

INSERT INTO `franchise` (`customer_id`, `name`, `emp_num`, `shipping_adress`, `buying_price`, `contract_start`, `contract_end`) VALUES
(1, 'Fischer', 1, 'Fjellvegen 3', 5000, '2022-03-01', '2022-03-28');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `franchise_store`
--

CREATE TABLE `franchise_store` (
  `store_id` int(100) NOT NULL,
  `customer_id` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `individual_store`
--

CREATE TABLE `individual_store` (
  `customer_id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `emp_num` int(100) NOT NULL,
  `shipping_adress` varchar(100) NOT NULL,
  `buying_price` int(100) NOT NULL,
  `contract_start` date NOT NULL,
  `contract_end` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `individual_store`
--

INSERT INTO `individual_store` (`customer_id`, `name`, `emp_num`, `shipping_adress`, `buying_price`, `contract_start`, `contract_end`) VALUES
(1, 'Ski Store', 1, 'Helms gate 74', 4000, '2022-02-01', '2022-02-28');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `order`
--

CREATE TABLE `order` (
  `order_number` int(100) NOT NULL,
  `franchise_id` int(100) NOT NULL,
  `individualStore_id` int(100) NOT NULL,
  `teamSki_id` int(100) NOT NULL,
  `s_number` int(100) NOT NULL,
  `ski_type` enum('classic_cross_country','free_style_skate') NOT NULL,
  `quantity` int(100) NOT NULL,
  `tot_price` int(100) NOT NULL,
  `state` enum('new','open','skis_available','ready_to_be_shipped', 'shipped') NOT NULL,
  `state_change` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `order`
--

INSERT INTO `order` (`order_number`, `franchise_id`, `individualStore_id`, `teamSki_id`, `s_number`, `ski_type`, `quantity`, `tot_price`, `state`, `state_change`) VALUES
(1, 1, 1, 1, 1, 'classic_cross_country', 50, 3456, 'new', 1);

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `order_skitype`
--

CREATE TABLE `order_skitype` (
  `o_num` int(100) NOT NULL,
  `type` int(100) NOT NULL,
  `quantity` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `planner_production_plans`
--

CREATE TABLE `planner_production_plans` (
  `emp_num` int(100) NOT NULL,
  `id` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `production_planner`
--

CREATE TABLE `production_planner` (
  `employee_number` int(100) NOT NULL,
  `pp_id` int(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `production_plans`
--

CREATE TABLE `production_plans` (
  `id` int(100) NOT NULL,
  `nr_ski_type_everyday` int(100) NOT NULL,
  `ski_production_everyday` int(100) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `production_plans`
--

INSERT INTO `production_plans` (`id`, `nr_ski_type_everyday`, `ski_production_everyday`, `start_date`, `end_date`) VALUES
(1, 4, 345, '2022-03-01', '2022-03-28'),
(2, 4, 345, '2022-03-01', '2022-03-28');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `prod_plan_ski_type`
--

CREATE TABLE `prod_plan_ski_type` (
  `type_id` int(100) NOT NULL,
  `type` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `prod_plan_ski_type`
--

INSERT INTO `prod_plan_ski_type` (`type_id`, `type`) VALUES
(1, 3),
(2, 3);

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `shipments`
--

CREATE TABLE `shipments` (
  `shipment_number` int(100) NOT NULL,
  `transporter` int(100) NOT NULL,
  `driver_id` int(100) NOT NULL,
  `franchise_name` varchar(100) NOT NULL,
  `shipping_adress` varchar(100) NOT NULL,
  `scheduled_pickup_date` date NOT NULL,
  `state` enum('not ready','ready','shipped') NOT NULL,
  `transport_company` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `shipments`
--

INSERT INTO `shipments` (`shipment_number`, `transporter`, `driver_id`, `franchise_name`, `shipping_adress`, `scheduled_pickup_date`, `state`, `transport_company`) VALUES
(1, 1, 1, 'Fischer', 'Helms gate 74', '2022-05-12', 'not ready', 'Ski Transport');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `ski`
--

CREATE TABLE `ski` (
  `ski_number` int(100) NOT NULL,
  `emp_num` int(100) NOT NULL,
  `type_id` int(100) NOT NULL,
  `production_date` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `ski`
--

INSERT INTO `ski` (`ski_number`, `emp_num`, `type_id`, `production_date`) VALUES
(1, 1, 1, '24.08.21'),
(2, 1, 1, '25.08.21'),
(3, 1, 3, '26.08.21');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `ski_type`
--

CREATE TABLE `ski_type` (
  `type_id` int(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  `type_of_ski` enum('classic_cross_country','free_style_skate') NOT NULL,
  `size` int(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `historical` int(1) NOT NULL,
  `photo_url` varchar(100) NOT NULL,
  `msrpp` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `ski_type`
--

INSERT INTO `ski_type` (`type_id`, `model`, `type_of_ski`, `size`, `description`, `historical`, `photo_url`, `msrpp`) VALUES
(1, 'fischer-256', 'classic_cross_country', 60, 'Very cool ski', 0, '...', 123),
(2, 'fischer-366', 'classic_cross_country', 120, 'Very nice ski', 0, '...', 124),
(3, 'rossignol hyper mega', 'free_style_skate', 100, 'Very stylish ski', 0, '...', 125),
(4, 'rossignol hyper ultra', 'free_style_skate', 125, 'Sharp edges for control', 1, '1', 126);

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `storekeeper`
--

CREATE TABLE `storekeeper` (
  `employee_number` int(100) NOT NULL,
  `sk_id` int(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `storekeeper`
--

INSERT INTO `storekeeper` (`employee_number`, `sk_id`, `first_name`, `last_name`, `department`) VALUES
(1, 1, 'Leidulf', 'Vigre', 'Stavanger');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `team_skier`
--

CREATE TABLE `team_skier` (
  `customer_id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `emp_num` int(100) NOT NULL,
  `dob` date NOT NULL,
  `club` varchar(100) NOT NULL,
  `num_of_skies` int(100) NOT NULL,
  `contract_start` date NOT NULL,
  `contract_end` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `team_skier`
--

INSERT INTO `team_skier` (`customer_id`, `name`, `emp_num`, `dob`, `club`, `num_of_skies`, `contract_start`, `contract_end`) VALUES
(1, 'Hailey Swirbul', 1, '1998-10-07', 'Alaska Pacific University Nordic Ski Club', 5, '2022-02-06', '2022-07-22');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `transporters`
--

CREATE TABLE `transporters` (
  `user_id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `transporters`
--

INSERT INTO `transporters` (`user_id`, `name`) VALUES
(1, 'Åge Helland');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `user`
--

CREATE TABLE `user` (
  `user_id` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `user`
--

INSERT INTO `user` (`user_id`) VALUES
(1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_rep`
--
ALTER TABLE `customer_rep`
  ADD PRIMARY KEY (`employee_number`),
  ADD UNIQUE KEY `cr_id` (`cr_id`);

--
-- Indexes for table `driver`
--
ALTER TABLE `driver`
  ADD PRIMARY KEY (`driver_id`);

--
-- Indexes for table `franchise`
--
ALTER TABLE `franchise`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `emp_num` (`emp_num`);

--
-- Indexes for table `franchise_store`
--
ALTER TABLE `franchise_store`
  ADD PRIMARY KEY (`store_id`,`customer_id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `individual_store`
--
ALTER TABLE `individual_store`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `emp_num` (`emp_num`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`order_number`),
  ADD KEY `franchise_id` (`franchise_id`),
  ADD KEY `individualStore_id` (`individualStore_id`),
  ADD KEY `teamSki_id` (`teamSki_id`),
  ADD KEY `s_number` (`s_number`),
  ADD KEY `state_change` (`state_change`);

--
-- Indexes for table `order_skitype`
--
ALTER TABLE `order_skitype`
  ADD PRIMARY KEY (`o_num`,`type`),
  ADD KEY `type` (`type`);

--
-- Indexes for table `planner_production_plans`
--
ALTER TABLE `planner_production_plans`
  ADD PRIMARY KEY (`emp_num`,`id`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `production_planner`
--
ALTER TABLE `production_planner`
  ADD PRIMARY KEY (`employee_number`),
  ADD UNIQUE KEY `pp_id` (`pp_id`);

--
-- Indexes for table `production_plans`
--
ALTER TABLE `production_plans`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `prod_plan_ski_type`
--
ALTER TABLE `prod_plan_ski_type`
  ADD PRIMARY KEY (`type_id`,`type`),
  ADD KEY `type` (`type`);

--
-- Indexes for table `shipments`
--
ALTER TABLE `shipments`
  ADD PRIMARY KEY (`shipment_number`),
  ADD KEY `transporter` (`transporter`),
  ADD KEY `driver_id` (`driver_id`);

--
-- Indexes for table `ski`
--
ALTER TABLE `ski`
  ADD PRIMARY KEY (`ski_number`),
  ADD KEY `emp_num` (`emp_num`),
  ADD KEY `type_id` (`type_id`);

--
-- Indexes for table `ski_type`
--
ALTER TABLE `ski_type`
  ADD PRIMARY KEY (`type_id`);

--
-- Indexes for table `storekeeper`
--
ALTER TABLE `storekeeper`
  ADD PRIMARY KEY (`employee_number`),
  ADD UNIQUE KEY `sk_id` (`sk_id`);

--
-- Indexes for table `team_skier`
--
ALTER TABLE `team_skier`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `emp_num` (`emp_num`);

--
-- Indexes for table `transporters`
--
ALTER TABLE `transporters`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- Begrensninger for dumpede tabeller
--

--
-- Begrensninger for tabell `customer_rep`
--
ALTER TABLE `customer_rep`
  ADD CONSTRAINT `customer_rep_ibfk_1` FOREIGN KEY (`employee_number`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Begrensninger for tabell `franchise`
--
ALTER TABLE `franchise`
  ADD CONSTRAINT `franchise_ibfk_1` FOREIGN KEY (`emp_num`) REFERENCES `customer_rep` (`employee_number`),
  ADD CONSTRAINT `franchise_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Begrensninger for tabell `franchise_store`
--
ALTER TABLE `franchise_store`
  ADD CONSTRAINT `franchise_store_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `franchise` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Begrensninger for tabell `individual_store`
--
ALTER TABLE `individual_store`
  ADD CONSTRAINT `individual_store_ibfk_1` FOREIGN KEY (`emp_num`) REFERENCES `customer_rep` (`employee_number`),
  ADD CONSTRAINT `individual_store_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Begrensninger for tabell `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_ibfk_1` FOREIGN KEY (`franchise_id`) REFERENCES `franchise` (`customer_id`),
  ADD CONSTRAINT `order_ibfk_2` FOREIGN KEY (`individualStore_id`) REFERENCES `individual_store` (`customer_id`),
  ADD CONSTRAINT `order_ibfk_3` FOREIGN KEY (`teamSki_id`) REFERENCES `team_skier` (`customer_id`),
  ADD CONSTRAINT `order_ibfk_4` FOREIGN KEY (`s_number`) REFERENCES `shipments` (`shipment_number`),
  ADD CONSTRAINT `order_ibfk_5` FOREIGN KEY (`state_change`) REFERENCES `customer_rep` (`employee_number`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Begrensninger for tabell `order_skitype`
--
ALTER TABLE `order_skitype`
  ADD CONSTRAINT `order_skitype_ibfk_1` FOREIGN KEY (`o_num`) REFERENCES `order` (`order_number`),
  ADD CONSTRAINT `order_skitype_ibfk_2` FOREIGN KEY (`type`) REFERENCES `ski_type` (`type_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Begrensninger for tabell `planner_production_plans`
--
ALTER TABLE `planner_production_plans`
  ADD CONSTRAINT `planner_production_plans_ibfk_1` FOREIGN KEY (`emp_num`) REFERENCES `production_planner` (`employee_number`),
  ADD CONSTRAINT `planner_production_plans_ibfk_2` FOREIGN KEY (`id`) REFERENCES `production_plans` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Begrensninger for tabell `production_planner`
--
ALTER TABLE `production_planner`
  ADD CONSTRAINT `production_planner_ibfk_1` FOREIGN KEY (`employee_number`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Begrensninger for tabell `prod_plan_ski_type`
--
ALTER TABLE `prod_plan_ski_type`
  ADD CONSTRAINT `prod_plan_ski_type_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `production_plans` (`id`),
  ADD CONSTRAINT `prod_plan_ski_type_ibfk_2` FOREIGN KEY (`type`) REFERENCES `ski_type` (`type_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Begrensninger for tabell `shipments`
--
ALTER TABLE `shipments`
  ADD CONSTRAINT `shipments_ibfk_1` FOREIGN KEY (`transporter`) REFERENCES `transporters` (`user_id`),
  ADD CONSTRAINT `shipments_ibfk_2` FOREIGN KEY (`driver_id`) REFERENCES `driver` (`driver_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Begrensninger for tabell `ski`
--
ALTER TABLE `ski`
  ADD CONSTRAINT `ski_ibfk_1` FOREIGN KEY (`emp_num`) REFERENCES `storekeeper` (`employee_number`),
  ADD CONSTRAINT `ski_ibfk_2` FOREIGN KEY (`type_id`) REFERENCES `ski_type` (`type_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Begrensninger for tabell `storekeeper`
--
ALTER TABLE `storekeeper`
  ADD CONSTRAINT `storekeeper_ibfk_1` FOREIGN KEY (`employee_number`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Begrensninger for tabell `team_skier`
--
ALTER TABLE `team_skier`
  ADD CONSTRAINT `team_skier_ibfk_1` FOREIGN KEY (`emp_num`) REFERENCES `customer_rep` (`employee_number`),
  ADD CONSTRAINT `team_skier_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Begrensninger for tabell `transporters`
--
ALTER TABLE `transporters`
  ADD CONSTRAINT `transporters_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
