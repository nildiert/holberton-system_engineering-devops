# Sed command
file_line { 'Exec file':
  path  => '/var/www/html/wp-settings.php',
  line  => 'php',
  match => 'phpp'
}
