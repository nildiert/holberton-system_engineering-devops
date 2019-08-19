#install nginx using puppet
package{ "nginx":
  ensure => '1.10.3',
}
