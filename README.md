# Bash script file search

File search using **fgrep** and **zenity** as a GUI.


## Dependencies

  * zenity

## Install

* `git clone git: //github.com/webmastak/file-search`
* `cd file-search`
* `cp ~/file-search/local/share/icons/search.png ~/.local/share/icons/search.png`
* `cp ~/file-search/local/bin/search ~/.local/bin/search`
* `cp ~/file-search/local/share/nautilus/scripts/FileSearch ~/.local/share/nautilus/scripts/FileSearch`
* `cp ~/file-search/local/share/nautilus-python/extensions/file-search.py ~/.local/share/nautilus-python/extensions/file-search.py`
* `enjoy`


## Usage

The script **search** file takes the first argument the path to the folder in which the search will be performed. 

Examle: `search /home/user/folder`

If you need another text editor or file manager, then replace strings in file **search**

```
editor="$(which gedit)"
fmanager="$(which nautilus)"
```

## Contributing

* Fork it (<https://github.com/webmastak/nautilus-commandsgit/fork>)
* Create your feature branch (`git checkout -b my-new-feature`)
* Commit your changes (`git commit -am 'Add some feature'`)
* Push to the branch (`git push origin my-new-feature`)
* Create a new Pull Request


## Contributors

- [webmastak](https://github.com/webmastak) - creator and maintainer
