imagemagick
===========

imagemagickのインストールを行う  
ソースコードからビルドするのでバージョンが上がっている場合は変数を書き換えること

webpもインストールするので直接webpへの変換も可能

Requirements
------------

* ubuntu 16.04

Role Variables
--------------

```yaml
imagemagick_version: 7.0.4-2
imagemagick_command_name: convert
imagemagick_dirname: "ImageMagick-{{ imagemagick_version }}"
imagemagick_download_url: "https://www.imagemagick.org/download/{{ imagemagick_dirname }}.tar.gz"
imagemagick_dependencies:
  - libpng-dev
  - libjpeg-dev
  - libtiff-dev
  - libwebp-dev

imagemagick_prefix: /usr/local
imagemagick_download_dest: "{{ imagemagick_prefix }}/src"
imagemagick_install_dest: "{{ imagemagick_prefix }}/bin"
imagemagick_ldconfig_path: "{{ imagemagick_prefix }}/lib"
```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: imagemagick, tags: ["imagemagick"] }

License
-------

BSD

Author Information
------------------

Link-U Inc.
