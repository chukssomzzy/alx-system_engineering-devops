# Shell, Redirections 

## Saying Hello 
```bash
#!/bin/bash
echo -e "Hello World"
``` 
## Confused the send a confusef face 
```bash 
#!/bin/bash
 echo -e "\"(Ôo)'"
 ```

## Display a file to stdoutput
```bash
#!/bin/bash
cat /etc/passwd
``` 
## Display pass amd hosts 
```bash 
#!/bin/bash
cat /etc/{passwd,hosts}
```
## Display 10 tails
```bash
#!/bin/bash
tail /etc/passwd
```

## heads 
```bash
#!/bin/bash
head /etc/passwd #displays 10 lines from the start of file by default
```
## third cat 
```bash
#!/bin/bash
head -3 ./iacta | tail -1 
```
## the tooks alot of time 
```bash 

#!/bin/bash
echo -e "Best School" > '\*\\'\''"Best School"\'\''\\*$\?\*\*\*\*\*:)'
``` 

## Save current state of directory 
```bash 
#!/bin/bash
ls -la > ls_cwd_content
```

## Duplicate last line 
```bash 
#!/bin/bash
tail -1 iacta >> iacta
```

## No more js
```bash 
#!/bin/bash
find . -name "*.js" -type f -delete
```

## get em dirs
```bash
#!/bin/bash
find . -mindepth -type d | wc -l
```

## list by timestamps 
```bash 
#!/bin/bash
ls -t | head
```
## Check for dub 
```bash
#!/bin/bash
sort -u -c 
```

## Search file with pattern 
```bash
#!/bin/bash
grep "root" /etc/passwd
```

## Display line number with bin
```bash
#!/bin/bash
grep "bin" /etc/passwd | wc -l
```
## Display those below
```bash
#!/bin/bash
grep -A 3 "bin" /etc/passwd
```

## No one like the bin
```
#!/bin/bash
grep -v "bin" /etc/passwd
```

## Grab all lines beginning with a letter 
```bash
#!/bin/bash
grep [[:alpha:]] /etc/ssh/sshd_config
```
## Translate this letters 
```bash
#!/bin/bash
tr 'Ac' 'Ce'
```

## It better to delete than translate 
```bash
#!/bin/bash
tr -d 'cC' 
```

## REVERSE 
```bash
#!/bin/bash
rev 
```

## CUT! 
```bash 
#!/bin/bash
cut -d: -f 1,6 /etc/bash 
```

## find empty files 
```bash
#!/bin/bash
find . -empty -printf "%f\n"
```
## 101- gifs 
```bash
#!/bin/bash
find . -type f -name "*.gif" -printf "%f\n"| rev | cut -d '.' -f2- | rev | LC_ALL=C sort -f
```

## Acoutic 
```bash
#!/bin/bash
echo -ne $(cut -c-1 | tr -d '\n')'\n 
```

## Biggest Fans 
 ```bash 
 #!/bin/bash
 tail -n +2 | cut -f1 | sort | uniq -c | sort -nr | head -11 | tr -s ' ' | cut -d' ' -f3
 ```
