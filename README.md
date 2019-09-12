# windows-cds

## Initiative

Linux bash has its `pushd` and `dirs` tool to easily switch to a history directory. `dirs -v` can be used to list history directory with index. `pushd +n` can be used to switch to that directory.

In Windows command line also has its `pushd`, but there is no `dirs` available. Only `popd` can be used to restore history directory one by one.

The purpose of this project is to provide facility on Windows with similar functionality of Linux `pushd` and `dirs`. The name `cds` can be interpreted as `cd with stack` or `cd super`.

## The Script

| Script File | Description |
|-------------|-------------|
| pythonScript\cds.py | python script to change to a dir with the old dir saved in a stack<br>it also provide functionality to list the dir stack, select one of the dir in the stack, and clean the stack|
| pythonScript\cdg.py | python script change to a parent directory with grep functionality |
| batchScript\cds.bat | batch script invoking cds.py |
| batchScript\cdg.bat | batch script invoking cdg.py |

## Installation
Copy `batchScript` and `pythonScript` to your Windows. In environment settings, add `batchScript` to <b>%path%</b>, create a new environment variable <b>%pythondir%</b> point to `pythonScript`.

## Usage

Open a command window. `cds` can be used just like `cd`, but it maintains a dir history file in <b>%userprofile%\dirstack.txt</b>.

`cds -l` list entries in the history file with index

`cds -s <n>` select the nth entry in the directory history

`cds -c` clean the history file

Please see the following example:

```bat
C:>cds Windows\

C:\Windows>cds System32\

C:\Windows\System32>cds drivers\

C:\Windows\System32\drivers>cds "%programfiles%"

C:\Program Files>cds d:\Temp

D:\Temp>cds -l
1 : c:\
2 : c:\Windows
3 : c:\Windows\System32
4 : c:\Windows\System32\drivers

D:\Temp>cds -s 2

C:\Windows>cds -s 4

C:\Windows\System32\drivers>cds -c


C:\Windows\System32\drivers>cds -l

C:\Windows\System32\drivers>cds -h
usage: cds.py [-h] [-l] [-s SELECT] [-c] [path]
positional arguments:
path                  path to to switch to
optional arguments:
-h, --help            show this help message and exit
-l, --list            list directory stack
-s SELECT, --select SELECT
select a dir in stack
-c, --clean           clean directory stack database

C:\Windows\System32\drivers>cdg win

C:\Windows>
```

> <b>Note</b>
>
> If the directory path contains `space` `(` `)`, it must be added with double quote, and must delele the trailing `\`. This is because of the limitation of batch script language
>
> For example
>
> `cds C:\Program Files (x86)` will fail because double quote is not there
>
> `cds "C:\Program Files (x86)\"` will fail because trailing `\` is not removed
>
> `cds "C:\Program Files (x86)"` OK

## License

&copy; Eric Sun

License under [MIT License](LICENSE)
