# contact/forms.py

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    # プライバシーポリシーの同意チェックボックスをフォームに追加
    privacy_policy = forms.BooleanField(
        label='プライバシーポリシーに同意する',
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-checkbox'}) # TailwindCSS用にクラスを追加
    )

    class Meta:
        model = Contact
        fields = [
            'name', 'email', 'phone', 'subject',
            'inquiry_type', 'contact_method', 'message'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'お名前を入力してください'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'メールアドレスを入力してください'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '任意：090-1234-5678'}),
            'subject': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'お問い合わせの件名'}),
            'inquiry_type': forms.Select(attrs={'class': 'form-input'}),
            'contact_method': forms.Select(attrs={'class': 'form-input'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'お問い合わせ内容を具体的にご記入ください'}),
        }
        labels = {
            'name': 'お名前',
            'email': 'メールアドレス',
            'phone': '電話番号',
            'subject': '件名',
            'inquiry_type': 'ご相談内容の種類',
            'contact_method': 'ご希望の連絡方法',
            'message': 'お問い合わせ内容',
        }
        # エラーメッセージを日本語化（必要に応じてカスタマイズ）
        error_messages = {
            'name': {
                'required': 'お名前は必須です。',
            },
            'email': {
                'required': 'メールアドレスは必須です。',
                'invalid': '有効なメールアドレスを入力してください。',
            },
            'message': {
                'required': 'お問い合わせ内容は必須です。',
            },
        }

    # プライバシーポリシーのチェックボックスのバリデーション
    def clean_privacy_policy(self):
        privacy_policy = self.cleaned_data.get('privacy_policy')
        if not privacy_policy:
            raise forms.ValidationError('プライバシーポリシーへの同意が必要です。')
        return privacy_policy

    # 全体のバリデーション（例：電話番号が入力された場合のみ形式をチェックするなど、複雑なバリデーションが必要な場合に使用）
    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        # ここに電話番号の形式チェックなど、追加のバリデーションロジックを書くことができます
        return cleaned_data