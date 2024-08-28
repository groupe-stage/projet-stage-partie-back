from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def custom_validation(data):
    email = data.get('email', '').strip()
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    cin = data.get('cin', '').strip()
    role = data.get('role', '').strip()
    identifiant = data.get('identifiant', '').strip()
    id_surveillance = data.get('id_surveillance')
    id_unite = data.get('id_unite')
    
    if not email or UserModel.objects.filter(email=email).exists():
        raise ValidationError('Choose another email')
    
    if not password or len(password) < 8:
        raise ValidationError('Choose another password, min 8 characters')
    
    if not username:
        raise ValidationError('Choose another username')
    
    if not cin:
        raise ValidationError('CIN is required')
    
    if not role:
        raise ValidationError('Role is required')
    
    if not identifiant:
        raise ValidationError('Identifiant is required')
    
    

    return data



def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError('an email is needed')
    return True

def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('choose another username')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('a password is needed')
    return True