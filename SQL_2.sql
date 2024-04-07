INSERT INTO `car_models` (`id`, `carBrandId`, `title`) VALUES ('1', '1', BMW 5), (NULL, '2', 'Porsche Panamera'), (NULL, '3', 'Porsche Cayenne'), (NULL, '4', 'Ford Fusion'), (NULL, '5', 'BMW Z3'), (NULL, '6', 'BMW X6'), (NULL, '7', 'Ford Focus'), (NULL, '8', 'Audi Q7'), (NULL, '9', 'Fiat Panda'), (NULL, '10', 'Ford Fiesta')
INSERT INTO `car_brands` (`id`, `title`) VALUES ('1', BMW 5), (NULL,'Porsche Panamera'), (NULL, 'Porsche Cayenne'), (NULL, 'Ford Fusion'), (NULL, 'BMW Z3'), (NULL, 'BMW X6'), (NULL, 'Ford Focus'), (NULL, 'Audi Q7'), (NULL, 'Fiat Panda'), (NULL, 'Ford Fiesta')
INSERT INTO `users` (`id`, `firstName`, `lastName`, `email`, `password`) VALUES ('1', 'Ivan', 'Pentrenko', 'ivan@i.ua', 'ivan'), (NULL, 'Vlad', 'Sidorov', 'vlad@i.ua', 'vlad'), (NULL, 'Sasha', 'Petrov', 'sasha@i.ua', 'sasha'), (NULL, 'Stas', 'Sobolev', 'stas@i.ua', 'stas'), (NULL, 'Danil', 'Vasilev', 'danil@i.ua', 'danil'), (NULL, 'Maria', 'Alexndrova', 'maria@i.ua', 'maria'), (NULL, 'Konstantin', 'Permakov', 'konstantin@i.ua', 'konstantin'), (NULL, 'Duglas', 'Roger', 'duglas@i.ua', 'duglas'), (NULL, 'Tamara', 'Malkolm', 'tamara@i.ua', 'tamara'), (NULL, 'Stan', 'Smit', 'stan@i.ua', 'stan')
INSERT INTO `cars` (`id`, `userId`, `carBrandId`, `carModelId`, `mileage`, `initialMilleage`) VALUES ('1', '1', '1', '1', '45', '67'), (NULL, '2', '2', '2', '56', '89'), (NULL, '3', '3', '3', '34', '90'), (NULL, '4', '4', '4', '12', '45'), (NULL, '5', '5', '5', '78', '123'), (NULL, '6', '6', '6', '78', '89'), (NULL, '7', '7', '7', '100', '130'), (NULL, '8', '8', '8', '78', '88'), (NULL, '9', '9', '9', '120', '150'), (NULL, '10', '10', '10', '130', '150')


ALTER TABLE QaAuto.car_models
ADD FOREIGN KEY (carBrandId) REFERENCES car_brands(id)


ALTER TABLE QaAuto.cars
ADD FOREIGN KEY (userId) REFERENCES users(id),
ADD FOREIGN KEY (carBrandId) REFERENCES car_brands(id),
ADD FOREIGN KEY (carModelId) REFERENCES car_models(id)




