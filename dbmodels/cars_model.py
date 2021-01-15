from .initdb import db


class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_name = db.Column(db.String(80), unique=True, nullable=False)
    car_image = db.Column(db.String(200), unique=True, nullable=False)
    fuel_type = db.Column(db.String(200), nullable=False)
    fuel_tank_capacity = db.Column(db.String(200), nullable=False)
    seating_capacity = db.Column(db.String(200), nullable=False)
    body_type = db.Column(db.String(200), nullable=False)
    transmission_type = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Cars {self.car_name}>'

    @staticmethod
    def __item_to_json(item):
        host = "https://carimage.netlify.app"
        resp = dict()
        resp['id'] = item.id
        resp['name'] = item.car_name
        resp['image'] = f"{host}/{item.car_image}"
        resp['fuel_type'] = item.fuel_type
        resp['fuel_tank_capacity'] = item.fuel_tank_capacity
        resp['seating_capacity'] = item.seating_capacity
        resp['body_type'] = item.body_type
        resp['transmission_type'] = item.transmission_type
        return resp

    @classmethod
    def __paginate(cls, all_items, page):
        if page is None:
            page = 1
        results = list()
        start = (page - 1) * 10
        last_idx = len(all_items) - 1
        if last_idx < start:
            return results
        total = 0
        for item in all_items[start:]:
            if total >= 10:
                break
            results.append(cls.__item_to_json(item))
            total += 1
        return results

    @classmethod
    def get_items(cls, page):
        """
        :param page: page (int) for pagination
        :return: list of items with id ,name & image , 10 items per page
        """
        all_items = cls.query.all()
        return cls.__paginate(all_items, page)

    @classmethod
    def get_item_by_id(cls, idno):
        """
        :param idno: id parameter (to search)
        :return: item matching the id
        """
        item = cls.query.filter_by(id=idno).first()
        return cls.__item_to_json(item)

    @classmethod
    def search_by_name(cls, search_term, page):
        """
        :param search_term: car name to search
        :param page: page (int) for pagination
        :return:  list of items with id ,name & image , 10 items per page
        """
        items = cls.query.filter(cls.car_name.like('%' + search_term + '%')).all()
        return cls.__paginate(items, page)
