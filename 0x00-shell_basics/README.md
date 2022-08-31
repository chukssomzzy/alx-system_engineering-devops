# Shell Basics

## List All Files and subdirectory 
 ```
 #!/bin/bash 
 # this show the location of bash sheel 
 pwd # this shows the absolute path of a dir
 ```

 ## List Content Of A dir 
 ```
  #!/bin/bash 
  ls  # shows the content of a dir
 ```

 ## Back to home 
 ``` 
    #!bin/bash 
    cd ~
 ```

 ## List file in human readable format 
 ``` 
 #!/bin/bash
 ls -l # this option  `l` format the output using `long format` list ever thing related to the file or dir 
 ```

 ## List all files including hidden file in long format 
 ``` 
 #!/bin/bash 
 ls -la # the option `a` tells `ls` to also include hidden files 
 ```

 ## List hidden file, long format and users and group ids in numeric format 
 ``` 
 #!/bin/bash #shebang #! 
 ls -na # the `n` option is like 'l' option but lists the user and group ids in numbers hope that makes sense 
 ``` 

## hope this works
``` 
 #!/bin/bash 
 mkdir /tmp/my_first_directory/
 ```

## move a file betty 
``` 
#!/bin/bash 
mv /tmp/betty /tmp/my_first_directory/betty 
```

## Delete a file betty 
``` 
#!/bin/bash 
rm  /tmp/my_first_directory/betty  # bye bye betty 
``` 

## Delete a dir 
``` 
#!/bin/bash 
rm -R /tmp/my_first_directory/ # the option 'R' tells remove recursively remove all the file in the dir 
```  

## Back to previous dir 
``` 
#!/bin/bash 
cd .. #moves to the previous dir 
``` 

## List without order 
``` 
#!/bin/bash 
ls -la . .. /boot 
```

## Type of iamafile 
```
#!/bin/bash 
file /tmp/iamafile 
```

## Sym link 
`` 
#!/bin/bash 
ln /bin/ls __ls__ 
``
