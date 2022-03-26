from django.shortcuts import render,redirect
from django.views import View

#DBの読み書きをするため、モデルクラスをimportする
from .models import Topic
from .forms import TopicForm


class IndexView(View):

    #リクエストがGETメソッドのときの処理
    def get(self, request, *args, **kwargs):

        #TODO:ここでモデルを使ってDB読み込みの処理
        #Topicモデルクラスを使ってDBに読み込み。手に入れたデータをtopicに入れる。
        topics  = Topic.objects.all()


        print("GETメソッド")
        message = "こんにちは"
        numbers = [1,2,3,4,5,6]
        flag    = True

        for number in numbers:
            print(number)

        context = { "test":message,
                    "numbers":numbers,
                    "flag":flag,
                    "topics":topics,
                    }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):
        print("POSTメソッド")

        #送信されたデータの書き込み処理を行う
        #送信されたフォームタグ内のname属性を元に参照している。
        #print(request.POST["message"])

        """
        # 送信された内容を引数に指定し、モデルクラスのオブジェクトを作る
        topic   = Topic( comment=request.POST["message"] )
        # .save()でDBに書き込みをする
        topic.save()
        """

        #受け取ったPOSTリクエストのボディを引数としてフォームクラスのオブジェクトを作る
        form = TopicForm(request.POST)

        #ルールに基づいていれば、is_valid()はTrueを、ルールに反していればFalseを返す
        if form.is_valid():
            print("バリデーションOK")
            #DBへ書き込みする
            form.save()
        else:
            print("バリデーションNG")
            #エラーの理由を表示させる
            print(form.errors)

        """
        topics  = Topic.objects.all()


        print("GETメソッド")
        message = "こんにちは"
        numbers = [1,2,3,4,5,6]
        flag    = True

        for number in numbers:
            print(number)

        context = { "test":message,
                    "numbers":numbers,
                    "flag":flag,
                    "topics":topics,
                    }

        return render(request,"bbs/index.html",context)
        """

        #POSTでレンダリングするとPOSTレスポンスになるので、リダイレクトを行い、GETメソッドへ誘導する
        # redirect("[app_name]:[name]") urls.pyに指定した、app_nameとnameを組み合わせて誘導先のURLを逆引きして指定する
        return redirect("bbs:index")


index   = IndexView.as_view()

