# create ssh client config 
#

$filectn = "HOSTS * 
  PasswordAuthentication no 
  IdentityFile ~/.ssh/school
"
file {'/root/.ssh/config':
  content => $filectn
}
