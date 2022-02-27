import random


class VKinder:
    def __init__(self, vk, session):
        self.vk = vk
        self.session = session

    def search(self, user):
        return self.session.users.search(
            count=100,
            offset=random.randrange(0, 100),
            fields=['photo_id', 'sex', 'bdate', 'city'],
            sex=user.search_sex,
            age_from=user.search_age_from,
            age_to=user.search_age_to,
            city=user.search_city,
            status=user.search_status,
            has_photo=1,
            is_closed=False,
            can_access_closed=True
        )['items']

    def photos(self, owner_id):
        photos = self.session.photos.get(
            owner_id=owner_id,
            album_id='profile',
            extended=1,
            photo_sizes=1
        )

        photos_lst = sorted(photos['items'], key=lambda k: k['likes']['count'], reverse=True)

        if len(photos_lst) > 3:
            photos_lst = photos_lst[:3]

        photos_to_send = list()

        for photo in photos_lst:
            media_id = photo['id']
            photos_to_send.append(f'photo{owner_id}_{media_id}')

        return photos_to_send
