from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):

    #ISBNは10桁もしくは13桁の数値である(ただし数値型として扱うことはなく、文字列として扱うため、CharFieldを使う。)
    isbn = models.CharField(verbose_name="ISBN", max_length=13)
    dt = models.DateTimeField(verbose_name="追加日時", default=timezone.now)

    #書籍検索スクリプトが自動入力するものに関しては、新規作成時に空欄にしておくことを許可する。
    #(一旦新規作成を許可して、残りの未入力箇所は検索スクリプトが記入していく形式)
    title = models.CharField(verbose_name="タイトル",max_length=200,null=True,blank=True)
    author = models.CharField(verbose_name="著者", max_length=50, null=True, blank=True)
    description = models.CharField(verbose_name="説明文",max_length=1000,null=True,blank=True)
    published = models.DateField(verbose_name="出版日", null=True, blank=True)

    #サムネイルはURLなのでURLFieldを使う(これでhttpもしくはhttpsから始まるURLだけ入力を許す。(デフォルトでmax_lengthは200までとなっている))
    thumbnail = models.URLField(verbose_name="サムネイル",null=True,blank=True)
    info = models.URLField(verbose_name="詳細情報", null=True, blank=True)


    #下記は記録方法を考慮する。
    #出版日(書籍によっては年月日ではなく年月だけの場合がある)、年月のみの場合は1日で
    #著者(書籍によって複数人いる。)、複数人いる場合は一人目だけ
    #詳細のURL(infoLink)
