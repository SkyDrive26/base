###### Wallet Updater by SkyDrive ################################
my $version;
my $VERSION;
$version->{main} = 1; $version->{major} = 1; $version->{minor} = 1;

my $text = get 'https://raw.githubusercontent.com/SkyDrive26/base/master/version.txt';
my ($MAIN, $MAJOR, $MINOR) = split(/\./, $text); #Split on "." doesnt work?
print "Our version is: ".$version->{main}.".".$version->{major}.".".$version->{minor}."\n";
print "Github version is: ".$MAIN.".".$MAJOR.".".$MINOR."\n";

if($MAIN > $version->{main}){
	print "Updating.. Please restart!";
	my $cgi = gfio::open("wallet.cgi", 'w');
	my $js = gfio::open("wallet.js", 'w');
	my $htm = gfio::open("wallet.htm", 'w');
	my $css = gfio::open("wallet.css", 'w'); 
	$cgi->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/master/FCC/Wallet/wallet.dev/wallet.cgi');
	$js->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/master/FCC/Wallet/wallet.dev/wallet.js');
	$htm->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/master/FCC/Wallet/wallet.dev/wallet.htm');
	$css->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/master/FCC/Wallet/wallet.dev/wallet.css');
	gfio::closeall;
	exec("perl wallet.cgi");
	exit;
}elsif($MAJOR > $version->{major} && $MAIN >= $version->{main}){
	print "Updating.. Please restart!";
	my $cgi = gfio::open("wallet.cgi", 'w');
	my $js = gfio::open("wallet.js", 'w');
	my $htm = gfio::open("wallet.htm", 'w');
	my $css = gfio::open("wallet.css", 'w'); 
	$cgi->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/master/FCC/Wallet/wallet.dev/wallet.cgi');
	$js->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/master/FCC/Wallet/wallet.dev/wallet.js');
	$htm->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/master/FCC/Wallet/wallet.dev/wallet.htm');
	$css->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/master/FCC/Wallet/wallet.dev/wallet.css');
	gfio::closeall;
	exec("perl wallet.cgi");
	exit;
}elsif($MINOR > $version->{minor} && $MAJOR >= $version->{major} && $MAIN >= $version->{main}){
	print "Updating.. Please restart!";
	my $cgi = gfio::open("wallet.cgi", 'w');
	my $js = gfio::open("wallet.js", 'w');
	my $htm = gfio::open("wallet.htm", 'w');
	my $css = gfio::open("wallet.css", 'w'); 
	$cgi->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/master/FCC/Wallet/wallet.dev/wallet.cgi');
	$js->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/master/FCC/Wallet/wallet.dev/wallet.js');
	$htm->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/master/FCC/Wallet/wallet.dev/wallet.htm');
	$css->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/master/FCC/Wallet/wallet.dev/wallet.css');
	gfio::closeall;
	exec("perl wallet.cgi");
	exit;
}

######################################################