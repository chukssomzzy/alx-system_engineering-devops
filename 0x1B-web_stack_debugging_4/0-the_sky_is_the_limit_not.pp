# Fix issue ulimit issue in default nginx file

exec { 'fix--for--nginx':
  path    => ['/usr/bin', '/bin'],
  cwd     => '/etc/default',
  group   => 'sudo',
  command => "sed -i '/ULIMIT=.-n /s/\d+/5000/1/./'"
  }
