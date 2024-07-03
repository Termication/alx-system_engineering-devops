# creating the manifest that kills a process

exec { 'pkill':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
