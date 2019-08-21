#install nginx using puppet
package{ "nginx":
ensure => 'present',
}
-> file { '/tmp/holberton':
ensure    => 'present',
  path    => '/var/www/index.html',
  content => 'Holberton School',
}
-> file { '/etc/nginx/sites-available/default':
ensure  => 'present',
}
-> file_line { 'Adding redirection':
  path  => '/etc/nginx/sites-available/default',
  line  => 'server {
        location /redirect_me {
                 return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }',
  match => '^server {',
}

-> exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => 'shell'
}

service { 'nginx':
  ensure => running,
  enable => true,
}
