# -*- coding: utf-8 -*-


class CatalogoRouter(object):
    """
    A router to control all database operations on models in the
    catalogo application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read operations models go to catalogo_db.
        """
        if model._meta.app_label == 'catalogo':
            return 'catalogo_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write operations models go to catalogo_db.
        """
        if model._meta.app_label == 'catalogo':
            return 'catalogo_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the operations app is involved.
        """
        if obj1._meta.app_label == 'catalogo' or \
            obj2._meta.app_label == 'catalogo':
            return True
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the operations app only appears in the 'catalogo_db'
        database.
        """
        if db == 'catalogo_db':
            return model._meta.app_label == 'catalogo'
        elif model._meta.app_label == 'catalogo':
            return False
        return None
