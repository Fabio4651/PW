-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 10-Jan-2021 às 23:26
-- Versão do servidor: 10.4.17-MariaDB
-- versão do PHP: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `pw`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `example`
--

CREATE TABLE `example` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `example`
--

INSERT INTO `example` (`id`, `name`) VALUES
(1, 'Diego'),
(2, 'Zman');

-- --------------------------------------------------------

--
-- Estrutura da tabela `property`
--

CREATE TABLE `property` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `size` varchar(45) DEFAULT NULL,
  `beds` int(11) DEFAULT NULL,
  `baths` int(11) DEFAULT NULL,
  `garagenumber` int(11) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  `img` varchar(45) DEFAULT NULL,
  `owner` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `property`
--

INSERT INTO `property` (`id`, `name`, `size`, `beds`, `baths`, `garagenumber`, `description`, `price`, `location`, `img`, `owner`) VALUES
(1, 'casa com varanda', '500', 3, 2, 1, 'very comfy house', '500.000', 'Lagoa', NULL, 1),
(2, 'penthouse', '420', 1, 1, 0, 'bruh', '250.000', 'Silves', NULL, 2),
(3, 'diego', '333', 2, 2, 66, 'ssssssssssss', '2222', 'PTM', 'static/upload/1.jpg', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `sessions`
--

CREATE TABLE `sessions` (
  `id` int(11) NOT NULL,
  `session_id` varchar(255) DEFAULT NULL,
  `data` blob DEFAULT NULL,
  `expiry` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `sessions`
--

INSERT INTO `sessions` (`id`, `session_id`, `data`, `expiry`) VALUES
(7, 'session:fab1249a-0c6f-4007-a314-26e10e0a96ea', 0x8004952b000000000000007d94288c0a5f7065726d616e656e7494888c08757365726e616d65948c0a446965676f2053496c6194752e, '2021-02-10 21:23:40');

-- --------------------------------------------------------

--
-- Estrutura da tabela `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `img` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `phone`, `img`, `password`) VALUES
(1, 'Diego SIla', 'diegosila@gmail.com', 966969696, 'diegosila.png', 'diego'),
(2, 'ZMANE', 'zman@gmail.com', 963563254, NULL, 'zman'),
(3, 'fabio', 'fasf@gmail.com', 963582415, 'static/upload/1.jpg', NULL),
(6, 'lanso', 'lanso@gmail.com', 965326584, 'static/upload/4.jpg', 'lanso');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `property`
--
ALTER TABLE `property`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_UNIQUE` (`id`),
  ADD KEY `owner_idx` (`owner`);

--
-- Índices para tabela `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `session_id` (`session_id`);

--
-- Índices para tabela `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `property`
--
ALTER TABLE `property`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `sessions`
--
ALTER TABLE `sessions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `property`
--
ALTER TABLE `property`
  ADD CONSTRAINT `owner` FOREIGN KEY (`owner`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
