# Shell, Init

## alias 
```bash
alias ls="rm *"
```

## Hello you
```bash
echo "Hello $(whoami)"
```

## last path
```bash
PATH=$PATH:action
```

## count path 
```bash
echo $PATH | tr ":" " " | wc -w
```

## print env 
```bash 
printenv
```

## print env func locals 
```bash
set
```

## local env
```bash
BEST="School"
```
## global var
```bash
export BEST="School"
```

## using expression
```bash
echo -e "$((128 + $TRUEKNOWLEDGE)) /n"
```

## using expression more divide

```bash 
echo -e "$(($POWER / $DIVIDE))"
```
