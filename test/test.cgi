#!/usr/bin/perl
use LWP::Simple;
my $version;
$version->{main} = 0; $version->{major} = 0; $version->{minor} = 0;

my $text = get 'https://raw.githubusercontent.com/SkyDrive26/base/dev/test/test.txt';
my ($main, $major, $minor) = split(/\./, $text); #Split on "." doesnt work?

print "Offline: \n";
print $version->{main}.".".$version->{major}.".".$version->{minor}."\n";

print "Online: \n";
print $main.".".$major.".".$minor."\n";

if($version->{main} > $main || $version->{major} > $major || $version->{minor} > $minor){
	print "New version available";