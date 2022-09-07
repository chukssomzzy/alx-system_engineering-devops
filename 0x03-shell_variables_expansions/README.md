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
