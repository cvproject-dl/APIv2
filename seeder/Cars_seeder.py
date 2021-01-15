import json
from dbmodels import Cars
from dbmodels.initdb import db


def cars_seeder(classesloc):
    """
    :param db : SQLAlchemy DB
    :param classesloc:PATH of json file with class names
    :return:
    """
    with open(classesloc) as f:
        classes = json.load(f)
        print(len(classes))
    for car in classes:
        c = Cars(car_name=car["Car Name"],
                 car_image=car["Image"],
                 fuel_type=car["Fuel Type"],
                 fuel_tank_capacity=car["Fuel Tank Capacity"],
                 seating_capacity = car['Seating Capacity'],
                 body_type=car["Body Type"],
                 transmission_type=car['Transmission Type'])
        db.session.add(c)
    db.session.commit()
