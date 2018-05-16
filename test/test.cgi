#!/usr/bin/perl
use LWP::Simple;
use gfio;

my $version;
my $VERSION;
$version->{main} = 0; $version->{major} = 0; $version->{minor} = 1;

my $text = get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/test/test.txt';
my ($MAIN, $MAJOR, $MINOR) = split(/\./, $text); #Split on "." doesnt work?

print "Offline: \n";
print $version->{main}.".".$version->{major}.".".$version->{minor}."\n";

print "Online: \n";
print $MAIN.".".$MAJOR.".".$MINOR."\n";

if($MAIN > $version->{main}){
	print "New version available";
	my $handle = gfio::open("test.cgi", w);
	$handle->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/test/test.cgi');
	gfio::closeall;
}elsif($MAJOR > $version->{major} && $MAIN >= $version->{main}){
	print "New version available";
	my $handle = gfio::open("test.cgi", w);
	$handle->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/test/test.cgi');
	gfio::closeall;
}elsif($MINOR > $version->{minor} && $MAJOR >= $version->{major} && $MAIN >= $version->{main}){
	print "New version available";
	my $handle = gfio::open("test.cgi", w);
	$handle->write(get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/test/test.cgi');
	gfio::closeall;
}else{
	print "No new version";
}

#YAAAAAAAAAAAAAAAAAY I AM THE UPDATED FILE!