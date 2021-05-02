
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL,
  `customer_name` varchar(45) DEFAULT NULL,
  `governrate` varchar(10) DEFAULT NULL,
  `town` varchar(10) DEFAULT NULL,
  `street_number` varchar(10) DEFAULT NULL,
  `balance` decimal(7,3) DEFAULT NULL,
  `sp_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `customer_name`, `governrate`, `town`, `street_number`, `balance`, `sp_id`) VALUES
(1, 'islam', 'cairo', 'mahalla', '14', '140.000', 1),
(2, 'kareem', 'gharbia', 'tanta', '17', '200.000', 1),
(3, 'taha', 'cairo', 'nasr city', '18', '170.000', 2);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL,
  `order_date` date DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_id`, `order_date`, `customer_id`) VALUES
(1, '2010-04-15', 1),
(2, '2011-05-25', 2),
(3, '2012-06-10', 1);

-- --------------------------------------------------------

--
-- Table structure for table `orders_product`
--

CREATE TABLE `orders_product` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders_product`
--

INSERT INTO `orders_product` (`id`, `order_id`, `product_id`) VALUES
(1, 1, 2),
(2, 2, 2),
(3, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL,
  `product_desc` varchar(45) DEFAULT NULL,
  `product_class` varchar(45) DEFAULT NULL,
  `price` decimal(7,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `product_desc`, `product_class`, `price`) VALUES
(1, 'mobile', 'samsung mobile', '1500.000'),
(2, 'car', 'mercedes car', '5000.000'),
(3, 'bike', 'auto bike', '550.000');

-- --------------------------------------------------------

--
-- Table structure for table `product_store`
--

CREATE TABLE `product_store` (
  `id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `store_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product_store`
--

INSERT INTO `product_store` (`id`, `product_id`, `store_number`) VALUES
(1, 1, 2),
(2, 2, 2),
(3, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `salesperson`
--

CREATE TABLE `salesperson` (
  `sp_id` int(11) NOT NULL,
  `sp_name` varchar(40) DEFAULT NULL,
  `governrate` varchar(10) DEFAULT NULL,
  `town` varchar(10) DEFAULT NULL,
  `street_number` varchar(10) DEFAULT NULL,
  `commission_rate` decimal(7,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `salesperson`
--

INSERT INTO `salesperson` (`sp_id`, `sp_name`, `governrate`, `town`, `street_number`, `commission_rate`) VALUES
(1, ' muhammed ali', 'cairo', 'nasr city', '12', '2.500'),
(2, 'ayman ahmed', 'cairo', 'giza', '11', '2.300'),
(3, 'ahmed ali', 'aswan', NULL, NULL, '1.500');

-- --------------------------------------------------------

--
-- Table structure for table `storehouse`
--

CREATE TABLE `storehouse` (
  `store_number` int(11) NOT NULL,
  `store_place` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `storehouse`
--

INSERT INTO `storehouse` (`store_number`, `store_place`) VALUES
(1, 'cairo'),
(2, 'alex'),
(3, 'tahrir');


ALTER TABLE `customer`
  ADD PRIMARY KEY (`customer_id`),
  ADD KEY `sp_id` (`sp_id`);

ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `customer_id` (`customer_id`);

ALTER TABLE `orders_product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `product_id` (`product_id`);

ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`);

ALTER TABLE `product_store`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_id2` (`product_id`),
  ADD KEY `store_number` (`store_number`);

ALTER TABLE `salesperson`
  ADD PRIMARY KEY (`sp_id`);

ALTER TABLE `storehouse`
  ADD PRIMARY KEY (`store_number`);


ALTER TABLE `customer`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `orders`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `orders_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `product`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `product_store`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `salesperson`
  MODIFY `sp_id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `storehouse`
  MODIFY `store_number` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `customer`
  ADD CONSTRAINT `sp_id` FOREIGN KEY (`sp_id`) REFERENCES `salesperson` (`sp_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `orders`
  ADD CONSTRAINT `customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `orders_product`
  ADD CONSTRAINT `order_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `product_store`
  ADD CONSTRAINT `product_id2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `store_number` FOREIGN KEY (`store_number`) REFERENCES `storehouse` (`store_number`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;
