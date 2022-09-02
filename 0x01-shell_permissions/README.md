# Shell, Permission 

## Switching between user 
``` 
#!/bin/bash 
su betty #this changes the current user to betty
``` 

## who am i 
`````
#!/bin/bash 
whoami
`````

## Let Print Some Groups 
``` 
#!/bin/bash 
groups 
``` 

##John Doe 
``` 
#!/bin/bash 
chown 763
```
## Who is the owner 
``` 
#!/bin/bash
chown somzzy hello.c 
```

## just empty 
``` 
#!/bin/bash 
touch hello 
```

## Add x to hello 
``` 
#!/bin/bash 
chmod u+x hello 
```

## Give them right to read as person, execute as a group and write as a f**king god 

```
#!/bin/bash 
chmod 754 hello 
``` 

## Give all the power of the god but not all the power 
````
#!/bin/bash 
chmod +551 hello 
````

## james Bond mode 
``` 
#!/bin/bash 
chmod =007 hello
// very weird permission 
```

## Creating a mirror 
``` 
#!/bin/bash 
chmod --reference=olleh hello 
``` 

## Add permission to dir 
~~
#!/bin/bash 
chmod +111 $(find * -type f)
~~

## Add permission and create dir 
``` 
#!/bin/bash 
mkdir -m 751 my_dir 
``` 

## Changing group owner 
``` 
#!/bin/bash 
chown :school hello 
``` 

## Recursively change owner and group 
``` 
#!/bin/bash 
chown -R vincent:staff *
```

## You are not Safe 
``` 
#!/bin/bash 
chown -h vincent:staff _hello 
``` 

