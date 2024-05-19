# Define a class for Nginx installation and configuration
class nginx_web_server {

    # Ensure the package list is up to date
    exec { 'update_system':
        command => '/usr/bin/apt-get update -qq',
        path    => ['/usr/bin', '/usr/sbin'],
        before  => Package['nginx'],
    }

    # Install Nginx package
    package { 'nginx':
        ensure => installed,
    }

    # Ensure the Nginx configuration file is set up correctly
    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /error_404.html;
}
",
        notify  => Service['nginx'],
    }

    # Create the custom error page
    file { '/var/www/html/error_404.html':
        ensure  => file,
        content => "Ceci n'est pas une page",
        owner   => 'www-data',
        group   => 'www-data',
        mode    => '0644',
    }

    # Ensure the index.html file contains 'Hello World!'
    file { '/var/www/html/index.html':
        ensure  => file,
        content => 'Hello World!',
        owner   => 'www-data',
        group   => 'www-data',
        mode    => '0644'
    }

    # Ensure the default site is enabled by creating a symbolic link
    file { '/etc/nginx/sites-enabled/default':
        ensure => link,
        target => '/etc/nginx/sites-available/default',
        require => File['/etc/nginx/sites-available/default'],
    }

    # Ensure Nginx service is running and enabled at boot
    service { 'nginx':
        ensure  => running,
        enable  => true,
        require => Package['nginx'],
    }
}

# Include the class to install and configure Nginx
include nginx_web_server
