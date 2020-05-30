# imagemagick

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
imagemagick_version: 7.0.6-0
imagemagick_command_name: "convert"
imagemagick_dirname: "ImageMagick-{{ imagemagick_version }}"
imagemagick_download_url: "https://github.com/ImageMagick/ImageMagick/archive/{{ imagemagick_version }}.tar.gz"
imagemagick_dependencies:
  - "libpng-dev"
  - "libjpeg-dev"
  - "libtiff-dev"
  - "libwebp-dev"

imagemagick_prefix: "/usr/local"
imagemagick_download_dest: "{{ imagemagick_prefix }}/src"
imagemagick_install_dest: "{{ imagemagick_prefix }}/bin"
imagemagick_ldconfig_path: "{{ imagemagick_prefix }}/lib"
```

### Example playbook

```yaml
- hosts:
    - servers
  become: True
  roles:
    - { role: imagemagick, tags: ["imagemagick"] }
```
