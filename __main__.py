import mini


class Classy(mini.MiniApplication):

    def before(self):
        self.drawables = []


if __name__ == "__main__":

    app = Classy(
        name='shmupy',
        settings='settings.yaml'
    )
    app.run()
