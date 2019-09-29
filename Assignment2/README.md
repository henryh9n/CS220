# Assignment 2

Foobar is a Python library for dealing with word pluralization.

## Usage

Simply execute the `main.py` as follows
```bash
./main.py
```
The script will automatically create the folders `./files` and 
`./files_new` if those doesn't exist and populate one with 1024 * 256 
files of 1MiB. Then the files will be moved from one directory to
another and back by the 3 different techniques.

The performance time of the operations is shown after each one is 
complete.  


## Performance
I've tested the 3 methods on my 4 code 2.2GHz Intel i7 8GB RAM laptop
with 140MB of files running each of the methods for 10 times. Here are
the results: 

| Method                     | Average duration  |
| -------------------------- | ----------------- |
| Synchronously moving files | 15.99802284319885 |
| Using multiprocessing      | 11.25370084040042 |
| Using threading            | 10.33701734269853 |