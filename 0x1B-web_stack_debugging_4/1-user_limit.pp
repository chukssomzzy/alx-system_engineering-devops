# change open file limit for user holberton 

exec { 'change-os-configuration-for-holberton-user':
  'command' => '/bin/sed -i "/holberton .*nofile/ s/[0-9]/65233/" /etc/security/limits.conf',
  'path'    => '/bin'
}
