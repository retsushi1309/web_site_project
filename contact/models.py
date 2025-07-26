# contact/models.py (修正案)

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='お名前')
    email = models.EmailField(verbose_name='メールアドレス')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='電話番号') # 追加: 電話番号は任意のためblank=True, null=True
    subject = models.CharField(max_length=200, verbose_name='件名')

    # ご相談内容の種類
    INQUIRY_TYPE_CHOICES = [
        ('website', 'Webサイト制作'),
        ('maintenance', '保守・更新'),
        ('consulting', '相談・見積もり'),
        ('other', 'その他'),
    ]
    inquiry_type = models.CharField(
        max_length=50,
        choices=INQUIRY_TYPE_CHOICES,
        default='other',
        verbose_name='ご相談内容の種類'
    )

    # ご希望の連絡方法
    CONTACT_METHOD_CHOICES = [
        ('email', 'メール'),
        ('phone', '電話'),
        ('either', 'どちらでも可'),
    ]
    contact_method = models.CharField(
        max_length=20,
        choices=CONTACT_METHOD_CHOICES,
        default='email',
        verbose_name='ご希望の連絡方法'
    )

    message = models.TextField(verbose_name='お問い合わせ内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='お問い合わせ日時')
    replied = models.BooleanField(default=False, verbose_name='返信済み')
    # 返信内容を保存するフィールドを追加
    reply_message = models.TextField(blank=True, null=True, verbose_name='返信内容')
    replied_at = models.DateTimeField(blank=True, null=True, verbose_name='返信日時')


    def __str__(self):
        return f'{self.subject} from {self.name} ({self.created_at.strftime("%Y-%m-%d %H:%M")})'

    class Meta:
        verbose_name = 'お問い合わせ'
        verbose_name_plural = 'お問い合わせ'
        ordering = ['-created_at'] # 新しいお問い合わせが上に表示されるようにする