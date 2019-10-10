# Change line
exec { '/etc/default/nginx':
  command  => "echo 'ULIMIT=\"-n 4096\"' > /etc/default/nginx",
  provider => 'shell'
}
-> exec { 'Restart Nginx':
  command  => 'sudo service nginx restart',
  provider => 'shell'
}