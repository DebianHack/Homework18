CREATE SCHEMA QaAuto;
CREATE TABLE car_brands(
			id int(10)NOT NULL AUTO_INCREMENT PRIMARY KEY,
			title varchar(255)
			);
CREATE TABLE QaAuto.car_models(
    			id int(10)NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                        carBrandId int(10)NOT NULL, 
                        title varchar(255)
			);
CREATE TABLE QaAuto.users(
    			id int(10)NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        firstName varchar(255), 
                        lastName varchar(255),
    			email varchar(255), 
    			password varchar(255)      
			);
CREATE TABLE QaAuto.cars(
    			id int(10)NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    			userId int(10) NOT NULL, 
    			carBrandId int(10) NOT NULL, 
    			carModelId int(10) NOT NULL, 
    			mileage int(15), 
    			initialMilleage int(15)
			);
