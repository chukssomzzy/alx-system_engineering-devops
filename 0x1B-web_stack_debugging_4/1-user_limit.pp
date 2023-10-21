# change open file limit for user holberton 

# exec { 'change-os-configuration-for-holberton-user':
#   'command' => 'sed -i "/holberton .*nofile/ s/[0-9]/65233/" limits.conf',
#   'path'    => '/bin',
#   'cwd'     => '/etc/security',
# }

 exec { 'fix--for-nginx':
  command => 'sed -i "/ULIMIT=\"-n 15\"/ s/15/4096/1" /etc/default/nginx',
  cwd     => '/etc/default',
  path    => '/bin',
} 
