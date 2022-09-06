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

