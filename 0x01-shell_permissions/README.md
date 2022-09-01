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
chmod 114 hello 
``` 

