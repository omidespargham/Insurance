from django.contrib.auth import password_validation
from django.forms import ValidationError
from django.utils.translation import ngettext


# customize password_validate Class for better message.
class MinLenght(password_validation.MinimumLengthValidator):
    def get_help_text(self):
        return "گذرواژه شما باید بیشتر از 8 کاراکتر باشد."
    
    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "این پسورد کوتاه است.باید حداقل"
                    "%(min_length)d کاراکتر باشد",
                    "این پسورد کوتاه است.باید حداقل"
                    "%(min_length)d کاراکتر باشد",
                    self.min_length,
                ),
                code="password_too_short",
                params={"min_length": self.min_length},
            )
    