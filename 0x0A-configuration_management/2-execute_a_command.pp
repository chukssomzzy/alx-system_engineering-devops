# kills a process named killmenow

exec {'pkill killmenow':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
  path    => '/usr/bin'
}
