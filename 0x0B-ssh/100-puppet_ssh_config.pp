# create ssh client config 
#

$filectn = "HOST * 
  PasswordAuthentication no 
  IdentityFile ~/.ssh/school
"
file {'/root/.ssh/config':
  content => $filectn
}
