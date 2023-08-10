# change the wrong extention name for wp-setting.php 


file { '/var/www/html/wp-settings.php':
  ensure  => present,
  path    => '/var/www/html/wp-settings.php',
  content =>  replace(
    file('/var/www/html/wp-settings.php'),
    "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );",
    "require_once( ABSPATH . WPINC . '/class-wp-locale.php')"
  )
}
