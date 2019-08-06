# kill the proccess killmenow with pp
exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell'
}
