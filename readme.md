# fz + folgezettel

Workaround around something I needed to replace Obsidian.md with [zk](https://github.com/mickael-menu/zk) and neovim. Sorry if the code seems ugly. The purpose was mainly to get it out of my head.

## configuration

In my `~/zettelkasten/.zk/config.toml`

```
# Folgezettel
nextsibling = 'zk-fz-nextsibling.py $ZK_NOTEBOOK_DIR $argv'
children = 'eval "zk list $(zk-fz-children.py $ZK_NOTEBOOK_DIR 
$argv) $argv"'
nextchild = 'zk-fz-nextchild.py $ZK_NOTEBOOK_DIR $argv'
```

## commands

```
$ zk nextsibling 42.md
$ zk nextchild 42.md
$ zk children 42.md
```

