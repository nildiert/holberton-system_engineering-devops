# Change line
exec { '/etc/default/nginx':
  command  => "sed -i 's/holberton hard nofile 5/holberton hard nofile 1000/' /etc/security/limits.conf",
  provider => 'shell'
}
-> exec { '/etc/security/limits.conf':
  command  => "sed -i 's/holberton soft nofile 4/holberton soft nofile 1000/' /etc/security/limits.conf",
  provider => 'shell'
}
-> exec { 'Restart command':
  command  => 'sysctl -p',
  provider => 'shell'
}