# 0-strace_is_your_friend.pp
class apache_debug {

  # Ensure Apache is installed and managed
  package { 'apache2':
    ensure => installed,
  }

  # Manage the Apache main configuration with specific content checks
  file { '/etc/apache2/apache2.conf':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('apache/apache2.conf.erb'), # Ensures content is as expected
    notify  => Exec['validate_apache_config'],
  }

  # Validate Apache configuration after any changes
  exec { 'validate_apache_config':
    command     => 'apachectl configtest',
    path        => '/usr/sbin:/usr/local/sbin:/bin:/usr/bin',
    refreshonly => true, # Only run when notified by a change in config
    subscribe   => File['/etc/apache2/apache2.conf'],
    notify      => Service['apache2'],
  }

  # Ensure the service is running and restart on changes
  service { 'apache2':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/apache2/apache2.conf'],
  }
}

include apache_debug
