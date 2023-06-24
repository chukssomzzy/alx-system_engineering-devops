# excute a command with puppet  

exec { 'killmenow':
  command => 'pkill killmenow',
  onlyif  => 'ps aux | grep killmenow',
  path    => ['/usr/bin']
}
