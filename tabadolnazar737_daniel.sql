-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: services.irn10.chabokan.net:31237
-- Generation Time: Jul 14, 2026 at 07:52 AM
-- Server version: 8.0.29
-- PHP Version: 8.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tabadolnazar737_daniel`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_profile`
--

CREATE TABLE `accounts_profile` (
  `id` bigint NOT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `nickname` varchar(50) NOT NULL,
  `bio` longtext NOT NULL,
  `child_age` int DEFAULT NULL,
  `condition_type` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `show_bio` tinyint(1) NOT NULL,
  `show_child_age` tinyint(1) NOT NULL,
  `show_condition_type` tinyint(1) NOT NULL,
  `show_location` tinyint(1) NOT NULL,
  `user_id` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `accounts_profile`
--

INSERT INTO `accounts_profile` (`id`, `avatar`, `nickname`, `bio`, `child_age`, `condition_type`, `location`, `show_bio`, `show_child_age`, `show_condition_type`, `show_location`, `user_id`, `created_at`, `updated_at`) VALUES
(1, 'avatars/134.jpg', '', 'با سلام این سایت در حال تست می باشد', 16, 'خیلی شدید', 'کرج', 1, 1, 1, 1, 1, '2026-07-09 06:20:22.851799', '2026-07-09 06:49:57.267344'),
(2, 'avatars/1000903089.jpg', '', '', NULL, '', '', 1, 1, 1, 1, 2, '2026-07-09 06:20:22.851799', '2026-07-09 06:20:22.947560'),
(3, '', '', '', NULL, '', '', 1, 1, 1, 1, 3, '2026-07-09 06:20:22.851799', '2026-07-11 07:33:33.872153'),
(4, '', '', '', NULL, '', '', 1, 1, 1, 1, 4, '2026-07-09 06:20:22.851799', '2026-07-09 06:20:22.947560'),
(5, 'avatars/IMG_20250909_211129.jpg', '', '', NULL, '', '', 1, 1, 1, 1, 5, '2026-07-09 08:13:32.148726', '2026-07-09 08:14:00.272459'),
(6, '', '', '', NULL, '', '', 1, 1, 1, 1, 6, '2026-07-09 08:49:23.781371', '2026-07-09 08:49:23.881903');

-- --------------------------------------------------------

--
-- Table structure for table `accounts_report`
--

CREATE TABLE `accounts_report` (
  `id` bigint NOT NULL,
  `reason` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `reported_user_id` int NOT NULL,
  `reporter_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add profile', 7, 'add_profile'),
(26, 'Can change profile', 7, 'change_profile'),
(27, 'Can delete profile', 7, 'delete_profile'),
(28, 'Can view profile', 7, 'view_profile'),
(29, 'Can add report', 8, 'add_report'),
(30, 'Can change report', 8, 'change_report'),
(31, 'Can delete report', 8, 'delete_report'),
(32, 'Can view report', 8, 'view_report'),
(33, 'Can add دسته‌بندی', 9, 'add_category'),
(34, 'Can change دسته‌بندی', 9, 'change_category'),
(35, 'Can delete دسته‌بندی', 9, 'delete_category'),
(36, 'Can view دسته‌بندی', 9, 'view_category'),
(37, 'Can add موضوع', 10, 'add_post'),
(38, 'Can change موضوع', 10, 'change_post'),
(39, 'Can delete موضوع', 10, 'delete_post'),
(40, 'Can view موضوع', 10, 'view_post'),
(41, 'Can add نظر', 11, 'add_comment'),
(42, 'Can change نظر', 11, 'change_comment'),
(43, 'Can delete نظر', 11, 'delete_comment'),
(44, 'Can view نظر', 11, 'view_comment'),
(45, 'Can add access attempt', 12, 'add_accessattempt'),
(46, 'Can change access attempt', 12, 'change_accessattempt'),
(47, 'Can delete access attempt', 12, 'delete_accessattempt'),
(48, 'Can view access attempt', 12, 'view_accessattempt'),
(49, 'Can add access log', 13, 'add_accesslog'),
(50, 'Can change access log', 13, 'change_accesslog'),
(51, 'Can delete access log', 13, 'delete_accesslog'),
(52, 'Can view access log', 13, 'view_accesslog'),
(53, 'Can add access failure', 14, 'add_accessfailurelog'),
(54, 'Can change access failure', 14, 'change_accessfailurelog'),
(55, 'Can delete access failure', 14, 'delete_accessfailurelog'),
(56, 'Can view access failure', 14, 'view_accessfailurelog'),
(57, 'Can add access attempt expiration', 15, 'add_accessattemptexpiration'),
(58, 'Can change access attempt expiration', 15, 'change_accessattemptexpiration'),
(59, 'Can delete access attempt expiration', 15, 'delete_accessattemptexpiration'),
(60, 'Can view access attempt expiration', 15, 'view_accessattemptexpiration');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$870000$jTBkSDZ5dmHbzawFYJkKQR$yE4b4F/kE5XX9/dLSP7AuieR5d29mOHWWDhGGXEYYs0=', '2026-07-09 06:49:57.250136', 0, 'javad', 'جواد', '', 'javadfaramarzi386@gmail.com', 0, 1, '2026-07-07 06:07:03.511010'),
(2, 'pbkdf2_sha256$870000$vZTg0LE7xKngucYSJjUDFC$nR1J01zVnpQ3oQlCJiwDPfXq7HIj3caW5k7Pm6Rlt+8=', '2026-07-07 08:02:51.574471', 0, 'Farhad', 'فرهاد', '', 'javadfaramarzi386@gmail.com', 0, 1, '2026-07-07 08:01:21.848124'),
(3, 'pbkdf2_sha256$870000$dMPIvHqXEzSQg8QESk2MgV$NboVLkjcUh7O6wXHmvKuJB5isb1NFWxQDE6Ayr2R3zg=', '2026-07-11 07:33:33.848535', 1, 'javad_admin', '', '', '', 1, 1, '2026-07-07 10:55:17.272341'),
(4, 'pbkdf2_sha256$870000$fvDxsfgL0tc6rRddTrHUVa$9MXB9zjJFenMYbR1dm4lxA4xjTNxB7WzS6Frbx+MWRU=', '2026-07-07 14:10:17.163997', 0, 'Zeinabmadadi', 'زینب', '', 'zeinabmadadi386@gmail.com', 0, 1, '2026-07-07 14:10:09.881556'),
(5, 'pbkdf2_sha256$870000$erOLudCIOiItnzK5RIooEe$iOwPiwV0B8EQY4OB+ijZ34wRa0WynRLEm8seQ5e0RNM=', '2026-07-09 08:13:32.171902', 0, 'Farimah', 'فریماه', '', 'faramarzi@outlook.com', 0, 1, '2026-07-09 08:13:31.251494'),
(6, 'pbkdf2_sha256$870000$FIxhe64ekZM3ScOPjfYtw1$COIBhzQ8Eio600BFyQegcORSRVvfMu0vEqT3M0kpuQk=', '2026-07-09 08:49:23.876744', 0, 'Farimah2', 'فریماه2', '', 'javadfaramarzi3863@gmail.com', 0, 1, '2026-07-09 08:49:15.311395');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `axes_accessattempt`
--

CREATE TABLE `axes_accessattempt` (
  `id` int NOT NULL,
  `user_agent` varchar(255) NOT NULL,
  `ip_address` char(39) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `http_accept` varchar(1025) NOT NULL,
  `path_info` varchar(255) NOT NULL,
  `attempt_time` datetime(6) NOT NULL,
  `get_data` longtext NOT NULL,
  `post_data` longtext NOT NULL,
  `failures_since_start` int UNSIGNED NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `axes_accessattemptexpiration`
--

CREATE TABLE `axes_accessattemptexpiration` (
  `access_attempt_id` int NOT NULL,
  `expires_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `axes_accessfailurelog`
--

CREATE TABLE `axes_accessfailurelog` (
  `id` int NOT NULL,
  `user_agent` varchar(255) NOT NULL,
  `ip_address` char(39) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `http_accept` varchar(1025) NOT NULL,
  `path_info` varchar(255) NOT NULL,
  `attempt_time` datetime(6) NOT NULL,
  `locked_out` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `axes_accesslog`
--

CREATE TABLE `axes_accesslog` (
  `id` int NOT NULL,
  `user_agent` varchar(255) NOT NULL,
  `ip_address` char(39) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `http_accept` varchar(1025) NOT NULL,
  `path_info` varchar(255) NOT NULL,
  `attempt_time` datetime(6) NOT NULL,
  `logout_time` datetime(6) DEFAULT NULL,
  `session_hash` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `axes_accesslog`
--

INSERT INTO `axes_accesslog` (`id`, `user_agent`, `ip_address`, `username`, `http_accept`, `path_info`, `attempt_time`, `logout_time`, `session_hash`) VALUES
(1, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36', '127.0.0.1', 'javad_admin', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', '/admin/login/', '2026-07-11 07:33:33.729678', NULL, 'e32d855143aef3982cd2b22201a6c10e300ca07a8366f8748d0a723d122d91c2');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'accounts', 'profile'),
(8, 'accounts', 'report'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(12, 'axes', 'accessattempt'),
(15, 'axes', 'accessattemptexpiration'),
(14, 'axes', 'accessfailurelog'),
(13, 'axes', 'accesslog'),
(5, 'contenttypes', 'contenttype'),
(9, 'forum', 'category'),
(11, 'forum', 'comment'),
(10, 'forum', 'post'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-07-07 05:47:18.790257'),
(2, 'auth', '0001_initial', '2026-07-07 05:47:21.528141'),
(3, 'accounts', '0001_initial', '2026-07-07 05:47:22.269989'),
(4, 'admin', '0001_initial', '2026-07-07 05:47:23.061320'),
(5, 'admin', '0002_logentry_remove_auto_add', '2026-07-07 05:47:23.171436'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2026-07-07 05:47:23.286477'),
(7, 'contenttypes', '0002_remove_content_type_name', '2026-07-07 05:47:23.925201'),
(8, 'auth', '0002_alter_permission_name_max_length', '2026-07-07 05:47:24.134014'),
(9, 'auth', '0003_alter_user_email_max_length', '2026-07-07 05:47:24.321357'),
(10, 'auth', '0004_alter_user_username_opts', '2026-07-07 05:47:24.428481'),
(11, 'auth', '0005_alter_user_last_login_null', '2026-07-07 05:47:24.733691'),
(12, 'auth', '0006_require_contenttypes_0002', '2026-07-07 05:47:24.829564'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2026-07-07 05:47:24.938930'),
(14, 'auth', '0008_alter_user_username_max_length', '2026-07-07 05:47:25.227291'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2026-07-07 05:47:25.540883'),
(16, 'auth', '0010_alter_group_name_max_length', '2026-07-07 05:47:25.750499'),
(17, 'auth', '0011_update_proxy_permissions', '2026-07-07 05:47:26.083586'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2026-07-07 05:47:26.285484'),
(19, 'forum', '0001_initial', '2026-07-07 05:47:28.900448'),
(20, 'forum', '0002_create_default_categories', '2026-07-07 05:47:31.906438'),
(21, 'forum', '0003_category_color_category_icon_category_image', '2026-07-07 05:47:32.135277'),
(22, 'forum', '0004_alter_post_options_category_is_visible_and_more', '2026-07-07 05:47:34.189480'),
(23, 'sessions', '0001_initial', '2026-07-07 05:47:34.471221'),
(24, 'accounts', '0002_alter_profile_options_alter_report_options_and_more', '2026-07-09 06:20:23.035046'),
(25, 'forum', '0005_alter_category_image', '2026-07-09 06:20:23.045498'),
(26, 'axes', '0001_initial', '2026-07-09 09:07:54.759044'),
(27, 'axes', '0002_auto_20151217_2044', '2026-07-09 09:07:55.028052'),
(28, 'axes', '0003_auto_20160322_0929', '2026-07-09 09:07:55.077147'),
(29, 'axes', '0004_auto_20181024_1538', '2026-07-09 09:07:55.105571'),
(30, 'axes', '0005_remove_accessattempt_trusted', '2026-07-09 09:07:55.165553'),
(31, 'axes', '0006_remove_accesslog_trusted', '2026-07-09 09:07:55.242981'),
(32, 'axes', '0007_alter_accessattempt_unique_together', '2026-07-09 09:07:55.382646'),
(33, 'axes', '0008_accessfailurelog', '2026-07-09 09:07:55.625934'),
(34, 'axes', '0009_add_session_hash', '2026-07-09 09:07:56.029592'),
(35, 'axes', '0010_accessattemptexpiration', '2026-07-09 09:07:56.283661');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('99p073h3p7qp7e1y2nmow38jvayprl1i', '.eJxVjEEOwiAURO_C2hCggB-X7j0D-cBHqgaS0q6Md5cmXehuMu_NvJnHbS1-67T4ObELU-z02wWMT6o7SA-s98Zjq-syB74r_KCd31qi1_Vw_w4K9jLW2UmXHWiRJjMJSc44Ja3SFC2giGhHkFkOMIEB1KBTwLMhhSYDCcE-X8MAN08:1wh0km:NZ_-rhoTP-6Z7c2IFUivJh1VJYBo7KNvMV8w18gR9qY', '2026-07-21 08:02:04.361833'),
('c0lsrz5772ff6wpddjeulipwo1agz6sn', '.eJxVjEEOwiAQRe_C2hBmaEtw6d4zkIHOSNVAUtpV490NSRe6_e-9f6hA-5bD3ngNy6yuCtTld4uUXlw6mJ9UHlWnWrZ1ibor-qRN3-vM79vp_h1karnXhkRYwDkzDYg-WSJBiWTjaMm4aCWBcPIo4D3jwDCKYXDgJm8A1ecLBnw4IQ:1whia5:hk9VWSZKe_73c270vjG7p9nSYHpDTyZNp5di-5wC-_8', '2026-07-23 06:49:57.282631'),
('f4y6jl6z9ukw0yo31xl7y23hjtq9xcuw', '.eJxVjEEOwiAQRe_C2hCYAgWX7j0DGWZAqoYmpV0Z765NutDtf-_9l4i4rTVuPS9xYnEWTpx-t4T0yG0HfMd2myXNbV2mJHdFHrTL68z5eTncv4OKvX5rHUAZC6YAE1AwZiTNIzlSYCyyheKTH5gLJV8sKk1K5SFlDkUHB0W8P9omOCs:1whkRf:CVV5XgswJGdjnY2AbSOgY6Xwqua9BMzaFdQOIOT0uaw', '2026-07-23 08:49:23.963487'),
('japge438vog1a18d8zirk8o547smqywv', '.eJxVjMsOwiAUBf-FtSEEKA-X7v0Gwn0gVQNJaVfGf9cmXej2zMx5iZS3taZt8JJmEmdhxel3g4wPbjuge263LrG3dZlB7oo86JDXTvy8HO7fQc2jfmuFXiskMugjeKsJIeRgMEZXCujoQHEIyBCJlMaJHRuli-bJmGLBifcHAZI4ng:1wh6V7:G_E4oY8r_nU3ytC4C01WSEmfHyD57Mm9ynHqZ_phxM4', '2026-07-21 14:10:17.170357'),
('jcd57qwt7smfzbj18odn968h5k7nd0g8', '.eJxVjEEOwiAURO_C2hCggB-X7j0D-cBHqgaS0q6Md5cmXehuMu_NvJnHbS1-67T4ObELU-z02wWMT6o7SA-s98Zjq-syB74r_KCd31qi1_Vw_w4K9jLW2UmXHWiRJjMJSc44Ja3SFC2giGhHkFkOMIEB1KBTwLMhhSYDCcE-X8MAN08:1wh0kH:SkdRodlCSf754195ZfEfmHf1h0mlYE5RozuFwwcgvlw', '2026-07-21 08:01:33.185288'),
('ltjr0ed35indlf7ficsabeit5tinddh1', '.eJxVjDkOwjAUBe_iGlnerVDScwbrLzYOIFuKkwpxd4iUAto3M-8lEmxrTdvIS5pZnIUVp98NgR657YDv0G5dUm_rMqPcFXnQIa-d8_NyuH8HFUb91m4CpU3WTM6rHAG1m8jaCCpyUORCwRJ9MdZj1mgiRSDLAKGogOxRvD_jWzh1:1wiSDN:Lnnl0fZFFOUoQi5sKWss_LjvDHEE89nYBgJEfKYMzhE', '2026-07-25 07:33:33.882662'),
('n9xtfn7b3ad8kouez2v7lun1z06e3xnq', '.eJxVjEEOwiAURO_C2hCggB-X7j0D-cBHqgaS0q6Md5cmXehuMu_NvJnHbS1-67T4ObELU-z02wWMT6o7SA-s98Zjq-syB74r_KCd31qi1_Vw_w4K9jLW2UmXHWiRJjMJSc44Ja3SFC2giGhHkFkOMIEB1KBTwLMhhSYDCcE-X8MAN08:1wh0kd:iyLwjbde5n6Qn8q9j-Si_VIA1BU8A6L_KPdHIgSXZE0', '2026-07-21 08:01:55.759940'),
('sy6e54m1rz8fkqomck654ga2yqrgvgsx', '.eJxVjEEOwiAURO_C2hCggB-X7j0D-cBHqgaS0q6Md5cmXehuMu_NvJnHbS1-67T4ObELU-z02wWMT6o7SA-s98Zjq-syB74r_KCd31qi1_Vw_w4K9jLW2UmXHWiRJjMJSc44Ja3SFC2giGhHkFkOMIEB1KBTwLMhhSYDCcE-X8MAN08:1wh0lX:dkleA887-Kh32Ca_M6YKSxy2HL77YX-MzJgAWHFm_9w', '2026-07-21 08:02:51.661728'),
('tb886vlltnnihdt5b6ewnhko79hv8cxq', '.eJxVjEEOwiAURO_C2hCggB-X7j0D-cBHqgaS0q6Md5cmXehuMu_NvJnHbS1-67T4ObELU-z02wWMT6o7SA-s98Zjq-syB74r_KCd31qi1_Vw_w4K9jLW2UmXHWiRJjMJSc44Ja3SFC2giGhHkFkOMIEB1KBTwLMhhSYDCcE-X8MAN08:1wh0lM:PhlXH8lf07tvp_0jeR7nM8RISL3kyax4KfTxuPMy4mY', '2026-07-21 08:02:40.174515');

-- --------------------------------------------------------

--
-- Table structure for table `forum_category`
--

CREATE TABLE `forum_category` (
  `id` bigint NOT NULL,
  `name` varchar(100) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `display_order` int UNSIGNED NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `parent_id` bigint DEFAULT NULL,
  `color` varchar(20) NOT NULL,
  `icon` varchar(100) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `is_visible` tinyint(1) NOT NULL
) ;

--
-- Dumping data for table `forum_category`
--

INSERT INTO `forum_category` (`id`, `name`, `slug`, `description`, `display_order`, `is_active`, `parent_id`, `color`, `icon`, `image`, `is_visible`) VALUES
(1, 'انواع معلولیت', 'disabilities', '', 1, 1, NULL, '#0d6efd', '', NULL, 1),
(2, 'اوتیسم', 'autism', '', 2, 1, 1, '#0d6efd', '', NULL, 1),
(3, 'سندرم داون', 'down-syndrome', '', 3, 1, 1, '#0d6efd', '', NULL, 1),
(4, 'سندرم کری دو شا', 'cri-du-chat', '', 4, 1, 1, '#0d6efd', '', NULL, 1),
(5, 'فلج مغزی', 'cerebral-palsy', '', 5, 1, 1, '#0d6efd', '', NULL, 1),
(6, 'کم‌توانی ذهنی', 'intellectual-disability', '', 6, 1, 1, '#0d6efd', '', NULL, 1),
(7, 'اختلال بینایی', 'visual-impairment', '', 7, 1, 1, '#0d6efd', '', NULL, 1),
(8, 'اختلال شنوایی', 'hearing-impairment', '', 8, 1, 1, '#0d6efd', '', NULL, 1),
(9, 'درمان', 'treatment', '', 9, 1, NULL, '#0d6efd', '', NULL, 1),
(10, 'کاردرمانی', 'occupational-therapy', '', 10, 1, 9, '#0d6efd', '', NULL, 1),
(11, 'گفتاردرمانی', 'speech-therapy', '', 11, 1, 9, '#0d6efd', '', NULL, 1),
(12, 'فیزیوتراپی', 'physiotherapy', '', 12, 1, 9, '#0d6efd', '', NULL, 1),
(13, 'روانشناسی', 'psychology', '', 13, 1, 9, '#0d6efd', '', NULL, 1),
(14, 'آموزش', 'education', '', 14, 1, NULL, '#0d6efd', '', NULL, 1),
(15, 'آموزش در خانه', 'home-education', '', 15, 1, 14, '#0d6efd', '', NULL, 1),
(16, 'مدرسه', 'school', '', 16, 1, 14, '#0d6efd', '', NULL, 1),
(17, 'مهارت های زندگی', 'life-skills', '', 17, 1, 14, '#0d6efd', '', NULL, 1),
(18, 'بازی درمانی', 'play-therapy', '', 18, 1, 14, '#0d6efd', '', NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `forum_comment`
--

CREATE TABLE `forum_comment` (
  `id` bigint NOT NULL,
  `content` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_approved` tinyint(1) NOT NULL,
  `author_id` int NOT NULL,
  `post_id` bigint NOT NULL,
  `is_edited` tinyint(1) NOT NULL,
  `parent_id` bigint DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `forum_comment`
--

INSERT INTO `forum_comment` (`id`, `content`, `created_at`, `is_approved`, `author_id`, `post_id`, `is_edited`, `parent_id`, `updated_at`) VALUES
(1, 'سلام', '2026-07-07 08:03:10.029926', 1, 2, 1, 0, NULL, '2026-07-07 08:03:10.029971'),
(2, '👍🏻', '2026-07-07 14:14:38.276895', 1, 4, 1, 0, NULL, '2026-07-07 14:14:38.276921'),
(3, 'سلام', '2026-07-09 08:14:22.895562', 1, 5, 2, 0, NULL, '2026-07-09 08:14:22.895617'),
(4, 'Hi', '2026-07-09 08:14:50.047086', 1, 5, 1, 0, NULL, '2026-07-09 08:14:50.047141');

-- --------------------------------------------------------

--
-- Table structure for table `forum_post`
--

CREATE TABLE `forum_post` (
  `id` bigint NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `is_approved` tinyint(1) NOT NULL,
  `author_id` int NOT NULL,
  `category_id` bigint DEFAULT NULL,
  `is_locked` tinyint(1) NOT NULL,
  `is_pinned` tinyint(1) NOT NULL,
  `views` int UNSIGNED NOT NULL
) ;

--
-- Dumping data for table `forum_post`
--

INSERT INTO `forum_post` (`id`, `title`, `content`, `created_at`, `updated_at`, `is_approved`, `author_id`, `category_id`, `is_locked`, `is_pinned`, `views`) VALUES
(1, 'نظر سنجی', 'لطفا نظر خود را در مورد محولاتی بیان کنید', '2026-07-07 06:08:21.558586', '2026-07-07 06:08:21.558628', 1, 1, 4, 0, 0, 44),
(2, 'تغذیه در کودکان تربیت پذیر', 'بنظر بنده در این کودکان حدالامکان غذا را بصورت کامل میکس شده از اول به بچه ندهید تا کودک از نهایت قدرت جویدن خود استفاده و تلاش کند.', '2026-07-07 14:12:31.366501', '2026-07-07 14:12:31.366578', 1, 4, 15, 0, 0, 14);

-- --------------------------------------------------------

--
-- Table structure for table `forum_post_likes`
--

CREATE TABLE `forum_post_likes` (
  `id` bigint NOT NULL,
  `post_id` bigint NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `forum_post_likes`
--

INSERT INTO `forum_post_likes` (`id`, `post_id`, `user_id`) VALUES
(1, 1, 2),
(3, 2, 1),
(2, 2, 2),
(4, 2, 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `accounts_report`
--
ALTER TABLE `accounts_report`
  ADD PRIMARY KEY (`id`),
  ADD KEY `accounts_report_reported_user_id_e4d773d9_fk_auth_user_id` (`reported_user_id`),
  ADD KEY `accounts_report_reporter_id_3d4247eb_fk_auth_user_id` (`reporter_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `axes_accessattempt`
--
ALTER TABLE `axes_accessattempt`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `axes_accessattempt_username_ip_address_user_agent_8ea22282_uniq` (`username`,`ip_address`,`user_agent`),
  ADD KEY `axes_accessattempt_ip_address_10922d9c` (`ip_address`),
  ADD KEY `axes_accessattempt_user_agent_ad89678b` (`user_agent`),
  ADD KEY `axes_accessattempt_username_3f2d4ca0` (`username`);

--
-- Indexes for table `axes_accessattemptexpiration`
--
ALTER TABLE `axes_accessattemptexpiration`
  ADD PRIMARY KEY (`access_attempt_id`);

--
-- Indexes for table `axes_accessfailurelog`
--
ALTER TABLE `axes_accessfailurelog`
  ADD PRIMARY KEY (`id`),
  ADD KEY `axes_accessfailurelog_user_agent_ea145dda` (`user_agent`),
  ADD KEY `axes_accessfailurelog_ip_address_2e9f5a7f` (`ip_address`),
  ADD KEY `axes_accessfailurelog_username_a8b7e8a4` (`username`);

--
-- Indexes for table `axes_accesslog`
--
ALTER TABLE `axes_accesslog`
  ADD PRIMARY KEY (`id`),
  ADD KEY `axes_accesslog_ip_address_86b417e5` (`ip_address`),
  ADD KEY `axes_accesslog_user_agent_0e659004` (`user_agent`),
  ADD KEY `axes_accesslog_username_df93064b` (`username`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `forum_category`
--
ALTER TABLE `forum_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD UNIQUE KEY `forum_category_name_9f308696_uniq` (`name`),
  ADD KEY `forum_category_parent_id_c38ddcc9_fk_forum_category_id` (`parent_id`);

--
-- Indexes for table `forum_comment`
--
ALTER TABLE `forum_comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `forum_comment_author_id_9e60eecd_fk_auth_user_id` (`author_id`),
  ADD KEY `forum_comment_post_id_eb329692_fk_forum_post_id` (`post_id`),
  ADD KEY `forum_comment_parent_id_4c29b530_fk_forum_comment_id` (`parent_id`);

--
-- Indexes for table `forum_post`
--
ALTER TABLE `forum_post`
  ADD PRIMARY KEY (`id`),
  ADD KEY `forum_post_author_id_609b7963_fk_auth_user_id` (`author_id`),
  ADD KEY `forum_post_category_id_202e3ede_fk_forum_category_id` (`category_id`);

--
-- Indexes for table `forum_post_likes`
--
ALTER TABLE `forum_post_likes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `forum_post_likes_post_id_user_id_fa33a7ea_uniq` (`post_id`,`user_id`),
  ADD KEY `forum_post_likes_user_id_56514e1a_fk_auth_user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `accounts_report`
--
ALTER TABLE `accounts_report`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `axes_accessattempt`
--
ALTER TABLE `axes_accessattempt`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `axes_accessfailurelog`
--
ALTER TABLE `axes_accessfailurelog`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `axes_accesslog`
--
ALTER TABLE `axes_accesslog`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `forum_category`
--
ALTER TABLE `forum_category`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `forum_comment`
--
ALTER TABLE `forum_comment`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `forum_post`
--
ALTER TABLE `forum_post`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `forum_post_likes`
--
ALTER TABLE `forum_post_likes`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_profile`
--
ALTER TABLE `accounts_profile`
  ADD CONSTRAINT `accounts_profile_user_id_49a85d32_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `accounts_report`
--
ALTER TABLE `accounts_report`
  ADD CONSTRAINT `accounts_report_reported_user_id_e4d773d9_fk_auth_user_id` FOREIGN KEY (`reported_user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `accounts_report_reporter_id_3d4247eb_fk_auth_user_id` FOREIGN KEY (`reporter_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `axes_accessattemptexpiration`
--
ALTER TABLE `axes_accessattemptexpiration`
  ADD CONSTRAINT `axes_accessattemptex_access_attempt_id_6b73a47a_fk_axes_acce` FOREIGN KEY (`access_attempt_id`) REFERENCES `axes_accessattempt` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `forum_category`
--
ALTER TABLE `forum_category`
  ADD CONSTRAINT `forum_category_parent_id_c38ddcc9_fk_forum_category_id` FOREIGN KEY (`parent_id`) REFERENCES `forum_category` (`id`);

--
-- Constraints for table `forum_comment`
--
ALTER TABLE `forum_comment`
  ADD CONSTRAINT `forum_comment_author_id_9e60eecd_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `forum_comment_parent_id_4c29b530_fk_forum_comment_id` FOREIGN KEY (`parent_id`) REFERENCES `forum_comment` (`id`),
  ADD CONSTRAINT `forum_comment_post_id_eb329692_fk_forum_post_id` FOREIGN KEY (`post_id`) REFERENCES `forum_post` (`id`);

--
-- Constraints for table `forum_post`
--
ALTER TABLE `forum_post`
  ADD CONSTRAINT `forum_post_author_id_609b7963_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `forum_post_category_id_202e3ede_fk_forum_category_id` FOREIGN KEY (`category_id`) REFERENCES `forum_category` (`id`);

--
-- Constraints for table `forum_post_likes`
--
ALTER TABLE `forum_post_likes`
  ADD CONSTRAINT `forum_post_likes_post_id_eeecd63b_fk_forum_post_id` FOREIGN KEY (`post_id`) REFERENCES `forum_post` (`id`),
  ADD CONSTRAINT `forum_post_likes_user_id_56514e1a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
