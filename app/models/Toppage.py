from config.database import Model

class Toppage(Model):
    #テーブル名がtoppageを探す
    __table__ = 'toppage'

    #トップページの内容をコントローラに返す
    @staticmethod
    def get_toppage():
        return Toppage ¥
            .select(
                'title',
                'article'
            ) ¥
            .find(1) ¥
            .serialize() #dictとして取得