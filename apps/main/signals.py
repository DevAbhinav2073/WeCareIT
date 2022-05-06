from django.dispatch import receiver
from django.db.models.signals import post_migrate

from apps.main.models import Vehicle, User

VEHICLE_DATA_LIST = [
    {
        'registration_number': 'Reg1',
        'make_year': 2017
    }, {
        'registration_number': 'Reg2',
        'make_year': 2015
    }, {
        'registration_number': 'Reg3',
        'make_year': 2013
    },

]


@receiver(post_migrate)
def create_dummy_data(sender, *args, **kwargs):
    try:
        if not Vehicle.objects.all().exists():
            for data in VEHICLE_DATA_LIST:
                Vehicle.objects.create(**data)
        print('Vehicles created')
        if User.objects.all().count() < 10:
            for i in range(0, 10):
                u, _ = User.objects.get_or_create(
                    username=f'User {i+1}',
                    email=f'{i}@gmail.com'
                )
                u.set_password(str(i))
                u.save()
        print('Users count', User.objects.all().count())
    except Exception as e:
        # when table is not present
        print(e)
