-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema TA_Maid
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `TA_Maid` ;

-- -----------------------------------------------------
-- Schema TA_Maid
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `TA_Maid` DEFAULT CHARACTER SET utf8 ;
USE `TA_Maid` ;

-- -----------------------------------------------------
-- Table `TA_Maid`.`role`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TA_Maid`.`role` (
  `role_id` VARCHAR(45) NOT NULL,
  `role_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`role_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TA_Maid`.`embed`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TA_Maid`.`embed` (
  `menu_embed_id` INT NOT NULL AUTO_INCREMENT,
  `embed_title` VARCHAR(45) NULL,
  `embed_description` VARCHAR(45) NULL,
  PRIMARY KEY (`menu_embed_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TA_Maid`.`role_menu_embed`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TA_Maid`.`role_menu_embed` (
  `role_role_id` VARCHAR(45) NOT NULL,
  `embed_menu_embed_id` INT NOT NULL,
  `role_description` VARCHAR(45) NULL,
  PRIMARY KEY (`role_role_id`, `embed_menu_embed_id`),
  INDEX `fk_role_has_role_menu_embed_role_menu_embed1_idx` (`embed_menu_embed_id` ASC),
  INDEX `fk_role_has_role_menu_embed_role_idx` (`role_role_id` ASC),
  CONSTRAINT `fk_role_has_role_menu_embed_role`
    FOREIGN KEY (`role_role_id`)
    REFERENCES `TA_Maid`.`role` (`role_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_role_has_role_menu_embed_role_menu_embed1`
    FOREIGN KEY (`embed_menu_embed_id`)
    REFERENCES `TA_Maid`.`embed` (`menu_embed_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
