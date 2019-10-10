# Change line
exec { 'Change line':
  command  => 'echo \'ULIMIT="-n 4096"\'',
  provider => 'shell'
}