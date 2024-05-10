# 0-strace_is_your_friend.pp
class apache_debug {

  # Ensure Apache and PHP are installed
  package { ['apache2', 'php']:
    ensure => installed,
  }

  # Correct permissions on the Apache configuration directory
  file { '/etc/apache2/':
    ensure  => directory,
    owner   => 'root',
    group   => 'root',
    mode    => '0755',
    recurse => true,
    notify  => Service['apache2'],
  }

  # Ensure the Apache service is running and restart it if there's a change
  service { 'apache2':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/apache2/'],
  }

  # Use exec resource to fix common misconfigurations detected via strace
  exec { 'fix_common_issues':
    command     => 'bash /path/to/fix_script.sh', # This script should contain the fixes based on strace findings
    path        => '/usr/local/bin:/bin:/usr/bin',
    refreshonly => true, # Run only when notified
    subscribe   => File['/etc/apache2/apache2.conf'],
    notify      => Service['apache2'],
  }
}

include apache_debug
