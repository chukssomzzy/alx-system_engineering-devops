# change the wrong extention name for wp-setting.php 


file_line { '/var/www/html/wp-settings.php':
  ensure => present,
  path   => '/var/www/html/wp-settings.php',
  line   => "require_once( ABSPATH . WPINC . '/class-wp-locale.php);",
  match  => "^require_once(.*'/class-wp-locale.phpp'.*);$",
}
