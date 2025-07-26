# contact/views.py

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings # settingsモジュールをインポート

from .forms import ContactForm # ContactFormをインポート

class ContactFormView(FormView):
    template_name = 'contact/contact.html' # 使用するテンプレートのパス
    form_class = ContactForm              # 使用するフォームクラス
    success_url = reverse_lazy('contact:contact_success') # フォーム送信成功後のリダイレクト先（名前空間を含む）

    def form_valid(self, form):
        # フォームがバリデーションを通過した場合に呼ばれるメソッド
        print("form_valid が実行されました。") # デバッグ用追加
        contact_instance = form.save() # データベースに保存し、保存されたインスタンスを取得
        print(f"フォームが保存されました。お問い合わせID: {contact_instance.pk}") # デバッグ用追加

        # --- 管理者への通知メール ---
        admin_subject = f'【お問い合わせ】新しいお問い合わせがありました: {contact_instance.subject}'
        print("管理者メールの準備中...") # デバッグ用追加
        admin_message = render_to_string(
            'contact/email/admin_notification.txt', # 後で作成するテキストテンプレート
            {'contact': contact_instance}
        )
        send_mail(
            admin_subject,
            admin_message,
            settings.DEFAULT_FROM_EMAIL, # 送信元メールアドレス
            [settings.ADMIN_EMAIL],      # 送信先メールアドレス
            fail_silently=False,         # 送信失敗時にエラーを発生させる
        )
        print("管理者メールが送信（コンソール出力）されました。") # デバッグ用追加

        # --- ユーザーへの自動返信メール ---
        user_subject = 'お問い合わせありがとうございます | Praxis Web' # 件名
        print("ユーザーメールの準備中...") # デバッグ用追加
        user_message = render_to_string(
            'contact/email/user_auto_reply.txt', # 後で作成するテキストテンプレート
            {'contact': contact_instance}
        )
        send_mail(
            user_subject,
            user_message,
            settings.DEFAULT_FROM_EMAIL,
            [contact_instance.email], # ユーザーのメールアドレス
            fail_silently=False,
        )
        print("ユーザーメールが送信（コンソール出力）されました。") # デバッグ用追加

        return super().form_valid(form)

    def form_invalid(self, form):
        # フォームがバリデーションに失敗した場合に呼ばれるメソッド
        print("form_invalid が実行されました。フォームはバリデーションに失敗しました。") # デバッグ用追加
        return super().form_invalid(form)

# お問い合わせ完了ページ用のビュー
def contact_success_view(request):
    return render(request, 'contact/contact_success.html')