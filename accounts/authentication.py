from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
User = get_user_model()
class EmailAuthBackend(ModelBackend):
    def authenticate(self,request,username=None,password=None,*args, **kwargs):
        '''
        email authentication backend
        '''
        if username is None or password is None:
            return 
        try:
            user  = User.objects.get(email=username)
        except User.DoesNotExist:
            return 
        except User.MultipleObjectsReturned:
            return 

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
    def get_user(self,user_id):
        try :
            return User.objects.get(id=1)
        except User.DoesNotExist:
            return None
        except User.MultipleObjectsReturned:
            return None


