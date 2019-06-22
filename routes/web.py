from masonite.routes import Get, Post
from app.http.controllers.ToppageController import ToppageController

ROUTES = [
    get('/', ToppageController.show),
    get('/my_site/api/get_toppage', ToppageController.get_toppage)
]
