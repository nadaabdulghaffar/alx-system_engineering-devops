# create a manifest that kills a process named killmenow
exec { 'kill_killmenow':
  command  => 'kill_killmenow',
  provider => shell,
  path     => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}
