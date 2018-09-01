# Basic coding test for DevOps

Please write a program that reads a file with following type of information:
```yaml
checks:
     ping:
          google: google.com:443
          mysite: mytest.test:443
```
(It might be yaml, json or any other text format of your choice, just keep extendable structure)
A program shall check connectivity to sites and show an output similar to this:

```bash
$ ./myceck.sh myinput.yaml
✔ google
✗ mysite

```
Context: rhel/centos 6/7, any language executable on os (bash, java, go, python, ruby or any other language of your choice). Dependencies allowed, just explicitly describe them.
Estimated time is 15-20 minutes. Bonus points for code quality and a git repo with commit history.
