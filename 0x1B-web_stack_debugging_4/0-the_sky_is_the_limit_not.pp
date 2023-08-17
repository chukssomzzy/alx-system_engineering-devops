# Fix issue ulimit issue in default nginx file

exec { 'fix--for--nginx':
  path    => ['/usr/bin', '/bin'],
  cwd     => '/etc/default',
  group   => 'sudo',
  command => 'sed -ri "/\<ULIMIT=.-n*\>/ s/[[:digit:]]+/478/1"'
  }
