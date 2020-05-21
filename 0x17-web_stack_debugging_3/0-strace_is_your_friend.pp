# fix it and then automate it using Puppet
exec { 'fixing error 500':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => ['/bin']
}
