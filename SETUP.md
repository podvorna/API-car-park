1. to clone repository 
2. run to application "manage.py" (in terminal: 'python manage.py runserver')
3. Open the link and use these endpoints:

+ GET /drivers/driver/ - output of the list of drivers
+ GET /drivers/driver/?created_at__gte=10-11-2021 - output of the list of drivers created after 10-11-2021
+ GET /drivers/driver/?created_at__lte=16-11-2021 - output of the list of drivers created before 16-11-2021
+ GET /drivers/driver/<driver_id>/ - obtaining information on a particular driver
+ POST /drivers/driver/ - creating a new driver

+ GET /vehicles/vehicle/ - output of the list of vehicles
+ GET /vehicles/vehicle/<vehicle_id> - obtaining information on a specific car
+ POST /vehicles/vehicle/ - створення нової машини
+ UPDATE /vehicles/vehicle/<vehicle_id>/ - creating a new car

