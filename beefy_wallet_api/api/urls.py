from django.conf.urls import url, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("transactions", TransactionsViewSet, basename="expenses")
# router.register("incomes", IncomesViewSet, basename="incomes")
router.register("money_sources", MoneySourcesViewSet, basename="money_sources")


urlpatterns = [
    url('', include(router.urls))
]