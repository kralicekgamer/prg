-- -----------------------------------------------------
-- Schema rejstrik
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `rejstrik` DEFAULT CHARACTER SET utf8 COLLATE utf8_czech_ci ;
USE `rejstrik` ;

-- -----------------------------------------------------
-- Table `rejstrik`.`zaci`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rejstrik`.`zaci` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `jmeno` VARCHAR(45) NOT NULL,
  `prijmeni` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rejstrik`.`ciny`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rejstrik`.`ciny` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nazev` VARCHAR(45) NOT NULL,
  `opatreni` VARCHAR(100) NOT NULL,
  `zaci_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ciny_zaci_idx` (`zaci_id` ASC),
  CONSTRAINT `fk_ciny_zaci`
    FOREIGN KEY (`zaci_id`)
    REFERENCES `rejstrik`.`zaci` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
