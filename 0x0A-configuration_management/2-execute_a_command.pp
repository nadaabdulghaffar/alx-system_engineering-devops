# create a manifest that kills a process named killmenow
exec { 'pkill killmenow':
  command  => 'pkill killmenow',
  provider => shell,
  path     => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}
