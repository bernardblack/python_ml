import csv
from sqlalchemy import create_engine
from sqlalchemy.sql import select, update
from sqlalchemy import Table, Column, String, Integer
from sqlalchemy.sql.schema import ForeignKey, MetaData
from collections import defaultdict

metadata = MetaData()

country = Table('country', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String)
                )


city = Table('city', metadata,
             Column('id', Integer, primary_key=True),
             Column('country_id', Integer, ForeignKey('country.id'), nullable=False),
             Column('name', String)
             )


def load_data(filename: str) -> dict:
    """
    load data and make the dictionary, where the key is country name,
    value - list of lists [CityName, CityId]
    {'Country': [['City', CityId], ['City', CityId]]}
    """
    data = defaultdict(list)

    with open(filename) as f:
        reader = csv.reader(f, delimiter=';', quotechar='"')
        next(reader)  # skip header
        for row in reader:
            try:
                city_and_code = [row[1], int(row[2])]
                data[row[0]].append(city_and_code)
            except (IndexError, ValueError):
                pass  # skip wrong line
    return data


def main():

    # db_string = "postgresql://user:password@localhost:5432/database"
    db_string = "sqlite:///database.db"
    engine = create_engine(db_string)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    conn = engine.connect()

    data = load_data("full_city_list.txt")

    # fill database
    country_id = 1
    for key in data:
        query = country.insert().values(id=country_id, name=key)
        conn.execute(query)
        for cityes in data[key]:
            query = city.insert().values(id=cityes[1], country_id=country_id, name=cityes[0])
            conn.execute(query)
        country_id += 1

    def select_cityes(country_name):
        """ select cityes for country """

        query = select(city.c.name).where(city.c.country_id == select(country.c.id).where(country.c.name == country_name).scalar_subquery())

        print(country_name)

        cityes = conn.execute(query)
        for c in cityes:
            print('\t', c.name)

    def add_city(country_name, city_name, city_id):
        """ add city to country """

        sub = select(country.c.id).where(country.c.name == country_name).scalar_subquery()
        query = city.insert().values(id=city_id, country_id=sub, name=city_name)
        conn.execute(query)

    def rename_city(country_name, old_city_name, new_city_name):
        """ rename city """

        sub = select(country.c.id).where(country.c.name == country_name).scalar_subquery()
        query = update(city).where(city.c.name == old_city_name and city.c.country_id == sub).values(name=new_city_name)
        conn.execute(query)

    select_cityes("Argentina")
    select_cityes("Jamaica")
    add_city("Ukraine", "Proskuriv", 5000)
    select_cityes("Ukraine")
    rename_city("Ukraine", "Proskuriv", "Khmelnytskyi")
    select_cityes("Ukraine")


if __name__ == "__main__":
    main()
