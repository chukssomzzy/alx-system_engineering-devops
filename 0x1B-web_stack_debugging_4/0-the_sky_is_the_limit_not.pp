# increase the ulimit of nginx process 

exec { 'fix--for-nginx':
  command => 'sed -i "/ULIMIT=\"-n 15\"/ s/15/4096/1" /etc/default/nginx',
  cwd     => '/etc/default',
  path    => '/bin',
}

exec { 'reload--nginx':
  command => '/usr/sbin/service nginx restart',
}
