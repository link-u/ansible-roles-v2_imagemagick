# imagemagick

![ansible ci](https://github.com/link-u/ansible-roles-v2_imagemagick/workflows/ansible%20ci/badge.svg)

## 概要

imagemagickのインストールを行う  
ソースコードからビルドするのでバージョンが上がっている場合は変数を書き換えること

webpもインストールするので直接webpへの変換も可能

## 動作確認バージョン

- Ubuntu 18.04 (bionic)
- ansible >= 2.8
- Jinja2 2.10.3

## 使い方 (ansible)

### Role variables

```yaml
### インストール設定 ###############################################################################
## 基本設定
imagemagick_install_flag: True  # インストールフラグ

## make install していた名残の変数.
#  * deb に以降する際に make install したファイルを掃除するのに以下の変数は必要
#  * 特に group_vars で修正するような項目はない
imagemagick_version: 7.0.6-0
imagemagick_download_url: "https://github.com/ImageMagick/ImageMagick/archive/{{ imagemagick_version }}.tar.gz"
imagemagick_prefix: "/usr/local"
```

### Example playbook

```yaml
- hosts:
    - servers
  become: True
  roles:
    - { role: imagemagick, tags: ["imagemagick"] }
```

## 後方互換性について

### 削除された変数の一覧

deb パッケージでのインストールに移行したため以下の変数は `group_vars` から削除して頂いて大丈夫です.

* `imagemagick_command_name`
* `imagemagick_dirname`
* `imagemagick_dependencies`
* `imagemagick_download_dest`
* `imagemagick_install_dest`
* `imagemagick_ldconfig_path`
