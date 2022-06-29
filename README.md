# SHA-1 Checksum of files in Python

## Usage
To use this script you run main.py giving oprion and argument which is path to directory:

### Linux
Depending of Distribution you use either python or python3 command

```console
python main.py [OPTION] [DIRPath]
```
or
```console
python3 main.py [OPTION] [DIRPath]
```

### Windows
```powershell
python main.py [OPTION] [DIRPath]
```

## Options

### -h
Displays help message for this program

### -r
Recursive option. If there are inner directories program will loop through them as well.

## Reuslt File
This script generates results file called <i>results.txt</i> in format:
```
filename.com;SHA-1Key
```
to import to excel spreadsheet
