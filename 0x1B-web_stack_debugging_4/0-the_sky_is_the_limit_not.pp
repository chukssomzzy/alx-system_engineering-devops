# increase the ulimit of nginx process 

exec { 'fix--for-nginx':
  command => 'sed -i /ULIMIT=\"-n 15\"/ s/15/4096/1',
  cwd     => '/etc/default',
  path    => '/usr/bin',
}
