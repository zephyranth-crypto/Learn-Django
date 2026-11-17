**1. Some Important Code**

- uv run python manage.py runserver
- uv run python manage.py shell
- uv run python manage.py makemigrations
- uv run python manage.py migrate

**2. CRUD Operations**

- create : Car.objects.create(car_name = "Tesla" , car_speed = 200)
- read : cars = Cars.object.get(id =1) or Cars.objects.filter(id =1)
- update : Car.objects.get(id =1).update(car_name = "Xiaomi", car_speed =100)
- delete : Car.objects.get(id =1).delete()
