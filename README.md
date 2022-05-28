# 大澤さんの本を読んでDockerfile を書きたくなったので書いてみた

## 参考書籍

[さわって学ぶクラウドインフラ　docker基礎からのコンテナ構築 - 大澤 文孝](https://www.amazon.co.jp/dp/B089VZXX63/ref=cm_sw_r_tw_dp_PV8T2D7AJ0KXCHTHRJBR)

## Dockerfile ベストプラクティス

AWS Summit から引用

### ベースイメージ

適切に選ぶ。

### イメージタグ

タグを適切に指定する。

### ECR First

### マルチステージビルド

### 最小限のレイヤー

### レイヤー順序

### 最小限のパッケージ

不要なパッケージをインストールしない。

### パッケージ管理コマンドのキャッシュ削除

`yum clean all` を実行する。

### Rootless

実行ユーザはrootにしないこと

### 特権フラグの削除

setuid と setgid のパーミッションを削除する。

### No Config

イメージにクレデンシャル/環境毎の設定を含めない。

### Copy First

`ADD` ではなく `COPY` を使う

