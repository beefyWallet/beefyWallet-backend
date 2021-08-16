from rest_framework import serializers
from beefy_wallet_api.models import *

class AdsSerializer(serializers.ModelSerializer):
     class Meta:
        model = Ads
        fields = '__all__'   

class QuotesSerializer(serializers.ModelSerializer):
     class Meta:
        model = Quotes
        fields = '__all__'   

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







