# create a file to configure ssh to accept no password authenitication and to use an identi

file { '~/.ssh/config':
  ensure  => file,
  path    => "${::HOME}/.ssh/config",
  content => "Host *\n\tPasswordAuthentication no\n\tIdentityFile '~/.ssh/school'\n"
}
