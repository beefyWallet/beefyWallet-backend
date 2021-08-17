from rest_framework import viewsets
from rest_framework.response import Response
from beefy_wallet_api.models import *
from .serializer import TransactionsSerializer,MoneySourcesSerializer,AdsSerializer,QuotesSerializer
from django.contrib.auth.models import User


class TransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionsSerializer

    def get_queryset(self):
        user = self.request.user
        expenses_incomes = Transactions.objects.filter(money_source__author__username = user)
        return expenses_incomes

    def create(self, request, *args, **kwargs):
        user = self.request.user
        expenses_incomes_data = request.data
        new_expense = Transactions.objects.create(
            money_source=MoneySources.objects.get(name=expenses_incomes_data['money_source'], author__username = user),
            value=expenses_incomes_data["value"],
            note=expenses_incomes_data["note"],
            transaction_type= expenses_incomes_data['transaction_type'],
            category= expenses_incomes_data['category'])

        new_expense.save()

        serializer = MoneySourcesSerializer(new_expense)

        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        user = self.request.user
        transaction = self.get_object()
        expenses_incomes_data = request.data

        money_source=MoneySources.objects.get(name=expenses_incomes_data['money_source'],author__username = user)

        transaction.money_source = money_source
        transaction.value = expenses_incomes_data["value"]
        transaction.transaction_type = expenses_incomes_data["transaction_type"]
        transaction.note = expenses_incomes_data["note"]
        transaction.category = expenses_incomes_data["category"]

        transaction.save()

        serializer = TransactionsSerializer(transaction)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        user = self.request.user
        transaction = self.get_object()
        expenses_incomes_data = request.data

        try:
            money_source=MoneySources.objects.get(name=expenses_incomes_data['money_source'],author__username = user)
            transaction.money_source = money_source
        except KeyError:
            pass

        transaction.value = expenses_incomes_data.get("value", transaction.value)
        transaction.transaction_type = expenses_incomes_data.get("transaction_type", transaction.transaction_type)
        transaction.note = expenses_incomes_data.get("note", transaction.note)
        transaction.category = expenses_incomes_data.get("category", transaction.category)

        transaction.save()

        serializer = TransactionsSerializer(transaction)

        return Response(serializer.data)

#     def destroy(self, request, *args, **kwargs):
#         logedin_user = request.user
#         car = self.get_object()
#         car.delete()
#         response_message = {"message": "Not Allowed"}
# 
#         return Response(response_message)


class MoneySourcesViewSet(viewsets.ModelViewSet):
    serializer_class = MoneySourcesSerializer

    def get_queryset(self):
        user = self.request.user
        money_sources = MoneySources.objects.filter(author__username = user)
        return money_sources

    def create(self, request, *args, **kwargs):
        user = self.request.user
        money_source_data = request.data

        new_money_source = MoneySources.objects.create(author=User.objects.get(username=user), name=money_source_data["name"], amount=money_source_data[
            "amount"])

        new_money_source.save()

        serializer = MoneySourcesSerializer(new_money_source)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user = self.request.user
        moeny_source = self.get_object()
        moeny_source_data = request.data

        moeny_source.name = moeny_source_data['name']
        moeny_source.amount = moeny_source_data['amount']
        moeny_source.author = User.objects.get(username=user)
        moeny_source.save()

        serializer = MoneySourcesSerializer(moeny_source)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        user = self.request.user
        moeny_source = self.get_object()
        moeny_source_data = request.data

        moeny_source.name = moeny_source_data.get('name',moeny_source.name)
        moeny_source.amount = moeny_source_data.get('amount',moeny_source.amount)

        moeny_source.save()

        serializer = MoneySourcesSerializer(moeny_source)

        return Response(serializer.data)


class AdsViewSet(viewsets.ModelViewSet):
    serializer_class = AdsSerializer

    def get_queryset(self):
        user = self.request.user
        ads = Ads.objects.all()
        return ads


class QuotesViewSet(viewsets.ModelViewSet):
    serializer_class = QuotesSerializer

    def get_queryset(self):
        quotes = Quotes.objects.all()
        return quotes
