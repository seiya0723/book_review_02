from django.db import models
from django.utils import timezone

#models.Modelを継承してモデルクラスを作る
class Topic(models.Model):

    #DBのカラムに値する部分(Djangoにおけるフィールド)
    #カラム名    = 制約(CharFieldで文字列型のフィールド、max_lengthで2000文字を上限とする、デフォルトで未入力禁止)
    comment     = models.CharField(verbose_name="コメント",max_length=2000)

    #defaultありのフィールド追加(そのままマイグレーションできる)
    #既に存在するデータにはマイグレーションされた時刻がセットされる。だから出来れば最初から投稿日時を記録するフィールドを作っておいたほうが良い。
    dt = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)

    #defaultなしのフィールドを追加する(この場合警告が出る)
    title = models.CharField(verbose_name="タイトル",max_length=200)


    """
    #本のジャンル(1対多のリレーション)
    #本のタイトル(文字列型)
    #ISBN
    #本の画像のURL(ImageFieldではない)
    #本の概要説明(文字列型)
    """

    #ISBNは10桁もしくは13桁の数値である(ただし数値型として扱うことはなく、文字列として扱うため、CharFieldを使う。)
    #isbn        = models.CharField(verbose_name="ISBN",max_length=13)

    #サムネイルはURLなのでURLFieldを使う(これでhttpもしくはhttpsから始まるURLだけ入力を許す。(デフォルトでmax_lengthは200までとなっている))
    #thumbnail   = models.URLField(verbose_name="サムネイル",null=True,blank=True)



    def __str__(self):
        return self.comment
