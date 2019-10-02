# Sed command
file_line { 'Exec file':
  path  => '/var/www/html/wp-settings.php',
  line  => 'require_once( ABSPATH . WPINC . "/class-wp-locale.php" );',
  match => 'phpp'
}