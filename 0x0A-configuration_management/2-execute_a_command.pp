# create a manifest that kills a process named killmenow
exec { 'pkill killmenow':
  command  => 'kill_killmenow',
  provider => shell,
  path     => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}
