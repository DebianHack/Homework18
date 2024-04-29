SELECT * FROM qaauto.users where firstName LIKE "am%";

USE qaauto
SELECT mileage, initialMilleage, car_brands.id , car_brands.title FROM qaauto.cars

INNER JOIN qaauto.car_brands 
ON cars.carModelId = car_brands.id 
WHERE car_brands.title = "Audi" 
AND qaauto.cars.initialMilleage = (SELECT MAX(initialMilleage) 
FROM qaauto.cars);

USE qaauto;

SELECT car_brands.title 
AS car_id, 
COUNT(car_brands.id) 
AS count_models

FROM qaauto.cars

INNER JOIN qaauto.car_brands

ON cars.carModelId = car_brands.id

WHERE 
car_brands.title LIKE "BMW%" 
OR car_brands.title LIKE "Audi%"

group by 

car_brands.title;

USE qaauto;

SELECT 

car_brands.title AS car_barnd,

car_models.id AS car_model, 

COUNT(cars.id) AS user_count

FROM qaauto.cars

INNER JOIN qaauto.car_brands 
ON cars.carModelId = car_brands.id

INNER JOIN car_models
 ON cars.carModelId = car_models.id

group by 

car_brands.title, car_models.id;


USE qaauto;

SELECT 
firstName

FROM users

INNER JOIN

cars ON users.id = cars.userId

Group BY

users.firstName;
