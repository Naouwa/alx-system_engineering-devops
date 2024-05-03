# Installs flask from pip3.

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['install_pip3'],
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

exec { 'install_pip3':
  command => 'apt-get install -y python3-pip',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
  onlyif  => 'which pip3',
}
