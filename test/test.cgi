###### Wallet Updater ################################
my $version;
my $VERSION;
$version->{main} = 0; $version->{major} = 1; $version->{minor} = 1;

my $text = get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/version.txt';
my ($MAIN, $MAJOR, $MINOR) = split(/\./, $text); #Split on "." doesnt work?

if($MAIN > $version->{main}){
	print "Updating.. Please restart!";
	my $cgi = gfio::open("wallet.cgi", 'w');
	my $js = gfio::open("wallet.js", 'w');
	my $htm = gfio::open("wallet.htm", 'w');
	my $css = gfio::open("wallet.css", 'w'); 
	$cgi->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/FCC/Wallet/wallet.dev/wallet.cgi');
	$js->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/FCC/Wallet/wallet.dev/wallet.js');
	$htm->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/FCC/Wallet/wallet.dev/wallet.htm');
	$css->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/FCC/Wallet/wallet.dev/wallet.css');
	gfio::closeall;
	exit;
}elsif($MAJOR > $version->{major} && $MAIN >= $version->{main}){
	print "Updating.. Please restart!";
	my $cgi = gfio::open("wallet.cgi", 'w');
	my $js = gfio::open("wallet.js", 'w');
	my $htm = gfio::open("wallet.htm", 'w');
	my $css = gfio::open("wallet.css", 'w'); 
	$cgi->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/FCC/Wallet/wallet.dev/wallet.cgi');
	$js->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/FCC/Wallet/wallet.dev/wallet.js');
	$htm->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/FCC/Wallet/wallet.dev/wallet.htm');
	$css->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/FCC/Wallet/wallet.dev/wallet.css');
	gfio::closeall;
	exit;
}elsif($MINOR > $version->{minor} && $MAJOR >= $version->{major} && $MAIN >= $version->{main}){
	print "Updating.. Please restart!";
	my $cgi = gfio::open("wallet.cgi", 'w');
	my $js = gfio::open("wallet.js", 'w');
	my $htm = gfio::open("wallet.htm", 'w');
	my $css = gfio::open("wallet.css", 'w'); 
	$cgi->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/FCC/Wallet/wallet.dev/wallet.cgi');
	$js->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/FCC/Wallet/wallet.dev/wallet.js');
	$htm->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/FCC/Wallet/wallet.dev/wallet.htm');
	$css->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/FCC/Wallet/wallet.dev/wallet.css');
	gfio::closeall;
	exit;
}else{
	print "No new version";
}

######################################################