# install nginx using puppet
exec { 'apt-update':
     command => '/usr/bin/apt-get -y update'
}
-> package{ "nginx":
ensure => 'present',
}
-> file { '/var/www/html/index.nginx-debian.html':
ensure    => 'present',
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Holberton School',
}
-> file { '/etc/nginx/sites-available/default':
   ensure  => 'present',
}
-> file_line { 'Adding redirection':
   path  => '/etc/nginx/sites-available/default',
   line  => 'server {
            location /redirect_me {
	                     return 301 https://www.youtube.com/watch?v=Mor495gXnNQ;
	    }',
  match => '^server {',
}
-> file_line { 'Adding config':
   path  => '/etc/nginx/nginx.conf',
  line => 'sendfile on;
add_header X-Served-By $hostname;',
   match => 'sendfile on;',
   }
-> exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => 'shell'
}

service { 'nginx':
  ensure => running,
  enable => true,
}
