import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_installed_imagemagick(host):
    assert host.package("imagemagick").is_installed

def test_created_symlink(host):
    prefix = host.ansible.get_variables()["imagemagick_prefix"]
    commands = [
        "Magick++-config",
        "MagickCore-config",
        "MagickWand-config",
        "magick",
        "animate",
        "compare",
        "composite",
        "conjure",
        "convert",
        "display",
        "identify",
        "import",
        "magick-script",
        "mogrify",
        "montage",
        "stream"
    ]

    for com in commands:
        symlink_com = prefix + "/bin/" + com
        assert host.file(symlink_com).is_symlink
        linked_com = host.run("readlink " + symlink_com).stdout.splitlines()[0]
        assert linked_com == ("/usr/bin/" + com)
