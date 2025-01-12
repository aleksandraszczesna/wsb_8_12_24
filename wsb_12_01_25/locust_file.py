import locust

from locust import HttpUser, task

#klasa jest zbiorem funkcji
#nazwa klas definiuje się od wielkiej litery
class MyUser(HttpUser):
    @task   #dekorator ->użytkownik symuluje poniższą funkcję
    def get_posts(self):
        self.client.get("/comments")

#        locust -f locust_file.py --host=https://jsonplaceholder.typicode.com

