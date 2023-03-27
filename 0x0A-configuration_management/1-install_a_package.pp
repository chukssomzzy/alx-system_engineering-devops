# install flask and pip3
# Requirements 
# install flask 
# version must be 2.1.0 

exec { 'pip install flask==2.1.0':
  command => 'pip install flask==2.1.0',
  path    => '/usr/bin',
  onlyif  => 'test `pip freeze | grep flask`="flask==2.1.0"'
}
