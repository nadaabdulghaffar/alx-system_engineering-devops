# create a manifest that kills a process named killmenow
excu { 'Kill_killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
