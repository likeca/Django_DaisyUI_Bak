# Crispy Form Theme - Bootstrap 5
from django.contrib.messages import constants as messages

CRISPY_ALLOWED_TEMPLATE_PACKS = "daisyui"
CRISPY_TEMPLATE_PACK = "daisyui"

# Change error alert to 'danger'
MESSAGE_TAGS = {
    messages.ERROR: "danger",
}
