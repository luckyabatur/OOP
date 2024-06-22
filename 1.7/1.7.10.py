class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False


class AppStore:
    def __init__(self):
        self.apps = []

    def add_application(self, app: Application):
        self.apps.append(app)

    def remove_application(self, app: Application):
        self.apps.remove(app)

    @staticmethod
    def block_application(app: Application):
        app.blocked = True

    def total_apps(self):
        return len(self.apps)
