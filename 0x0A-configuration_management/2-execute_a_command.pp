# Create a manifest that kills a process named killmenow.

exec { 'pkill':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
