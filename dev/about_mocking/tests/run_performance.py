import os
import sys

from assertpy import assert_that
from locust import TaskSet, task, HttpLocust

path = os.path.join(os.getcwd(), '../../..')
sys.path.append(path)


class GetUsers(TaskSet):
    @task
    def get_users(self):
        response = self.client.get('/users')

        assert_that(response.status_code).is_equal_to(200)


class WebUser(HttpLocust):
    task_set = GetUsers
    min_wait = 1000
    max_wait = 3000
