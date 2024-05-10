file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('apache/000-default.erb'), # You need to have this template in your Puppet module
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure => 'running',
  enable => true,
}

