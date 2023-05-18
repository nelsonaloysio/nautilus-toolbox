# nautilus-toolbox

Restores **type ahead** (jump to file) and **backspace to parent folder** features to **Nautilus** (**GNOME Files**).

The guide below is aimed at Fedora Linux, but should work with any other Linux distribution.

Additionally, the shortcut `<Alt>C` opens a Terminal in the host system from the current working directory.

## Instructions

### Create virtual environment

Create a Toolbox container with Fedora 36 (GNOME 42):

```
toolbox create -d fedora -r 36 fedora-toolbox-36
```

### Install patched Nautilus

Enter the Toolbox container, update and install Nautilus:

```
toolbox enter fedora-toolbox-36

dnf update

dnf install -y nautilus \
               nautilus-extensions \
               nautilus-python
```

Replace the Nautilus package with the patched versions:

```
dnf install -y rpm/nautilus*.rpm
```

Aftewards, copy the files in `config` and `local` accordingly:

```
mkdir -p ~/.config/nautilus \
         ~/.local/share/nautilus/scripts \
         ~/.local/share/nautilus-python/extensions

cp config/nautilus/scripts-accels ~/.config/nautilus/

cp local/share/nautilus/scripts/Terminal ~/.local/share/nautilus/scripts/

cp local/share/nautilus-python/extensions/CustomShortcuts.py ~/.local/share/nautilus-python/extensions
```

### (Recommended) Copy application shortcut/icons

Create a new `.desktop` shortcut pointing to patched Nautilus:

```
mkdir -p ~/.local/share/applications \
         ~/.local/share/icons/hicolor/scalable/apps \
         ~/.local/share/icons/hicolor/symbolic/apps

cp local/share/applications/nautilus.desktop \
    ~/.local/share/applications/

cp local/share/icons/hicolor/scalable/apps/nautilus.png \
    ~/.local/share/icons/hicolor/scalable/apps/

cp local/share/icons/hicolor/symbolic/apps/nautilus.png \
    ~/.local/share/icons/hicolor/symbolic/apps/

sudo cp bin/nautilus /usr/local/bin/
```

### (Optional) Remove base package

On **Fedora Silverblue** only, the default Nautilus package might be removed with:

```
rpm-ostree override remove nautilus gnome-classic-session
```

## Known limitations

* As we are running Nautilus in a container, only files available from within (e.g., inside `/home/$USER`) will be accessible from the file manager.

* Even though the launcher works as expected and can be pinned in the dock, a new running program will also appear whenever Nautilus is opened.

___

If you care about type ahead in Nautilus, make sure to [show your support](https://gitlab.gnome.org/Teams/Design/whiteboards/-/issues/142) in the current discussion.
