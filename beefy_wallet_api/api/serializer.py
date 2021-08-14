from rest_framework import serializers
from beefy_wallet_api.models import *

class TransactionsSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Transactions
        fields = '__all__'
        depth = 1

class MoneySourcesSerializer(serializers.ModelSerializer):
    # name = TransactionsSerializer(many=False)
    # name = TransactionsSerializer(many=False)
    class Meta:
        model = MoneySources
        fields = '__all__'




        # depth = 1
# class IncomesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Incomes
#         fields = '__all__'
#         depth = 1




# class StudentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Students
#         fields = ['id', 'name', 'age', 'grade', 'modules']
#         depth = 1