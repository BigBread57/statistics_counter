import datetime

from django.test import TestCase

from repository_statistic.models import RepositoryStatistic


class RepositoryStatisticViewSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создание 10 событий
        amount_days = 10
        for day_num in range(amount_days):
            RepositoryStatistic.objects.create(date=datetime.date.today(),
                                               views=100,
                                               clicks=10,
                                               cost=1000)

    # Тест, то что такая страница есть
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/api/v1/repository/')
        self.assertEqual(resp.status_code, 200)

    # Тест что создается событие через get
    def test_view_url_add_repository_across_get(self):
        resp = self.client.get('/api/v1/repository/?date=2021-09-12')
        self.assertEqual(resp.status_code, 200)

    # Тест что не создается событие через get если передать не те параметры
    def test_view_url_not_add_repository_across_get(self):
        resp = self.client.get('/api/v1/repository/?from_date=2021-09-12')
        self.assertEqual(resp.status_code, 200)

    # Тест что удаляется вся статистика
    def test_view_url_delete_all_repository_statistic(self):
        resp = self.client.delete('/api/v1/repository/destroy')
        self.assertEqual(resp.status_code, 301)

    # Тест что создается новое событие
    def test_view_url_add_new_event(self):
        resp = self.client.post('/api/v1/repository/',
                                {'date': '2021-09-16', 'views': '100',
                                 'clicks': '100', 'cost': '500'})
        self.assertEqual(resp.status_code, 201)


class RepositoryStatisticModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        RepositoryStatistic.objects.create(date=datetime.date.today())

    def test_date_fields(self):
        repository = RepositoryStatistic.objects.get(id=1)
        views = repository.views
        clicks = repository.clicks
        cost = repository.cost
        self.assertEquals(views, 0)
        self.assertEquals(clicks, 0)
        self.assertEquals(cost, 0)
