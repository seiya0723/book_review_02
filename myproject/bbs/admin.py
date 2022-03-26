from django.contrib import admin

from .models import Topic

class TopicAdmin(admin.ModelAdmin):
    #一覧表示時に表示させるデータ(表示の順番も考慮される)
    list_display = [ "id","dt","comment","title"]




    #保存された時にISBNの検索を行い、取得したデータを追記するため、save_modelのオーバーライドを行う。
    #手順:管理サイトからISBNを記録→下記処理が発動→取得したデータが追記
    #参照:https://noauto-nolife.com/post/django-admin-save-method/

    def save_model(self, request, obj, form, change):

        #ここが保存する処理
        super(TopicAdmin, self).save_model(request, obj, form, change)

        #TODO:この投稿されたデータからISBNを引き出し、NULLになっている書籍のタイトル、サムネイル、出版日、著者などのデータを検索して埋める。
        #投稿されたデータを表示
        print(obj.comment)
        print(obj.dt)
        print(obj.title)

        print("========")
        #このモデルのフォームオブジェクト
        print(form)
        print("========")
        #編集の場合はTrue、新規作成の場合はFalse
        print(change)



admin.site.register(Topic,TopicAdmin)
