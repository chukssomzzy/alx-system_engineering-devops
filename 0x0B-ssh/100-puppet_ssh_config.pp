# create ssh client config 
#

$filectn = "HOST * 
  PasswordAuthentication no 
  IdentityFile ~/.ssh/school
"
file {'/home/.ssh/config':
  content => $filectn
}
