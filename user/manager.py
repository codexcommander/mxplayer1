from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email,phone_no,password=None,**extra_fields):
        if not email:
            raise ValueError("email_id is required")
        user = self.model(email=email,phone_no=phone_no,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,phone_no,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("user must have is_superuser = true")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("user must have is_staff = true")
        if extra_fields.get('is_active') is not True:
            raise ValueError("user must have is_active = true")
        return  self.create_user(email,phone_no,password,**extra_fields)