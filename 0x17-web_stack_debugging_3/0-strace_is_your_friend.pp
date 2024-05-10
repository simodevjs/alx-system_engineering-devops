# 0-strace_is_your_friend.pp
# This Puppet manifest is designed to fix a common issue in wp-settings.php
# that could be causing Apache to return a 500 Internal Server Error.

class wordpress_fix {

  # Ensure Apache is installed
  package { 'apache2':
    ensure => installed,
  }

  # Correct a common misconfiguration in WordPress settings
  exec { 'fix-wordpress':
    command => 'sed -i \'s/phpp/php/g\' /var/www/html/wp-settings.php',
    path    => '/bin:/usr/bin:/usr/local/bin',
    unless  => 'grep -q "phpp" /var/www/html/wp-settings.php', # Only run if "phpp" is found
    notify  => Service['apache2'],
  }

  # Ensure the Apache service is running and enabled
  service { 'apache2':
    ensure    => running,
    enable    => true,
    require   => [Package['apache2'], Exec['fix-wordpress']],
  }
}

include wordpress_fix
