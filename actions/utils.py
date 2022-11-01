
from actions.models import Action
from django.contrib.contenttypes.models import ContentType
from .models import Action
import datetime
from django.utils import timezone
from accounts.models import Profile

def create_action(profile:Profile,body:str,target=None):
    #checking  for similar actions in the last minute
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    
    similar_actions = Action.objects.filter(profile__id=profile.id,body=body,created__gte=last_minute)

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_id=target.id,target_ct=target_ct)
    
    if not similar_actions.exists():
        action = Action(profile=profile,body=body,target=target)
        action.save()
        return action
    return None