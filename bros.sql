-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 06, 2019 at 04:10 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bros`
--

-- --------------------------------------------------------

--
-- Table structure for table `absensi`
--

CREATE TABLE `absensi` (
  `matkul_id` int(11) NOT NULL,
  `dos_id` int(11) DEFAULT NULL,
  `mhs_id` int(11) NOT NULL,
  `p1` varchar(255) DEFAULT NULL,
  `p2` varchar(255) DEFAULT NULL,
  `p3` varchar(255) DEFAULT NULL,
  `p4` varchar(255) DEFAULT NULL,
  `p5` varchar(255) DEFAULT NULL,
  `p6` varchar(255) DEFAULT NULL,
  `p7` varchar(255) DEFAULT NULL,
  `p8` varchar(255) DEFAULT NULL,
  `p9` varchar(255) DEFAULT NULL,
  `p10` varchar(255) DEFAULT NULL,
  `p11` varchar(255) DEFAULT NULL,
  `p12` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `absensi`
--

INSERT INTO `absensi` (`matkul_id`, `dos_id`, `mhs_id`, `p1`, `p2`, `p3`, `p4`, `p5`, `p6`, `p7`, `p8`, `p9`, `p10`, `p11`, `p12`) VALUES
(18, 7, 9, 'k3qH2esGFUvtIIo84IpzuOXpYQRDzEEdikWm6TBZcyY=', 'fczfjYIc6he+4t3D/rEJO8a/qrn7sFKWbJO3SXAoAEc=', 'Xkz+keM6qxTX8esOMD0nYRGpLaReDl5Ban29PB5egXQ=', 'tbNsYXhQuscvyJvsMmfmIEVH0Aby59QTFCi5M2DGjmQ=', '', '', '', '', '', '', '', ''),
(18, 7, 10, 'fZgij0xf314drhxTIZOFgjzPi80QsyN/Zg/zKzx6SWY=', '7AU1AqAAnTn3aOLFpsAUe1sLOHDYoc7MocP491RpE+U=', 'SYt9zJr54xWvNoAZhBYE917aON7OpISc1EVtfQZuXzQ=', 'tipzceJs90HjSYYAYgDVrfbhFd8cG/pXKQxhEKqRaOs=', '', '', '', '', '', '', '', ''),
(18, 7, 11, 'S75GrqKab/S+W1tVe7MEIW/InFAuNWw9ONbtLtgBhBc=', '3VyH1OIVQnP0IKfr+yS6vLJS1xrM5+cjkg55h+a1ssk=', 'cQcGBo7naSTCL3Qo8xj8zloalmdEKg07Fg/i7fHC1Zs=', 'EvzeyPPDj8M0G4gCIZDupm5UG6Bs7tftddwoS93dqfw=', '', '', '', '', '', '', '', ''),
(18, 7, 12, 'nb+7sHBlkkLyOGkJrrEVC64lHYpLmypbXihku0OmzZg=', '4JX4Z5SkGJX2LDW1y3KYu9NrLd1H32ZOiV4Cj0ZPIWk=', 'sjvKJjhS/DuR3DDvgNhjoZV+MKA9xFdkKrmCVc1imLE=', 'r2MQYw9GX3woSKr9HjS57JYMK3HKOaUrvmvjMyUFucE=', '', '', '', '', '', '', '', ''),
(18, 7, 13, 'gR8zjZ1u8UVQz73FWWjlocMajviofqA+DgquZqGoDFU=', 'RMUM/Y29Zr2UznrLndxgPt1t3u2DQeXNuxtFv5r3Jyo=', 'BTAAAgHHKyRLj4UeNBBDvJH5534llRttYDm6/ijg56E=', '1mheRWH/imi/frXXgcd6MUuyTn88VNusBzZryCdKv00=', '', '', '', '', '', '', '', ''),
(18, 7, 14, 'jf41Uwt4AEE0HokBeOsrxJl2N7tGVgD0DCgEphPH1yg=', 'T75LfC6BeT6S8rtA1vAqMXEh7Tsbq56xmdTkEXQXiTo=', 'hUIeU975ZT8xpNrcqXJo3S0ssGQTjzjXEZPAFA6c7DU=', 'CsLKDDzYCpYaA8JxYbuxM5DJ6wZubauOvobtAsxM3pE=', '', '', '', '', '', '', '', ''),
(18, 7, 15, 'UmyFYh4skjKciD9nJ0Uh5cqXdOAeRx9VHe9MfLn0UwM=', 'T20L6+TQVccj8SIMDm7h7QbNQgAbxM+8I+bF1E838l4=', 'JogPDcCIdHR4EZHtzhoMQW22BE6wXgkvzBAOl1PgeTs=', '4VLrhVwvecnohvHk9v2IMp+D+cQxr4XeEYo+rfJkGC4=', '', '', '', '', '', '', '', ''),
(18, 7, 16, '8U9mXYPcvlEwZbgxeYfRj/j//9A5B6vHrtFsFa6atdA=', 'hoDNoRjhwAuklZiJiMTmZumz2HB+eyULCaGEtWPNBfQ=', '7WGzKfryspZcOUcYERuk26iuP98ArOQxG+CWsWmK+/8=', '2AWaehmg/AoDXBmnxJ1PNyph6A7LFe2GThdSc0mNaDA=', '', '', '', '', '', '', '', ''),
(19, 7, 2, '', '', '', '', '', '', '', '', '', '', '', ''),
(19, 7, 3, '', '', '', '', '', '', '', '', '', '', '', ''),
(19, 7, 4, '', '', '', '', '', '', '', '', '', '', '', ''),
(19, 7, 5, '', '', '', '', '', '', '', '', '', '', '', ''),
(19, 7, 6, '', '', '', '', '', '', '', '', '', '', '', ''),
(19, 7, 7, '', '', '', '', '', '', '', '', '', '', '', ''),
(19, 7, 8, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 2, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 3, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 4, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 5, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 6, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 7, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 8, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 9, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 10, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 11, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 12, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 13, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 14, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 15, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 16, '', '', '', '', '', '', '', '', '', '', '', ''),
(20, 8, 20, '', '', '', '', '', '', '', '', '', '', '', ''),
(21, 8, 2, '', '', '', '', '', '', '', '', '', '', '', ''),
(21, 8, 3, '', '', '', '', '', '', '', '', '', '', '', ''),
(21, 8, 4, 'EfYnPbXwpUHuE98z3xv+jx7oplQCSlMpB5QnD9JbxPw=', '', '', '', '', '', '', '', '', '', '', ''),
(21, 8, 5, '', '', '', '', '', '', '', '', '', '', '', ''),
(21, 8, 8, '', '', '', '', '', '', '', '', '', '', '', ''),
(21, 8, 12, 'Gyva2Y0ieYzqZ5tB1zH/SHCKJPJUb1iJrpYpU1EVfn4=', '', '', '', '', '', '', '', '', '', '', ''),
(21, 8, 14, 'DTGb3SYcXqy2sP4IS9hSzJkIKP1wAXdYXqdUR/S+Hzk=', '', '', '', '', '', '', '', '', '', '', ''),
(21, 8, 15, '+zNnFQkUlcD36Mgq7Vo3V2v06hf5dF2wBwLTsz68MDE=', '', '', '', '', '', '', '', '', '', '', ''),
(21, 8, 20, 'Vf/vKe0Z+fg4wlfsOugPoCJ8zT+9w2i3fut4pLuaiHE=', '', '', '', '', '', '', '', '', '', '', ''),
(21, 8, 21, '6DcWPtjrycGdfBFonJ7At81BiGVzR5fIa5L4xR9Mbac=', '', '', '', '', '', '', '', '', '', '', ''),
(21, 8, 22, '', '', '', '', '', '', '', '', '', '', '', ''),
(21, 8, 23, '', '', '', '', '', '', '', '', '', '', '', ''),
(21, 8, 24, 'fbYsE4luP3/RWYbbv92K3DxtBsMJ46Y40HBvwVCZBhU=', '', '', '', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `dosen_pengajar`
--

CREATE TABLE `dosen_pengajar` (
  `id` int(11) NOT NULL,
  `nip` varchar(255) DEFAULT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `no_telp` varchar(255) DEFAULT NULL,
  `jurusan` varchar(255) DEFAULT NULL,
  `fakultas` varchar(255) DEFAULT NULL,
  `img_path` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dosen_pengajar`
--

INSERT INTO `dosen_pengajar` (`id`, `nip`, `nama`, `no_telp`, `jurusan`, `fakultas`, `img_path`) VALUES
(7, '197201102008121001', 'Dr. I Ketut Gede Suhartana, S.Kom., M.Kom.', '123456789', 'Ilmu Komputer', 'MIPA', 'Data Dosen/Foto Profil/197201102008121001.jpg'),
(8, '197806212006041002', 'Cokorda Rai Adi Pramartha, S.T., M.M., Ph.D.', '123456789', 'Ilmu Komputer', 'MIPA', 'Data Dosen/Foto Profil/197806212006041002.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `id` int(11) NOT NULL,
  `nim` varchar(255) DEFAULT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `no_telp` varchar(255) DEFAULT NULL,
  `mac_addr` varchar(255) DEFAULT NULL,
  `fakultas` varchar(255) DEFAULT NULL,
  `jurusan` varchar(255) DEFAULT NULL,
  `angkatan` int(11) DEFAULT NULL,
  `img_path` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`id`, `nim`, `nama`, `no_telp`, `mac_addr`, `fakultas`, `jurusan`, `angkatan`, `img_path`) VALUES
(2, '1508605007', 'Ida Bagus Andika Putra', '081558743063', 'F8:95:EA:8C:43:F6', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605007.jpg'),
(3, '1508605035', 'I Gede Pradistya Adisaputra', '082247807922', '20:34:fb:ef:5d:99', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605035.jpg'),
(4, '1508605014', 'Made Dwi Ariyawan', '081246617461', '50:8F:4C:32:5D:FE', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605014.jpg'),
(5, '1508605026', 'A.A. RIKY MAHENDRA', '482169', '9c:6b:72:55:7e:1c', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605026.jpg'),
(6, '1508605016', 'Ni Putu Ary Rara Iswari', '081236854002', '20:5E:F7:95:CC:DF', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605016.jpg'),
(7, '1508605025', 'I Made Bayu Dharma Wibawa', '087866896861', '50:29:f5:da:90:0c', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605025.jpg'),
(8, '1508605043', 'Ida Bagus Naradhipa Pidada', '081239473344', 'a8:5C:2C:67:FC:43', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605043.jpg'),
(9, '1508605033', 'I Made Pradnyanandana Suwitra', '085792447863', '4C:ED:FB:22:F2:23', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605033.jpg'),
(10, '1508605002', 'I Dewa Gede Budiastawa ', '089635922035', 'A4:D9:90:15:BF:B0', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605002.jpg'),
(11, '1508605028', 'Ketut Yogi Prasetya', '081239898758', '54:40:AD:A0:A0:2B', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605028.jpg'),
(12, '1508605018', 'Made Mas Adi Winata', '0895341586838', 'dc:f0:90:27:48:19', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605018.jpg'),
(13, '1508605051', 'I Komang Raka Dewantara', '081318072990', 'ec:d0:9f:4a:66:98', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605051.jpg'),
(14, '1508605041 ', 'I Wayan Aditya Anggara Putra ', '08970218036 \n', '8C:BE:BE:16:A5:AE', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605041 .jpg'),
(15, '1508605045', 'I Wayan Bhaskara Budi Yoga', '081238567603', '48:2C:A0:35:05:91', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605045.jpg'),
(16, '1508605004', 'Agung Rahadian Putra', '081658979465', '94:65:2D:97:FD:3E', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605004.jpg'),
(20, '1508605058', 'Yoel Samosir', '082144968180', '0C:98:38:7E:DF:1E', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605058.jpg'),
(21, '1508605055', 'Made Yoga Priyanta', '081333555666', '48:2C:A0:E4:8A:40', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605055.jpg'),
(22, '1508605003', 'Nyoman Wiratma Jaya', '08123698741', 'A4:50:46:61:B4:76', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605003.jpg'),
(23, '1508605006', 'I Made Santa Yana', '081234568791', 'A4:D9:90:1D:E6:96', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605006.jpg'),
(24, '1508605034', 'Putu Yasa Utama', '081234567891', '50:8F:4C:32:46:BB', 'MIPA', 'Ilmu Komputer', 2015, 'Data Mahasiswa/Foto Profil/1508605034.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `mata_kuliah`
--

CREATE TABLE `mata_kuliah` (
  `id` int(11) NOT NULL,
  `kode` varchar(255) DEFAULT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `id_dosen` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mata_kuliah`
--

INSERT INTO `mata_kuliah` (`id`, `kode`, `nama`, `id_dosen`) VALUES
(18, 'IF1650063', 'Interaksi Manusia dan Komputer', 7),
(19, 'IF801543', 'Ergonomi Terapan', 7),
(20, 'IF1670022', 'Komputer dan Masyarakat', 8),
(21, 'zone', 'Futsal', 8);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `mhs_dos_id` int(11) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `mhs_dos_id`, `username`, `password`, `role`) VALUES
(1, NULL, 'admin', '21232f297a57a5a743894a0e4a801fc3', 'admin'),
(6, 4, '1508605014', '4424d2deec2f9468fb61e2db07ecd6b6', 'mahasiswa'),
(8, 6, '1508605016', '7e3315fe390974fcf25e44a9445bd821', 'mahasiswa'),
(10, 8, '1508605043', 'b6f8dc086b2d60c5856e4ff517060392', 'mahasiswa'),
(11, 9, '1508605033', '91c77393975889bd08f301c9e13a44b7', 'mahasiswa'),
(12, 10, '1508605002', '415585bd389b69659223807d77a96791', 'mahasiswa'),
(13, 11, '1508605028', 'bf8dd8c68d02e161c28dc9ea139d4784', 'mahasiswa'),
(14, 12, '1508605018', '71463aaacf046fa24e7dfa4558607545', 'mahasiswa'),
(15, 13, '1508605051', '744878fbdd26871c594f57ca61733e09', 'mahasiswa'),
(16, 14, '1508605041 ', 'c7502c55f8db540625b59d9a42638520', 'mahasiswa'),
(17, 15, '1508605045', '56bd37d3a2fda0f2f41925019c81011d', 'mahasiswa'),
(18, 16, '1508605004', '3202111cf90e7c816a472aaceb72b0df', 'mahasiswa'),
(27, 7, 'dosen1', 'f499263a253447dd5cb68dafb9f13235', 'dosen'),
(28, 8, 'dosen2', 'ac41c4e0e6ef7ac51f0c8f3895f82ce5', 'dosen'),
(29, 2, '1508605007', '351869bde8b9d6ad1e3090bd173f600d', 'mahasiswa'),
(30, 3, '1508605035', 'aac933717a429f57c6ca58f32975c597', 'mahasiswa'),
(31, 5, '1508605026', 'f02208a057804ee16ac72ff4d3cec53b', 'mahasiswa'),
(32, 7, '1508605025', 'b6e584419a62da6229cf347e5ccfa166', 'mahasiswa'),
(33, 20, '1508605058', '7ffb4e0ece07869880d51662a2234143', 'mahasiswa'),
(34, 21, '1508605055', 'be6ad8761fe4eb9bb85934a2d21686bb', 'mahasiswa'),
(35, 22, '1508605003', '240ac9371ec2671ae99847c3ae2e6384', 'mahasiswa'),
(36, 23, '1508605006', '2c27a260f16ad3098393cc529f391f4a', 'mahasiswa'),
(37, 24, '1508605034', '2e2079d63348233d91cad1fa9b1361e9', 'mahasiswa');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `absensi`
--
ALTER TABLE `absensi`
  ADD PRIMARY KEY (`matkul_id`,`mhs_id`);

--
-- Indexes for table `dosen_pengajar`
--
ALTER TABLE `dosen_pengajar`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mata_kuliah`
--
ALTER TABLE `mata_kuliah`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dosen_pengajar`
--
ALTER TABLE `dosen_pengajar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `mata_kuliah`
--
ALTER TABLE `mata_kuliah`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
