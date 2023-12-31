from django.db import models

from base.models import User


class CareerFormModel(models.Model):
    class Meta:
        verbose_name = 'キャリアフォーム'
        verbose_name_plural = 'キャリアフォーム'

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    question_01 = models.TextField(
        "当社入社前の職歴について記載ください。（年/社名/業種）",
        help_text='''
例）<br>
・20✖✖年✖月～20○○年○月　株式会社ABCD　建築業界の法人営業として従事<br>
・20✖✖年✖月～20○○年○月　株式会社EFGH　広告業界の法人営業として従事<br>
・20✖✖年✖月～20○○年○月　株式会社IJKL　広告業界の営業企画として従事<br>
<br>
※新卒入社の方は「20✖✖年　新卒入社」とご記載ください。<br>
        ''',
        blank=False,
        null=True,
    )
    question_02 = models.TextField(
        "職歴要約を記載ください。",
        help_text='''
例）<br>
大学卒業後、株式会社ABCDの法人営業として入社。<br>
建設業者へ向けた資材の提案営業や納期管理を担当。<br>
その後、営業としてのスキルアップを目的に株式会社EFGHに入社。<br>
広告代理店として様々な業界の法人に向け営業。<br>
株式会社IJKLでは営業企画としてデジタルマーケティングツールの<br>
企画およびリード獲得のための営業向け研修なども担当。<br>
<br>
※新卒入社の方は「新卒入社」とご記載ください。<br>
        ''',
    )
    question_03 = models.TextField(
        "当社でのキャリア要約を記載ください。",
        help_text='''
例）<br>
20◎◎年◎月に△営業所へ営業職として入社。<br>
主に整備・鈑金業を担当し、営業サポートとして従事。<br>
営業サポートの業務の中で顧客期待に応えるサポート業務にやりがいを感じており、 <br>
20◎◎年◎月にコンタクトセンター部へ異動。<br>
リモートオペレーションを中心として全国の顧客フォローを担当。<br>
        ''',
    )
    question_04 = models.TextField(
        "保有している資格について記載ください。",
        help_text='''
例）<br>
・普通自動車運転免許<br>
・ITパスポート　等<br>
        ''',
    )
    question_05 = models.TextField(
        "仕事においてどのようなときにやりがいを感じるか記載ください。",
        help_text='''
        ''',
    )
    question_06 = models.TextField(
        "これまでの社内外での経験から当社で活かせると考えているご自身のスキル・経験を記載ください。",
        help_text='''
例）<br>
・営業職として新規営業をメインに担当したため、市場開拓やマーケティングを用いた業務に自身がある<br>
・営業現場にて大手部品商のサポートを経験したことからパーツマンについて様々な対応が可能<br>
・業務改善を得意とし、日々の業務の自動化を推進することが得意（RPAを使用したリマインドの自動化）<br>
・○○制度の企画等、既存の在り方に捉われず新たな企画推進することができる　　等<br>
        ''',
    )
    question_07 = models.TextField(
        "今後どのようなキャリアデザイン/業務に従事することを望まれるかについて具体的に記載ください。",
        help_text='''
※現状の業務状況やリソース等については考えていただかずにご自身の希望として率直に記載頂いて結構です。<br>
<br>
例）<br>
営業職として顧客への支援を経験する中で「何かを支える」ということに興味を持った。<br>
そのため、顧客への支援ではなく、従業員への支援をしていきたいと強く感じた。<br>
        ''',
    )
    question_08 = models.TextField(
        "当社において前項のキャリアデザイン/業務への従事を叶えることが可能だと思う部門（あるいは業務内容）を教えてください。",
        help_text='''
※現状の業務状況やリソース等については考えていただかずにご自身の希望等を率直に記載ください。<br>
※部署名が記載できない場合は、具体的な業務イメージを記載ください。<br>
        ''',
    )
    question_09 = models.CharField(
        "上記部署への異動が叶う場合、希望する時期を選択ください。",
        help_text='''
※現状の業務状況やリソース等については考えていただかずにご自身の希望等を率直に記載ください。<br>
        ''',
        max_length=255,
        choices=(
            ('できる限り早い異動を希望する', 'できる限り早い異動を希望する'),
            ('希望する部門から受入ニーズがあった際に希望する', '希望する部門から受入ニーズがあった際に希望する'),
            ('未定（異動の希望はあるものの、時期の希望は無し）', '未定（異動の希望はあるものの、時期の希望は無し）'),
            ('異動希望なし（現状の業務を継続したい）', '異動希望なし（現状の業務を継続したい）'),
            ('異動希望なし（特に異動は希望しない）', '異動希望なし（特に異動は希望しない）'),
        )
    )
    timestamp = models.DateTimeField(
        'タイムスタンプ',
        auto_now_add=True,
    )
    email = models.CharField(
        'メールアドレス',
        max_length=255,
    )