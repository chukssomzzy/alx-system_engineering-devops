# change the wrong extention name for wp-setting.php 

exec { 'replace_line':
  path    => '/bin/bash',
  command => "sed -i '/require_once(.*class-wp-locale/s/.phpp/php/1' /var/www/html/wp-settings.php",
  onlyif  => "grep -q '^require_once(.*class-wp-locale.phpp.*' /var/www/html/wp-settings.php",
}
