import random
import string

import django
from . models import *

def Get_token():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(random.randrange(25,100)))
     


def Get_CategoriesToAdd(member):
    try:
        fields = Fields.objects.get(member=member)

        for field in fields._meta.get_fields():
            if field.name != 'id' and field.name != 'accessory' and field.name != 'member':
                obj = Fields.objects.first()
                field_object = Fields._meta.get_field(field.name)
                field_value = field_object.value_from_object(obj)
                while field_value == True:
                    print(field.name)
                    return field.name

        return 'Done'
    except Exception as e:
        print(e)