# Cheatsheets

## Linux

### Filesystem Hierarchy Standard

Linux filesystem root directories and their respective purposes. According to the [Filesystem Hierarchy Standard 3.0](http://refspecs.linuxfoundation.org/fhs.shtml).

| Directory |                                Purpose                               |
|:---------:|:--------------------------------------------------------------------:|
| bin       | Essential binaries                                                   |
| boot      | Static boot-related files                                            |
| dev       | Device files                                                         |
| etc       | Host-specific system configuration.                                  |
| lib       | Essential shared libraries and kernel modules                        |
| media     | Mount point for removable media                                      |
| mnt       | Mount point for temporarily mounting a filesystem                    |
| opt       | Add-on software                                                      |
| run       | Data relevant to running processes; /var/run is used more frequently |
| sbin      | Essential system binaries                                            |
| srv       | Data for services provided                                           |
| tmp       | Temporary files                                                      |
| usr       | Secondary hierarchy; identical to primary (root) hierarchy           |
| var       | Variable (non-static) data                                           |
