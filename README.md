# Frequency Analyzer

## Usage

```
$ python3 analyze.py <filename>
```
or
```
$ ./analyze.py <filename>
```

## Examples

Print all words from `TASK.md`:
```
$ ./analyze.py TASK.md
the: 14
a: 9
of: 8
is: 5
must: 5
occurrences: 5
be: 4
in: 4
...
```

Print top 5 words from `bible.txt`:
```
$ ./analyze.py bible.txt | head -n5
the: 64193
and: 51763
of: 34782
to: 13660
that: 12927
```
