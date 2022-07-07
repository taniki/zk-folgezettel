# fz + folgezettel

Mainly a quick workaround around something I needed to replace Obsidian.md with [zk](https://github.com/mickael-menu/zk) and neovim.

## configuration

In my `~/zettelkasten/.zk/config.toml`

```
# Folgezettel
nextsibling = 'zk-fz-nextsibling.py $ZK_NOTEBOOK_DIR $argv'
nextchild = 'zk-fz-nextchild.py $ZK_NOTEBOOK_DIR $argv'
```

## commands

```
$ zk nextsibling 42.md
$ zk nextchild 42.md
```

