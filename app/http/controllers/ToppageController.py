from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.models.Toppage import Toppage

class ToppageController:

    def show(self):
        return view('my_site/build/index.html')

    def get_toppage(self):
        toppage = Toppage.get_toppage()
        return {'toppage': toppage}