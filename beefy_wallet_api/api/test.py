# 
# # MODELS:
# 
# class Account(AbstractBaseUser):
#     email = models.EmailField(unique=True, db_index=True)
#     username = models.CharField(max_length=40, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
# 
# objects = AccountManager()
# 
# USERNAME_FIELD = 'email'
# REQUIRED_FIELDS = ['username']
# 
# def __unicode__(self):
#     return self.email
# 
# def get_full_name(self):
#     return self.email
# 
# def get_short_name(self):
#     return self.email
# 
# class UserInfo(models.Model):
#     user = models.OneToOneField(Account, related_name='user')
#     first_name = models.CharField('first_name', max_length=50)
#     last_name = models.CharField('last_name', max_length=50)
#     address_1 = models.CharField('address_1', max_length=200)
#     address_2 = models.CharField('address_2', max_length=200)
#     city = models.CharField('city', max_length=100)
#     state = models.CharField('state', max_length=100)
#     zip = models.IntegerField()
#     phone = models.CharField('phone', max_length=20)
#     updated = models.DateTimeField(auto_now_add=True)
# 
# # SERIALIZER:
# 
# class UserInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserInfo
#         fields = ('first_name', 'last_name',
#         'address_1', 'address_2', 'city', 'state', 'zip',
#         'phone', 'updated')
#         read_only_fields = ('user', 'updated')
# 
# class AuthUserInfoSerializer(serializers.ModelSerializer):
#     userinfo = UserInfoSerializer()
# 
#     class Meta:
#         model = Account
#         fields = ('id', 'username', 'email', 'userinfo')
# 
