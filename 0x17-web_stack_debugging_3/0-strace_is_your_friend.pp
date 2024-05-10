# 0-strace_is_your_friend.pp
# Ensures that Apache does not have common configuration or permission issues

class apache_fix {

  # Ensure Apache is installed
  package { 'apache2':
    ensure => installed,
  }

  # Ensure the Apache service is running and enabled
  service { 'apache2':
    ensure    => running,
    enable    => true,
    require   => Package['apache2'],
    subscribe => File['/etc/apache2/apache2.conf'],
  }

  # Check and fix the permissions of the Apache configuration file
  file { '/etc/apache2/apache2.conf':
    ensure => file,
    owner  => 'root',
    group  => 'root',
    mode   => '0644',
    notify => Service['apache2'], # Restart Apache if this file is changed
  }

  # Optional: Use strace to debug Apache startup issues
  exec { 'debug_apache_startup':
    command     => 'strace -o /tmp/strace_apache.log -ff -e trace=network,open,read,write -p $(pgrep -o apache2)',
    path        => '/usr/bin:/usr/sbin:/bin',
    unless      => 'pgrep -x apache2', # Only run if Apache is not running
    logoutput   => true,
    require     => Service['apache2'], # Ensure Apache is running before debugging
  }
}

include apache_fix
