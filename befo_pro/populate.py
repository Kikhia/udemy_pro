import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','befo_pro.settings')

import django
django.setup()

import random
from befo_app.models import User
from faker import Faker

fakegen = Faker()
def populate(N=10):
    for data in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        userr = User.objects.get_or_create(first_name=fake_first_name,
                                            last_name=fake_last_name,
                                            email=fake_email)[0]

if __name__ == '__main__':
    print('populating..')
    populate(15)
    print('populating complete')
