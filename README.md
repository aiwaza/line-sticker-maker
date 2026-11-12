# 写真1枚からLINEスタンプ / 사진 한 장으로 LINE 스탬프

Codex向けの無料スキルです。写真からキャラクターを作り、**静止画・アニメーション**を選んで、制作からLINE Creators Marketへの審査申請まで進めます。

사진 한 장으로 캐릭터를 만들고, 정지형·움직이는형을 골라 LINE 심사 신청까지 안내받는 Codex용 무료 스킬입니다.

## 설치 / インストール

Codexに次の文章を送ってください。Codex에 다음 문장을 보내세요.

```text
このURLのスキルをインストールしてください。
https://github.com/aiwaza/line-sticker-maker/tree/main/skills/line-animated-stickers
```

インストール後、次のメッセージで写真を1枚添付し、次のように依頼します。
설치 후 다음 메시지에 사진 한 장과 함께 요청하세요.

```text
$line-animated-stickers
この写真でLINEスタンプを作りたいです。初めてなので、静止画か動くタイプか、
キャラクタースタイル・個数・言葉・ポーズの提案から登録まで案内してください。
```

한국어로 「이 사진으로 LINE 스탬프를 만들고 싶어. 종류와 스타일, 문구부터 제안해줘」라고 요청해도 됩니다.

## 選んで確認する流れ / 선택하고 확인하는 흐름

1. 静止画かアニメーションかを選ぶ / 정지형·움직이는형 선택
2. 10種類のスタイルや希望の画風から選ぶ / 10가지 스타일 또는 원하는 화풍 선택
3. 自分のキャラクターを確認 / 캐릭터 확인
4. 用途に合う個数・言葉・表情・ポーズを提案してもらう / 개수·문구·표정·포즈 제안과 수정
5. 最初の静止画を確認してから全点制作 / 첫 정지 시안 확인 후 전체 제작
6. 動くタイプは動きも確認 / 움직이는형은 애니메이션 확인
7. 規格検査、メイン・タブ、タイトル・説明、アップロード、同意後の審査申請 / 규격 검사·등록 준비·업로드·동의 후 심사 신청
8. 承認後、許可を得て販売開始 / 승인 후 판매 시작

| 種類 / 종류 | 個数 / 개수 | 最大サイズ / 최대 크기 | 形式 / 형식 |
|---|---|---|---|
| 静止画 / 정지형 | 8・16・24・32・40 | 370×320 | PNG |
| アニメーション / 움직이는형 | 8・16・24 | 320×270 | APNG |

キャラクター名やセリフは利用者が決めます。人物写真・過去のキャラクター作品・アカウント情報は同梱していません。
캐릭터 이름과 문구는 사용자가 정합니다. 개인 사진, 기존 캐릭터 작품과 계정 정보는 포함하지 않습니다.

## 必要な環境 / 실행 환경

- スキルを使えるCodex環境と、画像生成・ファイル処理・ブラウザー操作の機能が必要です。通常のChatGPTにURLを貼るだけで自動実行されるものではありません。
- スキルは無料配布です。AIサービスの利用料や生成制限は利用するサービスに従います。
- LINEのログイン・本人情報の入力・最後の権利同意には利用者の操作や確認が必要です。審査合格は保証しません。
- PNG/APNG検査スクリプトにはPython 3とPillowが必要です。

## 規格検査 / 규격 검사

```sh
python3 -m pip install -r requirements.txt
python3 skills/line-animated-stickers/scripts/validate_line_package.py upload.zip --type static
# アニメーション / 움직이는형:
python3 skills/line-animated-stickers/scripts/validate_line_package.py upload.zip --type animated
```

検査は読み取り専用です。ZIPの構成、サイズ、透過、静止画/アニメーションの違い、フレーム数や再生時間などを確認します。絵の美しさ、権利、LINEサーバーでの受理は別途確認が必要です。

```sh
python3 -m unittest discover -s skills/line-animated-stickers/scripts -p 'test_validate_line_package.py'
```

公式規格: [静止画](https://creator.line.me/ja/guideline/sticker/) / [アニメーション](https://creator.line.me/ja/guideline/animationsticker/)

作成: **aiwaza**
