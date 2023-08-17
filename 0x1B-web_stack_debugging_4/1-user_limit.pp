# change ulimit for a user os level 

exec { 'change-os-configuration-for-holberton-user':
  path    => ['/usr/bin', '/bin'],
  group   => 'sudo',
  cwd     => '/etc/security',
  command => 'sed -ri "/\<holberton*?[[:digit:]]+\>/ s/[[:digit:]]+/30000" limits.conf'
}
