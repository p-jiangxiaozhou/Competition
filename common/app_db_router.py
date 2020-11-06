from settings import APP_LABELS


class SlaveDbRouter(object):
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models
        """
        if model._meta.app_label in APP_LABELS:
            return 'slave'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models
        """
        if model._meta.app_label in APP_LABELS:
            return 'slave'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model is involved
        """
        if obj1._meta.app_label in APP_LABELS or obj2._meta.app_label in APP_LABELS:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        do not allow migrate
        """
        if db == 'slave' or app_label in APP_LABELS:
            return False
        return None
