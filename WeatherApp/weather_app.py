from create_app import create_app
from configure_app import configure_app

app = create_app()
configure_app(app)

app.mainloop()
