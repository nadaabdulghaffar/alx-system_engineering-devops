exec { 'pkill killmenow':
  command  => 'pkill killmenow',
  provider => shell,
  path     => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}
