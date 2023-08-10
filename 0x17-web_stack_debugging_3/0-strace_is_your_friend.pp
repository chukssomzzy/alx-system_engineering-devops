# change the wrong extention name for wp-setting.php 

exec { 'replace_line':
  path    => '/usr/bin/bash',
  command => "sed -i 's/^require_once(.*class-wp-locale.phpp.*);$/require_once( ABSPATH . WPINC . \"\/class-wp-locale.php\");/1' 
  /var/www/html/wp-settings.php",
  onlyif  => "grep -q '^require_once(.*class-wp-locale.phpp.*);$/' /var/www/html/wp-settings.php",
}
