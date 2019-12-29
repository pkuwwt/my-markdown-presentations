
# How to use `xargs`

## What is `xargs` in Unix/Linux

  * `xargs` is a command utility for build and execution pipeline from standard input.
  * While some tools like `grep` can accept parameters from standard input, many others cannot.
  * With `xargs`, tools like `echo`, `rm` and `mkdir` can accept standard input as arguments.

---

## How to use `xargs`?

  * By default, `xargs` reads items from standard input separated by blanks, and executes one command for each argument.
  * For example, we can create multiple directorys with `mkdir` 

```bash
echo 'one two three' | xargs mkdir
```

---

## How to `xargs` with `find`?

  * The most common usage of `xargs` is to use it with `find`
  * First use `find` to search for files/directories, then use `xargs` to operate on results
  * Typical examples: `rm`, `chown`, `mv`

```bash
# deleting files older than two weeks
find /tmp -mtime +14 -type f | xargs rm -f
```

---

## `xargs` vs. `find -exec`

  * `find` supports `-exec` option to execute arbitrary command on resulting files
  * The following commands are equivalent

```bash
find ./foo -type f -name '*.txt' -exec rm {} \;
find ./foo -type f -name '*.txt' | xargs rm 
```

  * Then which one we should use? `xargs` is much more efficient.
  * When deleting 1000 files, `xargs` is six times more efficient

```bash
time find ./foo -type f -name '*.txt' -exec rm {} \;
0.35s user 0.11s system 99% cpu 0.467 total
find ./foo -type f -name '*.txt' | xargs rm 
0.00s user 0.01s system 75% cpu 0.016 total
```

---

## How to view the command and prompt for execution?

  * Use `xargs -p`
  * It is useful to avoid destrutive commands from running

```bash
echo 'one two three' | xargs -p touch
touch one two three?...
```

---

## How to run multiple commands with `xargs`?

  * Use `xargs -I`
  * `-I` provides a placeholder to use each argument of `xargs`

```bash
echo -e 'one\ntwo\nthree' | xargs -I % sh -c 'echo %; mkdir %'
```

Results:
```
one
two
three
```

---

## References

  * [Linux and Unix xargs command tutorial with examples](https://shapeshed.com/unix-xargs/)

