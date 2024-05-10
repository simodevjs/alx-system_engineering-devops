# Puppet manifest to debug and fix common Apache issues
class web_stack_debugging_3 {

  # Ensure Apache is installed
  package { 'apache2':
    ensure => installed,
  }

  # Ensure the Apache service is running and enabled
  service { 'apache2':
    ensure    => running,
    enable    => true,
    require   => Package['apache2'], # Ensure package is installed before service starts
    subscribe => File['/etc/apache2/apache2.conf', '/etc/apache2/sites-enabled/000-default.conf'],
  }

  # Ensure the main Apache config file exists and has correct permissions
  file { '/etc/apache2/apache2.conf':
    ensure => file,
    owner  => 'root',
    group  => 'root',
    mode   => '0644',
  }

  # Ensure the default site configuration exists and has correct permissions
  file { '/etc/apache2/sites-enabled/000-default.conf':
    ensure => file,
    owner  => 'root',
    group  => 'root',
    mode   => '0644',
    require => Package['apache2'], # Ensure Apache is installed before creating the file
    notify  => Service['apache2'], # Restart Apache if this file changes
  }

  # Optional: Add a debug statement if you need to catch errors or log output
  exec { 'debug_apache_config':
    command     => "/usr/bin/strace -o /tmp/strace_apache.log -tt -e trace=all -p $(pgrep -o apache2)",
    path        => '/usr/bin:/usr/sbin:/bin',
    logoutput   => true,
    refreshonly => true, # Only run when notified by another resource change
    subscribe   => File['/etc/apache2/apache2.conf', '/etc/apache2/sites-enabled/000-default.conf'],
  }
}

include web_stack_debugging_3
