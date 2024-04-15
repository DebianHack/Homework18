ALTER TABLE QaAuto.car_models
ADD FOREIGN KEY (carBrandId) REFERENCES car_brands(id);


ALTER TABLE QaAuto.cars
ADD FOREIGN KEY (userId) REFERENCES users(id);
ADD FOREIGN KEY (carBrandId) REFERENCES car_brands(id);
ADD FOREIGN KEY (carModelId) REFERENCES car_models(id);


INSERT INTO qaauto.car_brands (`id`, `title`) VALUES (1, 'BMW 5'), (2,'Porsche Panamera'), 

(3, 'Porsche Cayenne'), (4, 'Ford Fusion'), (5, 'BMW Z3'), (6, 'BMW X6'), 

(7, 'Ford Focus'), (8, 'Audi Q7'), (9, 'Fiat Panda'), (10, 'Ford Fiesta');

INSERT INTO qaauto.car_models (`id`, `carBrandId`) VALUES (1, 1),
 (2, 2), (3, 3), (4, 4), 
(5, 5), (6, 6), (7, 7), 
(8, 8), (9, 9), (10, 10);

INSERT INTO qaauto.users (`id`, `firstName`, `lastName`, `email`, `password`) VALUES (1, 'Ivan', 'Pentrenko', 'ivan@i.ua', 'ivan'), 

(2, 'Vlad', 'Sidorov', 'vlad@i.ua', 'vlad'), (3, 'Sasha', 'Petrov', 'sasha@i.ua', 'sasha'), 

(4, 'Stas', 'Sobolev', 'stas@i.ua', 'stas'), (5, 'Danil', 'Vasilev', 'danil@i.ua', 'danil'), 

(6, 'Maria', 'Alexndrova', 'maria@i.ua', 'maria'), (7, 'Konstantin', 'Permakov', 'konstantin@i.ua', 'konstantin'), 

(8, 'Duglas', 'Roger', 'duglas@i.ua', 'duglas'), (9, 'Tamara', 'Malkolm', 'tamara@i.ua', 'tamara'),

(10, 'Stan', 'Smit', 'stan@i.ua', 'stan');

INSERT INTO qaauto.cars (`id`, `userId`, `carBrandId`, `carModelId`, `mileage`, `initialMilleage`) VALUES (1, 1, 1, 1, '45', '67'), (2, 2, 2, 2, '56', '89'), 

(3, 3, 3, 3, '34', '90'), (4, 4, 4, 4, '12', '45'), 

(5, 5, 5, 5, '78', '123'), (6, 6, 6, 6, '78', '89'), 
(7, 7, 7, 7, '100', '130'), 
(8, 8, 8, 8, '78', '88'), 
(9, 9, 9, 9, '120', '150'), (10, 10, 10, 10, '130', '150');