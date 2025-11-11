from celery import shared_task
from datetime import datetime
import logging

from claim.models import Claim
from claim.notification_client import ClaimNotificationSender
from claim.notification_templates import ClaimNotificationKeys

logger = logging.getLogger(__name__)

@shared_task
def process_claim_task():
    try:
        print("TASKING")
        claims = Claim.objects.filter(
            status_pre_authorization=Claim.STATUS_PRE_AUTHORIZATION_SUBMITED_TO_DOCTOR,validity_to__isnull=True
        )
        print(len(claims))
        if claims.exists() and len(claims)>0:
            ClaimNotificationSender.send_preauthorization_notifications(claims,ClaimNotificationKeys.ON_PENDING)
    except Exception as e:
        import traceback
        traceback.print_exc()
        logger.error(f"Failed to execute process_claim_task, error: {traceback.format_exc()}")
