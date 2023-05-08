#!/usr/bin/python3
'''
This is the 'db_storage' module.
'''

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

class DBStorage:
    '''
    This is the 'DBStorage' class.
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
        Initializes the storage class
        '''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        Queries all objects depending on class name
        '''
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        from models.base_model import BaseModel

        objects = {}

        if cls is None:
            for cls in [User, State, City, Amenity, Place, Review]:
                query = self.__session.query(cls)
                for obj in query:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objects[key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query:
                key = obj.__class__.__name__ + '.' + obj.id
                objects[key] = obj

        return objects

    def new(self, obj):
        '''
        Adds the object to the current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''
        Commits all changes of the current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
        Deletes from the current database session obj if not None
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''
        Creates all tables in the database
        '''
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        from models.base_model import BaseModel

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

